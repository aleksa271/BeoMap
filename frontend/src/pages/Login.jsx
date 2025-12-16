import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Login() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

const handleLogin = async (e) => {
    e.preventDefault();

    const res = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });


    if (!res.ok) {
        alert("Pogresan login");
        return;
    }

    const data = await res.json();
    localStorage.setItem("user", JSON.stringify(data));
    navigate("/profile");
};

return (
    <form onSubmit={handleLogin} className="container mt-5" style={{ maxWidth:400 }}>
        <h3>Login</h3>

        <input
            className="form-control mb-2"
            placeholder="Username"
            onChange={e => setUsername(e.target.value)}
        />
        
        <input
            type="password"
            className="form-control mb-2"
            placeholder="Password"
            onChange={e => setPassword(e.target.value)}
        />

        <button className="btn btn-primary w-100">Login</button>
    </form>
);

}