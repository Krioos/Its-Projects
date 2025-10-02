import React, { useState } from "react";


const TodoItem = ({ task, handleDeleteTask, onToggleTask, updateTask }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(task.text);
  const handleSave=()=>{
    if(editText.trim()){
    updateTask(task.id,editText)
    setIsEditing(false)
    }else{
      alert("Non puoi mettere un task vuoto")
    }
  }
  return (
    <li className="list-group-item d-flex justify-content-between">
      {isEditing ? (
        <div>
          <input
            type="text"
            className="form-control d-inline-block"
            value={editText}
            onChange={(e) => setEditText(e.target.value)}
            style={{ width: "300px", marginRight: "3px" }}
            autoFocus
            onBlur={handleSave}
          ></input>
          <button
            onClick={() => setIsEditing(false)}
            className="btn btn-danger"
            style={{ marginTop: "-6px" }}
          >
            X
          </button>
        </div>
      ) : (
        <div>
          <input
            type="checkbox"
            checked={task.completed}
            onChange={() => onToggleTask(task.id, task.completed)}
            className="form-check-input me-2"
          ></input>
          <span
            onDoubleClick={() => setIsEditing(true)}
            style={{ textDecoration: task.completed ? "line-through" : "none" }}
          >
            {task.text}
          </span>
        </div>
      )}


      <button
        className="btn btn-sm btn-danger"
        onClick={() => {
          handleDeleteTask(task.id);
        }}
      >
        Elimna
      </button>
    </li>
  );
};


export default TodoItem;
