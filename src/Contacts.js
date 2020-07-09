import React, { Component } from 'react'
import axios from 'axios'
import './UserProfile.css';
import Button from '@material-ui/core/Button';
import logo from './logo.png';



class Contacts extends Component {

    constructor(props) {
        super(props)

        var id = sessionStorage.getItem("id");

        this.state = {

            id: id,
            mgahd: 'False'
        }
    }

    changeHandler = e => {
        this.setState({ [e.target.name]: e.target.value })
    }

    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        axios
            .post('https://maimoji.herokuapp.com/api/contacts', this.state)
            .then(response => {

                var mgahd = response.data.boolean;
                if (mgahd === "True") {

                    window.location.replace("http://localhost:3000/UserProfile")

                } else {
                    alert("Error");
                }
                //document.getElementById("Demo").innerHTML = mgahd;

            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        var contactnames = JSON.parse(window.localStorage.getItem("contactnames")); // Retrieving


        var contactids = JSON.parse(window.localStorage.getItem("contactids")); // Retrieving



        // const items = []

        // for (const [index, value] of elements.entries()) {
        //     items.push(<li key={index}>{value}</li>)

        for (var i = 0; i < 3; i++) {
            console.log(contactnames[i])

        }



        const { id } = this.state
        return (


            <div>
                <div class="card text-center">
                    <div class="card-header">
                        <ul class="nav nav-pills card-header-pills">
                            <li class="nav-item">
                                <a class="nav-link" href="/UserProfile" variant="body2">UserProfile</a>
                            </li>
                            <li class="nav-item">
                                <form class="nav-link active" onSubmit={this.submitHandler}>
                                    <input type="hidden" name="id" value={id} onChange={this.changeHandler} ></input>
                                    <Button
                                        type="submit"

                                    ><font color="white">Contacts</font>
                                    </Button>
                                </form>
                            </li>
                        </ul>
                    </div>
                </div>

                {/* <div>
                    {items}
                </div> */}

                <div>




                    <center>



                        <div class="col-lg-6">
                            <div class="about-avatar">
                                <img src={logo} alt="Logo" />
                            </div>
                        </div>
                        <h1 class="dark-color">Contacts</h1>

                        <h2>

                            <div class="row about-list">
                                <div class="col-md-6">

                                    <ul>
                                        {contactnames.map((value, index) => {
                                            return <li key={index}>{value}</li>
                                        })}
                                    </ul>
                                    
                                        {contactids.map((value, index) => {
                                            return <form onSubmit={this.submitHandler}>
                                                <li key={index}>{value}</li>
                                                <input type= "text">{contactids[index]}</input>
                                                <Button
                                                    type="submit"
                                                > Send
                                                </Button>
                                            </form>
                                        })}
                                 


                                </div>


                            </div>

                        </h2>


                    </center >

                </div >








            </div>


        )
    }
}

export default Contacts