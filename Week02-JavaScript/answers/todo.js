const taskInput = document.getElementById("taskInput");
const tasks = document.getElementById("tasks");
document.getElementById("addTask").addEventListener("click", () => {
    const value = taskInput.value.trim();
    document.getElementById("todoError").textContent = "";
    if (!value) {
        document.getElementById("todoError").textContent = "Please enter a task first.";
        return;
    }
    const li = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.addEventListener("change", () => li.classList.toggle("completed", checkbox.checked));
    const label = document.createElement("span");
    label.textContent = value;
    const remove = document.createElement("button");
    remove.type = "button";
    remove.textContent = "Delete";
    remove.addEventListener("click", () => li.remove());
    li.append(checkbox, label, remove);
    tasks.appendChild(li);
    taskInput.value = "";
    taskInput.focus();
});
taskInput.addEventListener("keydown", event => {
    if (event.key === "Enter") document.getElementById("addTask").click();
});
