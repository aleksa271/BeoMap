import React from "react";
import logo from "../logo-inverse.svg"
function OpstinaCard({ opstina, onClose, closing}) {

  if(!opstina) return null;

  const handleAddFavorite = async () => {
    const user = JSON.parse(localStorage.getItem("user"));

    if (!user) {
      alert("Morate biti ulogovani da biste dodali omiljenu opstinu");
      return;
    }

    try {
      const res = await fetch("http://localhost:5000/favorites", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          userId: user.userId,
          opstina: opstina.name
        })
      });

      if (!res.ok) {
        const error = await res.json();
        alert(`Greska: ${error.error} || "Neuspesno dodavanje favorite"}`);
        return;
      }

      alert("Opstina odata u omiljene ⭐");
    } catch (err) {
      console.error(err);
      alert("Greska pri povezivanju sa serverom");
    }
  };
    
  return (
    <div className={`card opstina-card ${closing ? "closing" : ""}`}>
      <img src={opstina.slika} className="card-img-top" alt={opstina.name} />
      <div className="card-body">
        <h5 className="card-title">{opstina.name}</h5>
      </div>
      <ul className="list-group list-group-flush">
        <li className="list-group-item">Populacija: {opstina.populacija} </li>
        <li className="list-group-item">Povrsina: {opstina.povrsina} ha</li>
        <li className="list-group-item">Temp: {opstina.temp}  Vazduh: {opstina.air}</li>
      </ul>
      <div className="card-body">
        <a href={opstina.url} className="card-link" target="_blank" rel="noopener noreferrer">Vise informacija</a>
        <button
          className="btn btn-sm btn-outline-primary"
          onClick={handleAddFavorite}
        > ⭐</button>
        <button
  type="button"
  className="btn btn-danger rounded-pill ms-5 btn-outline-red "
  style={{
    "--bs-btn-padding-y": ".25rem",
    "--bs-btn-padding-x": ".5rem",
    "--bs-btn-font-size": ".75rem"
    
  }}
  onClick={onClose}
>
  Zatvori
</button>

      </div>
    </div>
  );
}

export default OpstinaCard;
