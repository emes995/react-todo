import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  return (
    <div style={headerStyle}>
      <h3>To-dos</h3>
      <Link style={linkStyle} to="/">Home</Link> |
      <Link style={linkStyle} to="/about">About</Link> |
      <Link style={linkStyle} to="/login">Login</Link>
    </div>
  )
}

const headerStyle = {
    backgroundColor: "#333",
    color: "#fff",
    textAlign: "center"
  }

const linkStyle = {
    color: "#fff",
    textDecoration: "none"
}
