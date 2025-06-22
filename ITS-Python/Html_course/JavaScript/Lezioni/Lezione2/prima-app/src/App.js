import './App.css';
import Persona from './Persona';
import Stampanumeri from './Stampanumeri';
import Tabellina from './Tabellina';

function App() {
  let nome = "Alessio";
  const persona = {
    nome: 'Luca',
    cognome: 'Verdi',
    eta: 25
  };
  const numero = 6;  
  return (
    <div className="App">
      <h1>Prima app con React {nome}</h1>
      <Persona persona={persona} />
      <Tabellina numero={numero} />
      <Stampanumeri></Stampanumeri>
    </div>
  );
}

export default App;
