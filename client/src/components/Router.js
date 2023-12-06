import { useState } from 'react'
import { Switch, Route } from "react-router-dom";
import Error from "./Error";
import Login from "./Login";
import Profile from "./Profile";
import Signup from "./SignUp";
import Home from './MenuBar';

function Router() {
  
  return (
    <>
    <Switch>
        <Route path="/profile" exact component={Profile} />
        <Route path="/signup" component={Signup} />
        <Route path="/login" component={Login} />
        <Route path="/" component={Home} />
        {/* <Route path="" component={Error} /> */}
    </Switch>
    </>
  );
}

export default Router;