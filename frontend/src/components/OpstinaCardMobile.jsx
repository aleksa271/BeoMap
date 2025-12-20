import React from "react";

export default function OpstinaCardMobile({ opstina, onClose }) {
  if (!opstina) return null;

  return (
    <div className="opstina-card-mobile">
      <div className="header">
        <h6>{opstina.name}</h6>
        <button onClick={onClose}>✕</button>
      </div>
        <a
            href={opstina.url}
            target="_blank"
            rel="noopener noreferrer"
        >
      <img src={opstina.slika} alt={opstina.name} />

      </a>
      <div className="info">
        <div>👥 {opstina.populacija}</div>
        <div>🌡 {opstina.temp}°</div>
      </div>
    </div>
  );
}
