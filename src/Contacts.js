import React, { Component } from 'react'
import axios from 'axios'
import './UserProfile.css';
import Button from '@material-ui/core/Button';
import logo from './logo.png';



class Contacts extends Component {



    constructor(props) {
        super(props)

        var sender = sessionStorage.getItem("id");
        var x = 2;

        this.state = {

            sender: sender,
            x: x
            // mgahd: 'False'
        }
    }

    changeHandler = e => {
        this.setState({ [e.target.name]: e.target.value })
    }

    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        axios
            .post('https://maimoji.herokuapp.com/api/chathistory', this.state)
            .then(response => {

                var mgahd = response.data.boolean;
                var rec = response.data.reciever;
                var sen = response.data.currentuser
                //  var loops = response.data.loop;
                if (mgahd === "True" && rec !== "") {
                    var messages = []
                    var dates = []
                    var senders = []
                    var recivers = []
                    console.log(response.data)
                    var loops = response.data.looping;
                    for (var i = 0; i < loops; i++) {
                        const message = response.data.msg[i];
                        const date = response.data.date[i];
                        const sender = response.data.sender[i];
                        const reciver = response.data.recivers[i];
                        messages.push(message)
                        dates.push(date)
                        senders.push(sender)
                        recivers.push(reciver)

                    }
                    window.localStorage.setItem("loops", JSON.stringify(loops)); // Saving
                    window.localStorage.setItem("messages", JSON.stringify(messages)); // Saving
                    window.localStorage.setItem("dates", JSON.stringify(dates)); // Saving
                    window.localStorage.setItem("senders", JSON.stringify(senders)); // Saving
                    window.localStorage.setItem("recivers", JSON.stringify(recivers)); // Saving
                    window.localStorage.setItem("rec", JSON.stringify(rec)); // Saving
                    window.localStorage.setItem("sen", JSON.stringify(sen)); // Saving

                    window.location.replace("http://localhost:3000/ChatHistory")
                    // window.location.replace("https://maimojiwebapp.herokuapp.com/ChatHistory")


                } else {
                    alert("Error");
                    console.log(mgahd)
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

            var contactnames = JSON.parse(window.localStorage.getItem("contactnames")); // Retrieving
            // var id = sessionStorage.getItem("id");
            var loop = JSON.parse(window.localStorage.getItem("loop")); // Retrieving
            var contactids = JSON.parse(window.localStorage.getItem("contactids")); // Retrieving



            // const items = []

            // for (const [index, value] of elements.entries()) {
            //     items.push(<li key={index}>{value}</li>)

            var Arr = [];
            for (var i = 0; i < loop; i++) {
                Arr.push(contactnames[i])

            }



            const { sender } = this.state

            return (


                <div>
                <div class="fixed-top">
                    <div class="card text-center">
                        <div class="card-header">
                            <ul class="nav nav-pills card-header-pills">
                                <li class="nav-item">
                                    <a class="nav-link" href="/UserProfile" variant="body2">UserProfile</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link active" href="/Contacts" variant="body2">Contacts</a>

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

                    {/* <div>
                    {items}
                </div> */}

                    <div>

                        <div class="col-lg-6">
                            <div class="about-avatar">
                                <img src={logo} alt="Logo" />
                            </div>
                        </div>
                        <div class="jumbotron">
                        <center><h1 class="dark-color">Contacts</h1></center>
                        <br></br>
                        <br></br>
                        <br></br>
                        <h2>

                            <div class="row about-list">
                                <div class="col-md-6">
                                    <form class="Right" onSubmit={this.submitHandler}>
                                        <input name="sender" type="hidden" value={sender} onChange={this.changeHandler}></input>
                                        {contactids.map((value, index) => {
                                            var z = value;
                                            console.log(z)
                                            // return <option value={z}>{Arr[index]}</option>


                                            return <div>
                                            <div class="card bg-secondary text-white">
                                            <div class="card-body">
                                             <input name="reciver" value={z} type="radio" onChange={this.changeHandler}></input> {Arr[index]}</div>
                                             </div><br></br></div>

                                        })}
                                        {/* {contactnames.map((x, i) => {
                                        return <li >{x}</li>
                                    })} */}
                                        <Button
                                            type="submit"
                                            class="btn btn-info"
                                            Style = "width: 50%; height: 35px;"
                                        >
                                            <h2>select</h2> </Button>
                                    </form>




                                    {/* {contactids.map((value, index) => {
                                            return <form onSubmit={this.submitHandler}>
                                                <li key={index}>{value}</li>
                                                <input type= "text">{contactids[index]}</input>
                                                <Button
                                                    type="submit"
                                                > Send
                                                </Button>
                                            </form>
                                        })} */}



                                </div>


                            </div>

                        </h2>


                          </div >
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

export default Contacts
