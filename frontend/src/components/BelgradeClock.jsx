import { useEffect, useState } from "react";

export default function BelgradeClock() {
    const [time, setTime] = useState("");

    useEffect(() => {
        const updateTime = () => {
            const now = new Date();
            const belgradeTime = new Intl.DateTimeFormat("sr-RS", {
                timeZone: "Europe/Belgrade",
                hour: "2-digit",
                minute: "2-digit",
                second: "2-digit"
            }).format(now);

            setTime(belgradeTime);
        };

        updateTime();
        const interval = setInterval(updateTime, 1000);

        return () => clearInterval(interval);
    }, []);

    return (
        <span className="belgrade-clock">
            🕒 {time}
        </span>
    );
}
