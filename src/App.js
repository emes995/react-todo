import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';

import './css/App.css'
import Todos from './components/Todos';
import Header from './components/layout/Header';
import AddTodo from './components/AddTodo';
import uuid from 'uuid'
import About from './components/layout/About';
import Axios from 'axios';
class App extends Component {

    state = {
      todos: [ ]
    }

    markComplete = (id) => {
        console.log(id)
        this.setState({props: this.state.todos.map( todo => {
            if (todo.id === id) {
              todo.completed = !todo.completed
            }
            return todo
          })
        })
    }

    deleteCompleted = (id) => {
      console.log("clearing id" + id)
      this.setState({todos: [...this.state.todos.filter( todo => todo.id !== id)]})
    }

    addTodo = (title) => {
      this.setState({todos: [...this.state.todos, {id: uuid.v4(), title: title, completed: false}]})
    }

    componentDidMount() {
      Axios.get("https://jsonplaceholder.typicode.com/todos?_limit=10")
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
              </div>
          </div>
        </Router>
      );
    }
}

export default App;
