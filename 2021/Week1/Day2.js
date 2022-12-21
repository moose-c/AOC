const fs = require('fs');
var input = fs.readFileSync('AOC/2021/Week1/input.txt', 'utf8');
var predata = input.split('\r\n');
var data = [];
predata.forEach(element => {
    add = element.split(' ');
    data.push(add);
}); // data split in array containing arrays: element is ['forward', '2']
////////////////
var forward = 0;
var depth = 0;
for (i = 0; i < predata.length; i++) {
    if (data[i][0] === 'forward') {
        forward += Number(data[i][1]);
    } 
    else if (data[i][0] === 'up') {
        depth -= Number(data[i][1]);
    } 
    else {
        depth += Number(data[i][1]);
    }
} 
console.log(forward*depth);
// 1st exercise is correct
var forward = 0;
var depth = 0;
var aim = 0;
var increase;
for (i = 0; i < predata.length; i++) {
    increase = Number(data[i][1]);
    if (data[i][0] === 'forward') {
        forward += increase;
        depth += aim*increase;
    } 
    else if (data[i][0] === 'up') {
        aim -= increase;
    } 
    else {
        aim += increase;
    }
} 
console.log(forward*depth);