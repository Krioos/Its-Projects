import React from 'react'
import piatti from './Piatti'

const MenuRistorante = () => {
  return (
    <div>
        <h1> Menù del ristorante</h1>
        <ul>
            {piatti.map((piatto) =>(
                <li key={piatto.id}>
                    {piatto.nome} - {piatto.prezzo}$
                </li>
            ))}
        </ul>
    </div>
  );
}

export default MenuRistorante;