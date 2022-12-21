var fs = require('fs');
var raw_data = fs.readFileSync('input.txt', 'utf-8');
var _a = raw_data.split('\n\r\n'), schematic_raw = _a[0], instruction_raw = _a[1];
var split_schematic = schematic_raw.split('\n');
function find_indexes_of_int(str) {
    var indexes = [];
    for (var i = 0; i < str.length; i++) {
        if (!(Number.isNaN(parseInt(str[i])))) {
            indexes.push(i);
        }
    }
    return indexes;
}
var indexes = find_indexes_of_int(split_schematic[split_schematic.length - 1]);
