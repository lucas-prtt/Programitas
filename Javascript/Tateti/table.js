function generateEmptyTable(rows, columns){
    const table = document.createElement("table");
    const tableBody = document.createElement("tbody");
    for (i = 0; i<rows; i++){
        const row = document.createElement("tr");
        for(j = 0; j<columns; j++){
            row.appendChild(createCell("\u{00a0}".repeat(5)));
        }
        tableBody.appendChild(row);
    }
    table.appendChild(tableBody);
    document.body.appendChild(table);
    table.setAttribute("border", "3");
    table.style.padding = "2px";
}

function createCell(text){
    const cell = document.createElement("td")
    const cellText = document.createTextNode(text);
    cell.appendChild(cellText);
    cell.style.padding = "6px"
    return cell;    
}
