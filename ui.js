import React, { useState, useEffect } from "react";
import axios from "axios";

function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [newTaskTitle, setNewTaskTitle] = useState("");
  const [error, setError] = useState(null);

  useEffect(() => {
    axios.get("/tasks").then(response => {
      setTasks(response.data);
    });
  }, []);

  function handleCreateTask() {
    axios
      .post("/tasks", { title: newTaskTitle })
      .then(response => {
        setTasks([...tasks, response.data]);
        setNewTaskTitle("");
      })
      .catch(error => {
        setError(error);
      });
  }

  function handleUpdateTask(task) {
    axios
      .put(`/tasks/${task.id}`, { ...task, completed: !task.completed })
      .then(response => {
        setTasks(
          tasks.map(t => (t.id === task.id ? response.data : t))
        );
      })
      .catch(error => {
        setError(error);
      });
  }

  function handleDeleteTask(task) {
    axios
      .delete(`/tasks/${task.id}`)
      .then(() => {
        setTasks(tasks.filter(t => t.id !== task.id));
      })
      .catch(error => {
        setError(error);
      });
  }

  return (
    <div>
      {error && <p>{error.message}</p>}
      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <input
              type="checkbox"
              checked={task.completed}
              onChange={() => handleUpdateTask(task)}
            />
            {task.title}
            <button onClick={() => handleDeleteTask(task)}>Delete</button>
          </li>
        ))}
      </ul>
      <input
        type="text"
        value={newTaskTitle}
        onChange={e => setNewTaskTitle(e.target.value)}
      />
      <button onClick={handleCreateTask}>Create Task</button>
    </div>
  );
}

export default TaskList;
