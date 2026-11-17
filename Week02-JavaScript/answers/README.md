# Week 02 answers

- `index.html`, `bill.js`, `style.css`: Tasks 1 and 2 together. Menu items are stored in an array, the subtotal is calculated from the array, and the selected tip and people count are validated before splitting.
- `todo.html` and `todo.js`: Task 3. A checkbox marks each task complete and a delete button removes it. No browser storage is used, so refreshing clears the list.

## Debugger evidence requested by the worksheet
Open the bill splitter in Chrome, press F12, select Sources and open `bill.js`. Click the line `const subtotal = getSubtotal();` to set a breakpoint. Add two items and press Calculate. The debugger should pause at the breakpoint. Use Step over to move to the next line, then hover over `subtotal` (or add it in the Scope/Watch panel) to inspect its value. Take your own screenshots of (1) the breakpoint, (2) stepping, and (3) the variable value, because they must show your browser and actual execution.
