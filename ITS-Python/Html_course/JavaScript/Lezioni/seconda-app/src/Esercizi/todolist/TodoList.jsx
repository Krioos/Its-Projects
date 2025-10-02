import React from 'react'
import TodoItem from './TodoItem'


const TodoList = ({tasks,onDeleteTask,onToggleTask,updateTask}) => {
console.log("todolist->",tasks);
  return (
    <ul className="list-group">
        {
            tasks.map((t)=>{
              return(  <TodoItem key={t.id} task={t} handleDeleteTask={onDeleteTask} onToggleTask={onToggleTask} updateTask={updateTask}></TodoItem>)
            })
        }
           
       
    </ul>
  )
}


export default TodoList
