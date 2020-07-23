import React, { Component } from 'react'
import { Navbar, Nav, NavItem } from 'react-bootstrap';
import { Link } from 'react-router-dom';


export default class CustomNavbar extends Component {
  render() {
    return (
        <div class="card text-center">
  <div class="card-header">
    <ul class="nav nav-pills card-header-pills">
      <li class="nav-item">
        <a class="nav-link active" href="/" variant="body2">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="/Signup" variant="body2">Signup</a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="/Signin" variant="body2">Signin</a>
      </li>
    </ul>
  </div>
</div>
    )
  }
}
