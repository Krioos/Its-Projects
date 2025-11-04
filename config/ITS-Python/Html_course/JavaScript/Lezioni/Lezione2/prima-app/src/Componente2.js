import React from 'react'

const Cloack = (props)=>{
    const t = Date.now()+3600*props.timezone*1000
    const data = new Date(t);
    return(
        <h2>In {props.country} sono le {data.toLocaleDateString()+ " " + data.toLocaleTimeString()}</h2>
    );
};

export default Cloack