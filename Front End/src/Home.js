import React, { Component } from 'react'
import { Jumbotron, Container, Row, Col, Image } from 'react-bootstrap';
import './Home.css';
import './font.css';

export default class Home extends Component {
    render() {
        sessionStorage.clear();
        // setTimeout("location.href = 'http://localhost:3000/Signin';", 3000);
        return (
            <div>
            <div class="fixed-top">
                <div class="card text-center">
                    <div class="card-header">
                        <ul class="nav nav-pills card-header-pills">
                            <li class="nav-item">
                                <a class="nav-link active" href="/" variant="body2"><h4>Home</h4></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/Signup" variant="body2"><h4>Sign up</h4></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/Signin" variant="body2"><h4>Sign in</h4></a>
                            </li>
                            <li class="nav-item">
                                <img  class="nav-link" Style="width:4.7%; float:Right; position: fixed; top:0; right:0;" src="./assets/maimojilogo.png"></img>
                            </li>
                        </ul>
                    </div>
                </div>
                </div>
                <Container>
                    <Jumbotron>
                    <center><h1>Maimoji</h1></center>
                    <br></br>
                    <div id="demo" class="carousel slide" data-ride="carousel">


                      <div class="carousel-inner">
                      <div class="carousel-item active">
                        <img src="assets/gifatk.gif" alt="Los Angeles"></img>
                      </div>
                      <div class="carousel-item">
                        <img src="assets/pinks.jpg" alt="Chicago"></img>
                      </div>
                      <div class="carousel-item">
                        <img src="assets/dog-people.jpg" alt="New York"></img>
                      </div>
                      </div>

                      <a class="carousel-control-prev" href="#demo" data-slide="prev">
                      <span class="carousel-control-prev-icon"></span>
                      </a>
                      <a class="carousel-control-next" href="#demo" data-slide="next">
                      <span class="carousel-control-next-icon"></span>
                      </a>

                      </div>
                        <h2>Welcome to Maimoji</h2>
                        <p>This is the new future of chating</p>
                    </Jumbotron>
                    {/*<Row className="show-grid text-center">
                        <Col xs={12} sm={4} className="person-wrapper">
                            <Image src="assets/person-1.jpg" circle className="profile-pic" />
                            <h3>Mgahd</h3>
                            <p>BackEnd</p>
                        </Col>
                        <Col xs={12} sm={4} className="person-wrapper">
                            <Image src="assets/person-2.jpg" circle className="profile-pic" />
                            <h3>Radwa</h3>
                            <p>FrontEnd</p>
                        </Col>
                        <Col xs={12} sm={4} className="person-wrapper">
                            <Image src="assets/person-3.jpg" circle className="profile-pic" />
                            <h3>Sherif</h3>
                            <p>Algorithm</p>
                        </Col>
                    </Row>*/}
                </Container>
            </div>
        )
    }
}
