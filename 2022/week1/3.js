const fs = require('fs')

const raw_input = fs.readFileSync('../media/input.txt', 'utf-8');
const lines = raw_input.split('\n');

function twoHalves(str) {
    const length = str.length
    const firstHalve = str.slice(0, length/2)
    const secondHalve = str.slice(length/2)

    return [firstHalve, secondHalve]
}

function checkUpperCase(str) {
    return /[A-Z]/.test(str);
}

var overlap = []
for (let index = 0; index < lines.length; index++) {
    const line = lines[index];
    var [firstHalve, secondHalve] = twoHalves(line)
    for (let index = 0; index < firstHalve.length; index++) {
        var letterf = firstHalve[index];
        for (let index = 0; index < secondHalve.length; index++) {
            var letters = secondHalve[index];
            if (letterf == letters) {
                overlap.push(letterf);
                break;
            }
        }
        if (letterf == letters) {
            break;
        }
    }
}
console.log(lines.length)

function answer(lijstje) {
var numberarray = []
for (const el of lijstje){
    const char = el.charCodeAt(0)
    if (checkUpperCase(el)) {
        numberarray.push(char-38);
    }
    else {
        numberarray.push(char-96);
    }
}

const sum = numberarray.reduce((partialSum, a) => partialSum + a, 0);
return sum;
}
sum = answer(overlap)
console.log(sum)

// create list with list of 3 lines at each index
const lines3 = []
for (let index = 0; index < lines.length/3; index++) {
    const line1 = lines[index*3];
    const line2 = lines[index*3+1];
    const line3 = lines[index*3+2];
    lines3.push([line1, line2, line3])
}

var second_overlap = []
for (const line of lines3){
    const overlap1 = (line[0].match(new RegExp('[' + line[1] + ']', 'g')) || []).join('');
    const overlap2 = (line[2].match(new RegExp('[' + overlap1 + ']', 'g')) || []).join('');
    second_overlap.push(overlap2)
}

var final_overlap = []
for (const el of second_overlap){
    final_overlap.push(el[0])
}

sum = answer(final_overlap)
console.log(sum)

// 10204 too high