const fs = require('fs');
var input = fs.readFileSync('AOC/2021/Week1/input.txt', 'utf8');
data = input.split('\r\n');
data = data.map(Number);

////////////////
function Compare(data) {
    var sum = 0;
    for (let i = 1; i < data.length; i++) {
        if (data[i] > data[i-1]){
            sum++;
        }
    }
    return sum;
};
var slidingWindow = [];
for (let i = 2; i < data.length; i++) {
    slidingWindow.push(data[i-2] + data[i-1] + data[i]);
}
sum = Compare(slidingWindow);
console.log(sum);

