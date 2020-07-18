import React from 'react';
import Signin from './Signin';
import { BrowserRouter, Route, Router } from 'react-router-dom';
import SignUp from './Signup';
import Home from './Home';
//import CustomNavbar from './CustomNavbar'
import UserProfile from './UserProfile';
import Contacts from './Contacts';
import ChatHistory from './ChatHistory';
import AddContact from './AddContact'
import VideoInput from './views/VideoInput';
import createHistory from 'history/createBrowserHistory';






const App = () => {

    return (
        <div>
            <BrowserRouter>
                <div>
                    <Router history={createHistory({ basename: process.env.PUBLIC_URL })}>
                        <Route path="/" exact component={Home} />
                        <Route path="/ChatHistory" exact component={ChatHistory} />
                        <Route path="/AddContact" exact component={AddContact} />
                        <Route path="/UserProfile" exact component={UserProfile} />
                        <Route path="/Signup" exact component={SignUp} />
                        <Route path="/Signin" exact component={Signin} />
                        <Route path="/Contacts" exact component={Contacts} />
                        <Route path="/camera" exact component={VideoInput} />
                    </Router>
                </div>

            </BrowserRouter>




        </div>
    );

};
export default App;