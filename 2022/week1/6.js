const fs = require('fs')
var input  = fs.readFileSync('input.txt', 'utf-8')

// retrieve char at which 4 unique preceding.
function check_if_unique(string) {
    for (let char of string) {
        if (string.split(char).length != 2) {
            return false
        }
    }
    return true
}

function first_occurance(input, marker) {
    for (let i = 0, j = marker; j < input.length; i++, j++) {
        var str = input.substring(i, j)
        if (check_if_unique(str)) {
            console.log(j)
            console.log(str)
            break
        }
    }
    return str
}

console.log(first_occurance(input, 4))
console.log(first_occurance(input, 14))
