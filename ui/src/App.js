import React, { useEffect } from "react";
import Home from "./pages/Home";
import { Route, Routes } from 'react-router-dom';
import Susan from "./pages/Susan"
import About from "./pages/About";
import Router from "./components/router";
import "./style.scss";
import "./App.css";
import { useState } from "react";
import axios from "axios";





function App() {

  const [currentUser, setCurrentUser] = useState({});

  const fetchCurrentUser = event => {

    axios({
      method:'get',
      url:'http://127.0.0.1:8000/api/current-user',
    }).then(response => {
      console.log(response);
    }).catch(err => {
      console.log(err);
    })
  }

  useEffect(() => {
    fetchCurrentUser();
  }, [])

  return (
    <div className=" font-lato bg-dark  min-h-screen flex flex-col">  
      <Router />
    </div>  
);
}


export const backend_url = 'http://127.0.0.1:8000'

export default App;
