import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import './css/App.css'
import Todos from './components/Todos';
import Header from './components/layout/Header';
import AddTodo from './components/AddTodo';
import About from './components/layout/About';
import Login from './components/layout/Login';
import Axios from 'axios';
class App extends Component {

    serverUrl = "http://localhost:8080";

    credentials = {
      user: null,
      password: null
    }

    state = {
      todos: [ ]
    }

    getCredentials() {
      return 'user='+this.credentials.user + '&pwd=' + this.credentials.password
    }

    doLogin = (username, password) => {
      this.credentials.user = username
      this.credentials.password = password

      Axios.post(this.serverUrl + "/login?" + encodeURI(this.getCredentials()))
          .then( res => {
            if (res.data['status'] === 'LOGIN_SUCESSFUL') {
            } else {
              this.credentials.user = null
              this.credentials.password = null
            }
          })
    }

    markComplete = (id) => {
        console.log(id)
        this.setState({props: this.state.todos.map(todo => {
            if (todo.id === id) {
              todo.completed = !todo.completed
              var todoStr = todo.completed ? "True" : "False";
              Axios.post(this.serverUrl + "/update?" + encodeURI(this.getCredentials() + "&title="+todo.title+"&completed="+todoStr+"&id="+todo.id))
                   .then(res => {
                     console.log(res.data)
                   })
            }
            return todo
          })
        })
    }

    deleteCompleted = (id) => {
      Axios.delete(this.serverUrl+"/delete?" + encodeURI(this.getCredentials()+"&id="+id))
          .then(res => {
            console.log(res.data)
            this.setState({todos: [...this.state.todos.filter(todo => todo.id !== res.data["id"])]})
          })
    }

    addTodo = (title) => {
      Axios.post(this.serverUrl + "/insert?" + encodeURI(this.getCredentials() + "&title="+title))
          .then(res => {
            this.setState({todos: [...this.state.todos, {id: res.data["id"], title: res.data["title"], completed: false}]})
          })
    }

    componentDidMount() {
      if (this.credentials.username == null) {
        alert("You must login first")
        return
      }
      Axios.get(this.serverUrl + "/list?" + encodeURI(this.getCredentials()))
          .then( res => {
              this.setState({todos: res.data})
          })
    }

    render() {
      return (
        <Router>
          <div className="App">
              <div className="container">
                  <Header />
                  <Route exact path="/" render={props => (
                      <React.Fragment>
                        <AddTodo addTodo={this.addTodo}/>
                        <Todos todos={this.state.todos} markComplete={this.markComplete}
                              deleteCompleted={this.deleteCompleted}/>  
                      </React.Fragment>
                  )}
                  />
                  <Route path="/about" component={About} />
                  <Route path="/login" render = { (props) => <Login {...props} doLogin={this.doLogin} />} />
              </div>
          </div>
        </Router>
      );
    }
}

export default App;
