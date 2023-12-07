import { useState } from 'react'
import { Routes, Route } from "react-router-dom";
import Error from "./Error";
import Login from "./Login";
import Profile from "./Profile";
import Signup from "./SignUp";
import Home from './MenuBar';

function Router() {
  
  return (
    <>
    <Routes>
        <Route path="/profile" exact element={<Profile />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Home />} />
        {/* <Route path="" component={Error} /> */}
    </Routes>
    </>
  );
}

export default Router;