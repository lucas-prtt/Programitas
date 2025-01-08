


class TatetiGame {
    constructor() {
        this.gameCells = [];
        
        for (var i = 0; i < 9; i++) { this.gameCells.push(new GameCell()) }
    }
    asMatrix() {
        var matrix = [[], [], []]
        for (var i = 0; i < 3; i++) {
            for (var j = 0; j < 3; j++) {
                matrix[i].push(this.gameCells[i * 3 + j].content.char)
            }
        }
        /*
        [El1, EL2, EL3, EL4, EL5, EL6, EL7, EL8, EL9]
            ==>
        [[El1, El2, El3]
         [El4, El5, El6]
         [El7, El8, El9]]
        */
        return matrix
    }

}

class GameCell {
    constructor() {
        this.content = e
    }
    x(){
        this.content = x
    }
    o(){
        this.content = o
    }
    e(){
        this.content = e
    }
}

const o = {char:"o"} // Circulo 
const x = {char:"x"} // Equis
const e = {char:"\u00a0"} // Vacio




