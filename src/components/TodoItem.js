import React, { Component } from 'react'
import PropTypes from 'prop-types'

export class TodoItem extends Component {

    getStyle(todo) {
        return {
            backgroundColor: todo.completed ? "#f4f4f4" : "#e6e6e6",
            textDecoration: todo.completed ? "line-through" :  "none",
            padding: '10px',
            borderBottom: '1px #ccc dotted'
        }
    }
    
    render() {
        const {id, title, completed} = this.props.todo
        return (
            <div style={this.getStyle(this.props.todo)}>
                <input type="checkbox" onChange={this.props.markComplete.bind(this, id)} />
                {title}
                <button type="button" class="btn btn-primary ">x</button>
            </div>
        )
    }

    static propTypes = {
        todo: PropTypes.object.isRequired,
        markComplete: PropTypes.func.isRequired
    }
}

export default TodoItem
