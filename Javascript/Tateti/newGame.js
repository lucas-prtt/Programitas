import {TatetiGame} from "./tateti.js"

function newGame(){
    var game = TatetiGame();
    document.body.appendChild(generateTable(TatetiGame.asMatrix()))
}
