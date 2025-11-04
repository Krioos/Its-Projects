import React from 'react'

const Persona = ({persona}) => {
    return (
    <div>
      <h2>Dati Anagrafici</h2>
      <p>Nome: {persona.nome}</p>
      <p>Cognome: {persona.cognome}</p>
      <p>Età: {persona.eta}</p>
    </div>
  )
}

export default  Persona
