import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, GeoJSON, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import OpstinaCard from "./OpstinaCard";

const defaultStyle = { fillColor: "lightblue", weight: 1, color: "black", fillOpacity: 0.6 };
const hoverStyle = { fillColor: "orange", weight: 2, color: "black", fillOpacity: 0.8 };
const selectedStyle = { fillColor: "red", weight: 2, color: "black", fillOpacity: 0.8 };

function ZoomToBounds({ bounds }) {
  const map = useMap();
  useEffect(() => {
    if (bounds) {
      map.fitBounds(bounds, { padding: [50, 50] }); 
    }
  }, [bounds, map]);
  return null;
}

export default function BelgradeMap() {
  const [geoData, setGeoData] = useState(null);
  const [info, setInfo] = useState({});
  const [selected, setSelected] = useState(null);
  const [selectedBounds, setSelectedBounds] = useState(null);

  const bounds = [
    [43.6, 19.4],
    [45.6, 21.3]
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

    layer.on({
      mouseover: e => e.target.setStyle(hoverStyle),
      mouseout: e => e.target.setStyle(selected?.name === name ? selectedStyle : defaultStyle),
      click: e => {
        setSelected({ name, ...info[name] });
        setSelectedBounds(layer.getBounds());
      }
    });
  };

  const styleFeature = feature => {
    const name = feature.properties.opstina__1;
    return selected?.name === name ? selectedStyle : defaultStyle;
  };

  const handleCloseCard = () => {
    setSelected(null);
    setSelectedBounds(null);
  };

  return (
    <div style={{ display: "flex", position: "relative" }}>
      <div style={{ flex: 1 }}>
        <MapContainer
          center={[44.8176, 20.4569]}
          zoom={9}
          minZoom={9}
          maxZoom={16}
          maxBounds={bounds}
          maxBoundsViscosity={0.4}
          style={{ height: "90vh", width: "100%" }}
        >
          <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
          {geoData && <GeoJSON data={geoData} style={styleFeature} onEachFeature={onEachFeature} />}
          {selectedBounds && <ZoomToBounds bounds={selectedBounds} />}
        </MapContainer>
      </div>

      {selected && (
        <OpstinaCard 
          opstina={selected} 
          onClose={handleCloseCard} 
        />
      )}
    </div>
  );
}
