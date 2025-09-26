import React from "react";
import logo from "../logo-inverse.svg"
function OpstinaCard({ opstina }) {

  return (
    <div className="card" style={{ width: "18rem", position: "absolute", top: 200, right: 20, zIndex: 1000, borderRadius: "20px"}}>
      <img src={logo} className="card-img-top" alt="Logo" />
      <div className="card-body">
        <h5 className="card-title">Title </h5>
        <p className="card-text">Sadrzaj</p>
      </div>
      <ul className="list-group list-group-flush">
        <li className="list-group-item">Populacija: </li>
        <li className="list-group-item">Povrsina: km²</li>
        <li className="list-group-item">Ostalo...</li>
      </ul>
      <div className="card-body">
        <a href="#" className="card-link">Vise informacija</a>
        <button
  type="button"
  className="btn btn-danger rounded-pill ms-5 btn-outline-red "
  style={{
    "--bs-btn-padding-y": ".25rem",
    "--bs-btn-padding-x": ".5rem",
    "--bs-btn-font-size": ".75rem"
    
  }}
>
  Zatvori
</button>

      </div>
    </div>
  );
}

export default OpstinaCard;
