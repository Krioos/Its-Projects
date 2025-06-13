import './App.css';
import Componente1 from './Componente1';
import Cloack from './Componente2';


function App() {
  let nome = "Alessio";
  return (
    <div className="App">
      <h1>Prima app con React {nome}</h1>
      <Componente1>{nome}</Componente1>
      <Cloack timezone="-6" country="USA"></Cloack>
      <Cloack timezone="0" country="Italy"></Cloack>
    </div>
  );
}

export default App;
