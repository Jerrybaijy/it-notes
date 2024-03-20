document.addEventListener('DOMContentLoaded', function () {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');

    taskInput.addEventListener('keyup', function (event) {
        if (event.key === 'Enter') {
            addTask(taskInput.value);
            taskInput.value = '';
        }
    });

    function addTask(taskText) {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${taskText}</span>
            <button onclick="toggleTask(this)">Done</button>
            <button onclick="deleteTask(this)">Delete</button>
        `;
        taskList.appendChild(li);
    }

    window.toggleTask = function (button) {
        const task = button.parentElement;
        task.classList.toggle('completed');
    };

    window.deleteTask = function (button) {
        const task = button.parentElement;
        task.remove();
    };

    // Load tasks from local storage
    const storedTasks = JSON.parse(localStorage.getItem('tasks')) || [];
    storedTasks.forEach(taskText => addTask(taskText));
});

// Save tasks to local storage
window.addEventListener('beforeunload', function () {
    const tasks = Array.from(document.querySelectorAll('#taskList li span')).map(span => span.textContent);
    localStorage.setItem('tasks', JSON.stringify(tasks));
});
