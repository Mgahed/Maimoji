import React, { Component } from 'react'
import axios from 'axios'
import './UserProfile.css';
import Button from '@material-ui/core/Button';



class AddContact extends Component {

    constructor(props) {
        super(props)
        var typo = "typo";
        var id = sessionStorage.getItem("id");

        this.state = {
            typo: typo,
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
            .post('https://maimoji.herokuapp.com/api/addcontact', this.state)
            .then(response => {
                console.log(response.data)
                var mgahd = response.data.boolean;
                var name = response.data.name;

                if (mgahd === "True") {

                    alert(name)


                    // window.location.replace("http://localhost:3000/Contacts")

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

            const { id, typo } = this.state
            var fis = false;
            var loop = JSON.parse(window.localStorage.getItem("loop")); // Retrieving
            fis = loop;
            console.log(loop)
            if (fis === null) {
                return <div>

                    <div class="card text-center">
                        <div class="card-header">
                            <ul class="nav nav-pills card-header-pills">
                                <li class="nav-item">
                                    <a class="nav-link" href="/UserProfile" variant="body2">UserProfile</a>
                                </li>
                                {/* <li class="nav-item">
                            <a class="nav-link " href="/Contacts" variant="body2">Contacts</a>

                        </li> */}
                                <li class="nav-item">
                                    <a class="nav-link active " href="/AddContact" variant="body2">Add Contact</a>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <center>
                        <form class="nav-link" onSubmit={this.submitHandler}>
                            <input type="hidden" name="id" value={id} onChange={this.changeHandler} ></input>
                            <input type="hidden" name="typo" value={typo} onChange={this.changeHandler} ></input>
                            <input type="text" name="mailornum" onChange={this.changeHandler} ></input>
                            <Button
                                type="submit"
                            > Add
                                </Button>
                        </form>
                    </center>
                </div>
            }
            else {
                return <div>

                    <div class="card text-center">
                        <div class="card-header">
                            <ul class="nav nav-pills card-header-pills">
                                <li class="nav-item">
                                    <a class="nav-link" href="/UserProfile" variant="body2">UserProfile</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link " href="/Contacts" variant="body2">Contacts</a>

                                </li>
                                <li class="nav-item">
                                    <a class="nav-link active " href="/AddContact" variant="body2">Add Contact</a>
                                </li>
                                <li class="nav-item">
                                    <a class="p-3 mb-2 bg-danger text-white" href="/" variant="body2">Log Out</a>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <center>
                        <form class="nav-link" onSubmit={this.submitHandler}>
                            <input type="hidden" name="id" value={id} onChange={this.changeHandler} ></input>
                            <input type="hidden" name="typo" value={typo} onChange={this.changeHandler} ></input>
                            <input type="text" name="mailornum" onChange={this.changeHandler} ></input>
                            <Button
                                type="submit"
                            > Add
                                    </Button>
                        </form>
                    </center>
                </div>
            }
        }
        else{
          window.location.replace("http://localhost:3000/")
            // window.location.replace("https://maimojiwebapp.herokuapp.com/")
        }
    }
}

export default AddContact
