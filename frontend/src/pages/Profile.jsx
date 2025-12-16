import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile() {
    const navigate = useNavigate();
    const user = JSON.parse(localStorage.getItem("user"));
    const [favorites, setFavorites] = useState([]);

    useEffect(() => {
        if (!user) return;

        fetch(`http://localhost:5000/favorites?userId=${user.userId}`)
        .then(res => res.json())
        .then(setFavorites);
    }, []);

    const handleLogout = () => {
        localStorage.removeItem("user");
        navigate("/login");
    };


    if (!user) return <p>Niste ulogovani</p>;

    return (
        <div className="container mt-4">
            <h3>Profil: {user.name}</h3>

            <button className="btn btn-danger mb-3" onClick={handleLogout}>
                Logout
            </button>

            <h5 className="mt-3">Omiljene opstine</h5>

            {favorites.length === 0 && <p>Nema omiljenih</p>}

            <ul className="list-group">
                {favorites.map(o => (
                    <li key={o} className="list-group-item">{o}</li>
                ))}
            </ul>
        </div>
    );
}