import React, { useState } from "react";

function Termostato() {
  const [temp, setTemp] = useState(20);

  const aumenta = () => {
    setTimeout(() => {
      setTemp(current => current + 1);
    }, 2000); // delay di 2 secondi
  };

  const diminuisci = () => {
    setTimeout(() => {
      setTemp(current => current - 1);
    }, 2000); // delay di 2 secondi
  };

  return (
    <div>
      <h1>Temperatura: {temp}°C</h1>
      <button onClick={aumenta}>+</button>
      <button onClick={diminuisci}>-</button>
    </div>
  );
}

export default Termostato;
