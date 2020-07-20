import React, { Component } from 'react'
import axios from 'axios'
import './UserProfile.css';
import logo from './logo.png';
import Button from '@material-ui/core/Button';



class UserProfile extends Component {

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
                console.log(response.data.contactname)
                var mgahd = response.data.boolean;
                if (mgahd === "True") {

                    var loop = response.data.loop;

                    // alert(typeof contactname)
                    var contactids = []
                    var contactnames = []
                    for (var i = 0; i < loop; i++) {
                        const contactname = response.data.contactname[i];
                        const contactid = response.data.contactid[i];
                        contactnames.push(contactname)
                        contactids.push(contactid)

                    }
                    // for (var i = 0 ;i<3; i++) {
                    //    console.log(contactnames[i])

                    // }
                    window.localStorage.setItem("contactnames", JSON.stringify(contactnames)); // Saving
                    window.localStorage.setItem("contactids", JSON.stringify(contactids)); // Saving
                    window.localStorage.setItem("loop", JSON.stringify(loop)); // Saving


                    window.location.replace("http://localhost:3000/Contacts")
                    // window.location.replace("https://maimojiwebapp.herokuapp.com/Contacts")

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
        var idds = sessionStorage.getItem("id");
        if (idds !== null) {



            var mail = sessionStorage.getItem("mail");
            var num = sessionStorage.getItem("num");
            var name = sessionStorage.getItem("name");






            const { id } = this.state
            return (


                <div>
                <div class="fixed-top">
                    <div class="card text-center">
                        <div class="card-header">
                            <ul class="nav nav-pills card-header-pills">
                                <li class="nav-item">
                                    <a class="nav-link active" href="/UserProfile" variant="body2">UserProfile</a>
                                </li>
                                <li class="nav-item">
                                    <form class="nav-link" onSubmit={this.submitHandler}>
                                        <input type="hidden" name="id" value={id} onChange={this.changeHandler} ></input>
                                        <Button
                                            type="submit"
                                        > Contacts
                                    </Button>
                                    </form>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link " href="/AddContact" variant="body2">Add Contact</a>
                                </li>
                                <li class="nav-item">
                                    <a class="p-3 mb-2 bg-danger text-white" href="/" variant="body2">Log Out</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                    </div>
                    <br></br>
                    <br></br>
                    <br></br>

                    <div>




                        <center>



                            <div class="col-lg-6">
                                <div class="about-avatar">
                                    <img src={logo} alt="Logo" />
                                </div>
                            </div>
                            <h1 class="dark-color">User Profile</h1>

                            <h2>

                                <div class="row about-list">
                                    <div class="col-md-6">

                                        <div class="media">
                                            <label>Name</label>
                                            <p>{name}</p>
                                        </div>

                                        <div class="media">
                                            <label> Phone Number </label>
                                            <p>{num}</p>
                                        </div>




                                        <div class="media">
                                            <label>E-mail </label>
                                            <p>{mail}</p>
                                        </div>



                                    </div>


                                </div>

                            </h2>


                        </center >

                    </div >

                </div>

            )


        }
        else{
          window.location.replace("http://localhost:3000/")
            // window.location.replace("https://maimojiwebapp.herokuapp.com/")
        }
    }
}

export default UserProfile
