const fs = require('fs')
const raw_data = fs.readFileSync('input.txt', 'utf-8')
const [schematic_raw, instruction_raw] = raw_data.split('\n\r\n')
const split_schematic = schematic_raw.split('\n')
function find_indexes_of_int(str: string){
    const indexes: number[] = []
    for (let i = 0; i < str.length; i++) {
        if (!(Number.isNaN(parseInt(str[i])))) {
            indexes.push(i)
        }
    }
    return indexes
}
const indexes: number[] = find_indexes_of_int(split_schematic[split_schematic.length - 1])

