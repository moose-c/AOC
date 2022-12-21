const fs = require('fs');
const raw_data = fs.readFileSync('input.txt', 'utf-8');
const [raw_schematic, raw_instructions] = raw_data.split('\n\r\n');
const split_schematic = raw_schematic.split('\n');
const split_instructions = raw_instructions.split('\n')

// parse input
function process_schematic(schematic) {
    var piles = {}
    for (var row of schematic){
        for (let i = 0; i < row.length; i++){
            var el = row[i]
            var nb = parseInt(schematic[schematic.length - 1][i])
            if (!Number.isNaN(nb)){
                if (el.charCodeAt(0) > 64 && el.charCodeAt(0) < 91) {
                    if (typeof piles[nb] == 'undefined') {
                        piles[nb] = []
                    }
                    piles[nb].push(el)
                }
            }
        }
    }
    return piles
}
var schematic = process_schematic(split_schematic);

function process_instructions(raw_instructions) {
    var instructions = []
    for (line of raw_instructions) {
        [_, a, _, b, _, c] = line.split(' ')
        instructions.push([parseInt(a), parseInt(b), parseInt(c)])
    }
    return instructions
}
var instructions = process_instructions(split_instructions)

// verplaatsen!
function move_simple(schematic) {
    for (var instruction of instructions) {
        amt = instruction[0]
        from = instruction[1]
        to = instruction[2]
        for (; amt > 0; amt--){
            schematic[to].unshift(schematic[from].shift())
        }
    }
    return schematic
}

//obtaining result
function tops_to_str(schematic){
    var result = ""
    for (let key = 1; key < Object.keys(schematic).length+1; key++){
        result += schematic[key][0]
    }
    return result
}
// simple_new_schematic = move_simple(schematic)
// console.log(tops_to_str(simple_new_schematic))

// different movement
function move_difficult(schematic){
    for (var instruction of instructions) {
        amt = instruction[0]
        from = instruction[1]
        to = instruction[2]
        var temp = []
        for (let i = 0; i < amt; i++) {
            temp.unshift(schematic[from].shift()) // z at front
        }
        for (let i = 0; i < amt; i++) {
            schematic[to].unshift(temp.shift())
        }
    }
    return schematic
}

difft_new_schematic = move_difficult(schematic)
console.log(tops_to_str(difft_new_schematic))


