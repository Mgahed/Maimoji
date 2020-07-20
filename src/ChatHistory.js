import React, { Component } from 'react'
import axios from 'axios'
import './UserProfile.css';
import Button from '@material-ui/core/Button';
// import logo from './logo.png';
import VideoInput from './views/VideoInput'
// import ScriptTag from 'react-script-tag';
// import faceapii from './faceapii';
// import * as faceapi from 'face-api.js';





class ChatHistory extends (Component) {



    constructor(props) {
        super(props)
        var neutral = sessionStorage.getItem("neutral");
        var happy = sessionStorage.getItem("happy");
        var sad = sessionStorage.getItem("sad");
        var sender = sessionStorage.getItem("id");
        var reciver = JSON.parse(window.localStorage.getItem("rec")); // Retrieving

        this.state = {

            sad: sad,
            happy: happy,
            neutral: neutral,
            sender: sender,
            reciver: reciver
            // mgahd: 'False'
        }
    }

    changeHandler = e => {
        this.setState({ [e.target.name]: e.target.value })
        this.state.neutral = sessionStorage.getItem("neutral");
        this.state.happy = sessionStorage.getItem("happy");
        this.state.sad = sessionStorage.getItem("sad");
        console.log(this.state.neutral);
    }


    submitHandler = e => {
        e.preventDefault()
        console.log(this.state)
        console.log(sessionStorage.getItem("happy"));
        axios
            .post('https://maimoji.herokuapp.com/api/message', this.state)
            .then(response => {

                var mgahd = response.data.boolean;
                //  var loops = response.data.loop;
                console.log(response.data)

                if (mgahd === "True") {
                    var whats = response.data.whatsapp
                    window.location.replace(whats)


                    // console.log(response.data)



                    //   window.location.replace("http://localhost:3000/chathistory")

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


        // require("script")
        var messages = JSON.parse(window.localStorage.getItem("messages")); // Retrieving
        // var id = sessionStorage.getItem("id");
        var loops = JSON.parse(window.localStorage.getItem("loops")); // Retrieving
        var dates = JSON.parse(window.localStorage.getItem("dates")); // Retrieving
        var senders = JSON.parse(window.localStorage.getItem("senders")); // Retrieving
        var recivers = JSON.parse(window.localStorage.getItem("recivers")); // Retrieving

        ///////////////////////////////////////////////////////////////////////////////////////////////////////////////


        //////////////////////////////////////////////////////////////////////



        // const items = []

        // for (const [index, value] of elements.entries()) {
        //     items.push(<li key={index}>{value}</li>)

        var sender1 = [];
        var date1 = [];
        var reciever1 = [];
        var message1 = [];
        for (var i = 0; i < loops; i++) {
            sender1.push(senders[i])
            date1.push(dates[i])
            reciever1.push(recivers[i])
            message1.push(messages[i])


        }



        const { sender, reciver, neutral, happy, sad } = this.state

        console.log("neutral " + neutral);
        return (


            <div>



                {/* <div class="card text-center">
                    <div class="card-header">
                        <ul class="nav nav-pills card-header-pills">
                            <li class="nav-item">
                                <a class="nav-link" href="/UserProfile" variant="body2">UserProfile</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link active" href="/Contacts" variant="body2">Contacts</a>

                            </li>
                        </ul>
                    </div>
                </div> */}

                {/* <div>
                    {items}
                </div> */}

                <div>

                    <div class="col-lg-6">
                        <div class="about-avatar">
                            <VideoInput></VideoInput>
                        </div>
                    </div>
                    <h1 class="dark-color">Chat History</h1>
                    <h2>


                        <div class="row about-list">
                            <div class="col-md-6">

                                {/* <input name="sender" type="hidden" value={sen} onChange={this.changeHandler}></input> */}
                                {dates.map((value, index) => {
                                  // var neutral = sessionStorage.getItem("neutral")
                                  // var happy = sessionStorage.getItem("happy")
                                  // var sad = sessionStorage.getItem("sad")
                                  // console.log("happyyy " + happy)
                                  // console.log("sad " + sad)
                                  // console.log("neutral " + neutral)
                                    var z = value;
                                    console.log(z)
                                    // return <option value={z}>{Arr[index]}</option>


                                    return <div class="card text-white bg-info mb-3" >
                                        <div class="card-header">{date1[index]}</div>
                                        <div class="card-body">
                                            <h1 class="card-title">Sender: {sender1[index]}</h1>
                                            <p>{ sessionStorage.getItem("neutral")}</p>
                                            <p class="card-text">{message1[index]}</p>
                                        </div>
                                    </div>
                                })}

                                <form class="Right" onSubmit={this.submitHandler}>

                                    {/* <video id="video" width="720" height="560" autoPlay muted></video> */}
                                    {/* <ScriptTag  src="faceapii.js" />
                                    <ScriptTag src="script.js" /> */}
                                    <input name="neutral5" type="hidden" value={neutral} onChange={this.changeHandler}></input>
                                    <input name="happy5" type="hidden" value={happy} onChange={this.changeHandler}></input>
                                    <input name="sad5" type="hidden" value={sad} onChange={this.changeHandler}></input>
                                    <input name="sender5" type="hidden" value={sender} onChange={this.changeHandler}></input>
                                    <input name="reciver5" type="hidden" value={reciver} onChange={this.changeHandler}></input>
                                    <div class="fixed-bottom">
                                        <div class="input-group mb-3">

                                            <input name="msg" type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2" onChange={this.changeHandler}></input>
                                            <div class="input-group-append">
                                                <Button class="btn btn-outline-secondary" type="submit" id="button-addon2">Send</Button>
                                            </div>
                                        </div>

                                    </div>
                                    <br></br>

                                </form>

                            </div>


                        </div>

                    </h2>



                </div >








            </div>


        )

    }

}

export default ChatHistory