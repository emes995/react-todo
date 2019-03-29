import React, { Component } from 'react'

export class Login extends Component {

    handleOnChange = (e) => {
        console.log({[e.target.name]: e.target.value})
    }

    handleOnSubmit = (e) => {
        e.preventDefault()
        console.log('username: ' + {[e.target.name]: e.target.value})
      }

    render() {
        return (
            <form onSubmit={this.handleLogin} style={ {display:"flex"} } >
                <input type="text"
                   name="username"
                   placeholder="Enter username..."
                   style={ {flex:"0.75", padding:"5px"} }
                   onChange={this.handleOnChange}
                   />

                <input type="password"
                   name="password"
                   placeholder="Enter password..."
                   style={ {flex:"0.75", padding:"5px"} }
                   onChange={this.handleOnChange}
                   />
            </form>
        )
    }
}

export default Login