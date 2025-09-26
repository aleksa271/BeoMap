import React, { useEffect, useState, useRef } from "react";
import { MapContainer, TileLayer, GeoJSON } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const defaultStyle = { fillColor: "lightblue", weight: 1, color: "black", fillOpacity: 0.6 };
const hoverStyle = { fillColor: "orange", weight: 2, color: "black", fillOpacity: 0.8 };
const selectedStyle = { fillColor: "red", weight: 2, color: "black", fillOpacity: 0.8 };

export default function BelgradeMap() {
  const [geoData, setGeoData] = useState(null);
  const [info, setInfo] = useState({});
  const [selected, setSelected] = useState(null);
  
const bounds = [
  [43.6, 19.4], // jugozapad (više dole)
  [45.6, 21.3]  // severoistok (više gore)
];

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/geojson")
      .then(res => res.json())
      .then(data => setGeoData(data));

    fetch("http://127.0.0.1:5000/api/data")
      .then(res => res.json())
      .then(data => setInfo(data));
  }, []);

  const onEachFeature = (feature, layer) => {
    const name = feature.properties.opstina__1; 
    layer.bindPopup(`<b>${name}</b><br/>Temperatura: ${info[name]?.temp ?? "-"}°C<br/>Kvalitet vazduha: ${info[name]?.air ?? "-"}`);

    layer.on({
      mouseover: e => e.target.setStyle(hoverStyle),
      mouseout: e => e.target.setStyle(selected === name ? selectedStyle : defaultStyle),
      click: e => setSelected(name)
    });
  };

  const styleFeature = feature => {
    const name = feature.properties.opstina__1;
    return selected === name ? selectedStyle : defaultStyle;
  };

  return (
    <MapContainer center={[44.8176, 20.4569]} zoom={9} minZoom={9} maxZoom={16} maxBounds={bounds} maxBoundsViscosity={0.4} style={{ height: "90vh", width: "100%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
      {geoData && <GeoJSON data={geoData} style={styleFeature} onEachFeature={onEachFeature} />}
    </MapContainer>
  );
}
