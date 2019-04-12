import React, { Component } from 'react'
import PropTypes from 'prop-types'

export class Login extends Component {

    constructor(props) {
        super(props)
        this.state = {
            username: null,
            password: null
        }
    }

    handleOnChange = (e) => {
        this.setState(
            {[e.target.name]: e.target.value}
        )
    }

    handleLogin = (e) => {
        e.preventDefault()
        this.props.doLogin(this.state['username'], this.state['password'])
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

                <input type="submit"
                  value="Login"
                  className="btn"
                  style={ {flex: '.25'} }
                />
            </form>
        )
    }

    static propTypes = {
        doLogin: PropTypes.func.isRequired
    }
}

export default Login