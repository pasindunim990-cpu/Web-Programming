// Keep the menu items in memory. Refreshing the page clears the list.
const items = [];
const itemName = document.getElementById("itemName");
const itemPrice = document.getElementById("itemPrice");
const itemList = document.getElementById("itemList");
const errors = document.getElementById("errors");

function showItems() {
    itemList.innerHTML = "";
    items.forEach((item, index) => {
        const li = document.createElement("li");
        li.textContent = `${item.name} - LKR ${item.price.toFixed(2)} `;
        const remove = document.createElement("button");
        remove.type = "button";
        remove.textContent = "Remove";
        remove.addEventListener("click", () => {
            items.splice(index, 1);
            showItems();
        });
        li.appendChild(remove);
        itemList.appendChild(li);
    });
    document.getElementById("subtotal").textContent = getSubtotal().toFixed(2);
}

function getSubtotal() {
    return items.reduce((sum, item) => sum + item.price, 0);
}

document.getElementById("addItem").addEventListener("click", () => {
    const name = itemName.value.trim();
    const price = Number(itemPrice.value);
    errors.textContent = "";
    if (!name || !Number.isFinite(price) || price <= 0) {
        errors.textContent = "Enter an item name and a price greater than zero.";
        return;
    }
    items.push({ name: name, price: price });
    itemName.value = "";
    itemPrice.value = "";
    showItems();
});

document.getElementById("calculate").addEventListener("click", () => {
    errors.textContent = "";
    document.getElementById("result").textContent = "";
    const tipRate = Number(document.getElementById("tipRate").value);
    const people = Number(document.getElementById("people").value);
    const problems = [];
    if (items.length === 0) problems.push("Add at least one menu item.");
    if (!Number.isInteger(people) || people < 1) problems.push("Number of people must be a whole number of at least 1.");
    if (![0, 5, 10, 15, 20].includes(tipRate)) problems.push("Choose a valid tip rate.");
    if (problems.length) {
        errors.textContent = problems.join(" ");
        return;
    }
    const subtotal = getSubtotal();
    const tip = subtotal * tipRate / 100;
    const total = subtotal + tip;
    const each = total / people;
    document.getElementById("result").innerHTML =
        `<p>Subtotal: LKR ${subtotal.toFixed(2)}</p>` +
        `<p>Tip (${tipRate}%): LKR ${tip.toFixed(2)}</p>` +
        `<p><strong>Total including tip: LKR ${total.toFixed(2)}</strong></p>` +
        `<p><strong>Each person pays: LKR ${each.toFixed(2)}</strong></p>`;
});
