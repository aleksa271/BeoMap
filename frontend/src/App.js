import React from "react";
import "bootstrap/dist/css/bootstrap.min.css"
import BelgradeMap from "./components/BelgradeMap";
import MyNavbar from "./components/Navbar";
import OpstinaCard from "./components/OpstinaCard";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import { BrowserRouter, Routes, Route } from "react-router-dom"
import "./App.css"
function App() {
  return (
    <BrowserRouter>
      <MyNavbar />

      <Routes>
        <Route path="/" element={<BelgradeMap />} />
        <Route path="/login" element={<Login />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;
