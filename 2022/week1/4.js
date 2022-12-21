// parse input
const fs = require('fs')
const raw_data= fs.readFileSync('../media/input.txt', 'utf-8');
const lines = raw_data.split('\r\n')
const parsed_lines = []
for (const line of lines){
    [imp1, imp2] = line.split(',')
    imp1_lst = imp1.split('-').map(function (x) {
        return parseInt(x,10);
    }); 
    imp2_lst = imp2.split('-').map(function (x) {
        return parseInt(x, 10);
    });
    parsed_lines.push([imp1_lst, imp2_lst])
}
console.log(parsed_lines[0])

// create ranges
function create_range(lst){
    [int1, int2] = lst
    var range = []
    for (let index = int1; index < int2+1; index++){
        range.push(index)
    }
    return range
}

var ranges = []
for (const line of parsed_lines){
    ranges.push(line.map(x => create_range(x)))
}

// create overlap
function overlap(ar1, ar2){
    const same = ar1.filter(value => ar2.includes(value))
    return same
}

var overlaps = []
for (buddies of ranges){
    overlaps.push(overlap(buddies[0], buddies[1]))
}
console.log(overlaps[0])

// check if subset

function array_equality(ar1, ar2){
    if (!(ar1.length === ar2.length)){
        return false
    }
    else {
        for (let i = 0; i < ar1.length; i++) {
            if (!(ar1[i] == ar2[i])) {
                return false
            }
        }
    }
    return true
}

console.log(array_equality([1,2,3], [1,2,3]))

var count = 0
for (let index = 0; index < overlaps.length; index++) {
    const overlap = overlaps[index];
    if (array_equality(overlap, ranges[index][0]) || array_equality(overlap, ranges[index][1])){
        count++
    }
}
console.log(count)

var count2 = 0
for (let index = 0; index < overlaps.length; index++) {
    const overlap = overlaps[index];
    if (!(overlap.length == 0)) {
        count2++
    }
}
console.log(count2)
