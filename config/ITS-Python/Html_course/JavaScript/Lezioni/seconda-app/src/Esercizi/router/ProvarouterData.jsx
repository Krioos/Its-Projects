import React from 'react'

const ProvarouterData = () => {
  return (
    <div>ProvarouterData
        <nav>
        <BrowserRouter>
        <nav className="navbar ">
          <Link to="/">Home</Link>
          <Link to="About">About</Link>
          <Link to="Profiles">Profiles</Link>
        </nav>
        <hr></hr>
        <Routes>
          <Route path="/" element={<Home></Home>}></Route>
          <Route path="/about" element={<About></About>}></Route>
          <Route path="/profiles" element={<Profiles></Profiles>}></Route>
        </Routes>
      </BrowserRouter>
            <button classname= 'bin bin-link nav-link'>Home</button>
            <button classname= 'bin bin-link nav-link'>About</button>
            <button classname= 'bin bin-link nav-link'>Profile</button>
        </nav>
    </div>
  )
}

export default ProvarouterData