import React from 'react'

function Stampanumeri() {
    const array = Array.from({length: 11}, (_,i)=> i)
    return(
        <div>
            <h2>Numeri da 0 a 10</h2>
            {array.map((n)=>(
                <p key={n}>{n}</p>
            ))}
        </div>
    )
}
export default Stampanumeri