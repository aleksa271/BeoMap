import React from "react";
import "bootstrap/dist/css/bootstrap.min.css"
import BelgradeMap from "./components/BelgradeMap";
import MyNavbar from "./components/Navbar";
import OpstinaCard from "./components/OpstinaCard";
import "./App.css"
function App() {
  return (
    <div className="App">
      <MyNavbar />
      <BelgradeMap />
      <OpstinaCard />

    </div>
  );
}

export default App;
