import React from "react";

export default function About() {
    return (
        <div className="container mt-5 about-page">
            <h2 className="mb-4">O projektu</h2>

            <p>
                Ova aplikacija omogucava interaktivni prikaz opstina na teritoriji Beograda. Klikom na opstinu korisnik moze videti osnovne informacije kao i dodati opstinu u listu omiljenih
            </p>

            <h4 className="mt-4">Funkcionalnosti</h4>
            <ul>
                <li>Interaktivna mapa sa opstinama</li>
                <li>Detaljne informacije o svakoj opstini</li>
                <li>Sistem omiljenih opstina</li>
                <li>Responzivan dizajn za mobile uredjaje</li>
            </ul>

            <h4 className="mt-4">Koriscene tehnologije</h4>
            <ul>
                <li>React</li>
                <li>React Leaflet</li>
                <li>Flask</li>
                <li>Bootstrap</li>
            </ul>
        </div>

    );
}