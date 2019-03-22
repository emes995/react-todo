import React, { Component } from 'react'
import PropTypes from 'prop-types'

export class TodoItem extends Component {

    getStyle(todo) {
        return {
            backgroundColor: todo.completed ? "#f4f4f4" : "#e6e6e6",
            textDecoration: todo.completed ? "line-through" : "none",
            padding: '10px',
            borderBottom: '1px #ccc dotted'
        }
    }
    
    render() {
        const {id, title} = this.props.todo
        return (
            <div style={this.getStyle(this.props.todo)}>
                <input type="checkbox" onChange={this.props.markComplete.bind(this, id)} />
                {title}
                <button onClick={this.props.deleteCompleted.bind(this, id)} 
                        style={btnStyle}>x</button>
            </div>
        )
    }

    static propTypes = {
        todo: PropTypes.object.isRequired,
        markComplete: PropTypes.func.isRequired,
        deleteCompleted: PropTypes.func.isRequired
    }
}

const btnStyle = {
        background: "#ff0000",
        color: "#fff",
        border: "none",
        padding: "5px 10px",
        borderRadius: "50%",
        cursor: "pointer",
        float: "right"
    }

export default TodoItem
