import { useState } from 'react';
import TodoForm from './TodoForm'
import TodoList from './TodoList'

const API_URL ="";
function TodoApp = () => {
  const [tasks, setTasks]= useState([]);
  const [loading, setLoading]= useState(true);
  const [error, setError]= useState(null);
  const fetchTask = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response
    }
  };
  return (
    <div className="container m-4">
      <h1 className="mb-4">TodoApp</h1>
      <TodoForm />
      <TodoList />
    </div>
  )
}

export default TodoApp
