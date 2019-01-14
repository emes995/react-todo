import React, { Component } from 'react';
import './css/App.css'
import Todos from './components/Todos';
class App extends Component {

    state = {
      todos: [
        {
          id: 1,
          title: 'First to do',
          completed: false

        },
        {
          id: 2,
          title: 'Second to do',
          completed: false

        },
        {
          id: 3,
          title: 'Third to do',
          completed: false

        }
      ]
    }

    markComplete = (id) => {
        console.log(id)
        this.setState({props : this.state.todos.map( todo => {
            if (todo.id === id) {
              todo.completed = !todo.completed
            }
            return todo
          })
        })
    }

    render() {
      return (
        <div className="App">
            <Todos todos={this.state.todos} markComplete={this.markComplete}/>
        </div>
      );
    }
}

export default App;
