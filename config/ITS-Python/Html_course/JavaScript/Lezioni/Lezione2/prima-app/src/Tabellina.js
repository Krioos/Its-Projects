import React from 'react'

const Tabellina = ({numero}) => {
    const moltiplicatori = Array.from({length: 10}, (_, i) => i +1)
    return (
        <div>
            <h2>Tabellina del numero {numero}</h2>
            {moltiplicatori.map(i =>(
                <p key={i}>
                    {numero} x {i} = {numero * i}
                </p>
            ))}
        </div>
  )
}

export default Tabellina