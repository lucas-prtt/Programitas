

function generateTable(matrix){
    columns = columnsAmount(matrix)
    rows = rowsAmount(matrix)
    const table = document.createElement("table");
    const tableBody = document.createElement("tbody");
    for (i = 0; i<rows; i++){
        const row = document.createElement("tr");
        for(j = 0; j<columns; j++){
            row.appendChild(createCell(matrix[i][j]));
        }
        tableBody.appendChild(row);
    }
    table.appendChild(tableBody);
    table.setAttribute("border", "3");
    table.style.padding = "2px";
    return table
}

function createCell(text){
    const cell = document.createElement("td")
    const cellText = document.createTextNode(text);
    cell.appendChild(cellText);
    cell.style.padding = "6px"
    return cell;    
}

function generateEmptyTable(rows, columns){
    var matrix = []
    for (i=0; i<columns; i++){
        matrix.push([])
        for (j=0; j<columns; j++){
            matrix[i].push("\u00a0".repeat(5))
        }
    }
    var table = generateTable(matrix)
    return table
}

function rowsAmount(matrix){
    return matrix.length
}
function columnsAmount(matrix){
    var col = 0
    for (i = 0; i<rowsAmount(matrix); i++){
        col = Math.max(col, matrix[i].length)
    }
    return col
}



