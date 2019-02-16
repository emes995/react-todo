import React, { Component } from 'react'
import PropTypes from 'prop-types'

export class AddTodo extends Component {

    state = {
      title: ""
    }

    handleOnChange = (e) => {this.setState({[e.target.name]: e.target.value})}

    handleOnSubmit = (e) => {
      e.preventDefault()
      if (this.state.title.length > 0 ) {
          this.props.addTodo(this.state.title)
          this.setState({title: ""})
      }
    }

    render() {
      return (
        <form onSubmit={this.handleOnSubmit} style={ {display:"flex"} } >
            <input type="text"
                   name="title"
                   placeholder="Add todo..."
                   style={ {flex:"0.75", padding:"5px"} }
                   value={this.state.title}
                   onChange={this.handleOnChange}
                   />

            <input type="submit"
                  value="Submit"
                  className="btn"
                  style={ {flex: '.25'} }
                  />
        </form>
      )
    }

    static propTypes = {
        addTodo: PropTypes.func.isRequired
    }
}

export default AddTodo
