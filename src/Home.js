import React, { Component } from 'react'
import { Jumbotron, Container, Row, Col, Image } from 'react-bootstrap';
import './Home.css';

export default class Home extends Component {
    render() {
        sessionStorage.clear();
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
                                <a class="nav-link" href="/Signup" variant="body2"><h4>Signup</h4></a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/Signin" variant="body2"><h4>Signin</h4></a>
                            </li>

                        </ul>
                    </div>
                </div>
                </div>
                <br></br>
                <br></br>
                <br></br>
                <Container>
                    <Jumbotron>
                        <Image src="assets/dog-people.jpg" className="header-image" />
                        <h2>Welcome to Maimoji</h2>
                        <p>This is the new future of chating</p>
                    </Jumbotron>
                    <Row className="show-grid text-center">
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
                    </Row>
                </Container>
            </div>
        )
    }
}
