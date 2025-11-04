import './App.css';
import Saluto from './Esericizi/Esercizio1/Saluto';
import CardUtente from './Esericizi/Esercizio2/CardUtente';
import MenuRistorante from './Esericizi/Esercizio3/MenuRistorante';
import Termostato from './Esericizi/Esercizio4/Termostato';
function App() {
  const persona = {
    titolo: "Utente1",
    testo: "testo di prova",
    imgSrc: "https://via.placeholder.com/150/FF0000/FFFFFF"
  }
  return (
    <>
    <Saluto></Saluto>
    <CardUtente {... persona}></CardUtente>
    <CardUtente
    titolo = "Utente2"
    testo = "Testo di prova"
    imgSrc = "https://via.placeholder.com/150/FF0000/FFFFFF">
    </CardUtente>
    <MenuRistorante></MenuRistorante>
    <Termostato></Termostato>
    </>
  )
}
export default App;
