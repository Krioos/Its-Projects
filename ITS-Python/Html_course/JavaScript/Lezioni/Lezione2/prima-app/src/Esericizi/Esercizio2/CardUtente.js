import React from 'react'

const CardUtente = (props) => {
  return (
    <div className="card" style={{ width: '18rem' }}>
      <img src={props.imgSrc} className="card-img-top" alt={props.titolo} />
      <div className="card-body">
        <h5 className="card-title">{props.titolo}</h5>
        <p className="card-text">{props.testo}</p>
        <a href={props.link} className="btn btn-primary"> Go somewhere
          {props.linkLabel}
        </a>
      </div>
    </div>
  )
}

export default CardUtente