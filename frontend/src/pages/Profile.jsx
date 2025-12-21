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
        .then(setFavorites)
        .catch(err => console.error("Fetch error:", err));
    }, [user]);

    const handleLogout = () => {
        localStorage.removeItem("user");
        navigate("/login");
    };

    const handleRemoveFavorite = async (opstina) => {
        try {
            const res = await fetch("http://localhost:5000/favorites", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    userId: user.userId,
                    opstina: opstina
                })
            });

            if (!res.ok) {
                throw new Error("Neuspesno brisanje");
            }

            setFavorites(prev =>
                prev.filter(o => o !== opstina)
            );
        } catch (err) {
            console.error("Delete error:", err);
            alert("Greska pri brisanju favorita")
        }
    }


    if (!user) return <p style={{ textAlign:"center", color:"#D34E4E", fontWeight:"bold"}}>⚠️ Niste ulogovani</p>;

    return (
        <div className="container mt-4" style={{color: "#CE7E5A"}}>
            <h3>Profil: {user.name}</h3>

            <button className="btn btn-danger mb-3" style={{backgroundColor:"#CE7E5A"}}onClick={handleLogout}>
                Logout
            </button>

            <h5 className="mt-3">Omiljene opstine</h5>

            {favorites.length === 0 && <p>Nema omiljenih</p>}

            <ul className="list-group">
                {favorites.map(o => (
                    <li 
                        key={o} 
                        className="list-group-item" style={{backgroundColor: "#F9E7B2"}}
                        >
                    
                        {o}
                        <button
                        className="btn btn-sm btn-outline-danger" style={{backgroundColor: "#CE7E5A", marginLeft: "0.5rem"}}
                        onClick={() => handleRemoveFavorite(o)}
                    >
                            Ukloni
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}