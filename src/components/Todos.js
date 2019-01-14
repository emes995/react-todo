import React, { Component } from 'react'
import TodoItem from './TodoItem';
import PropTypes from 'prop-types'

export class Todos extends Component {

    render() {
            return this.props.todos.map( (todo) => (
                <TodoItem key={todo.id} todo={todo} markComplete={this.props.markComplete} 
                          clearComplete={this.props.clearComplete}/>
        ));
    }

    static propTypes = {
        todos: PropTypes.array.isRequired,
        markComplete: PropTypes.func.isRequired,
        clearComplete: PropTypes.func.isRequired
    }
}

export default Todos
