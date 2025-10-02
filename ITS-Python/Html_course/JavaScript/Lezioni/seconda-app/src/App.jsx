import { useState } from 'react'
import TodoApp from './Esercizi/todolist/TodoApp'
import MainComponent from './Esercizi/MainContent'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <MainComponent></MainComponent>
    </>
  )
}

export default App
