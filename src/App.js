import React from 'react';
import Signin from './Signin';
import { BrowserRouter, Route } from 'react-router-dom';
import SignUp from './Signup';
import Home from './Home';
//import CustomNavbar from './CustomNavbar'
import UserProfile from './UserProfile';
import Contacts from './Contacts';






const App = () => {

    return (
        <div>
            <BrowserRouter>
                <div>
                  
                    <Route path="/" exact component={Home} />
                    <Route path="/UserProfile" exact component={UserProfile} />
                    <Route path="/Signup" exact component={SignUp} />
                    <Route path="/Signin" exact component={Signin} />
                    <Route path="/Contacts" exact component={Contacts} />
                </div>

            </BrowserRouter>




        </div>
    );

};
export default App;