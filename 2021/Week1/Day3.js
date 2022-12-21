const fr = require('fs');
var input = fr.readFileSync('AOC/2021/input.txt', 'utf-8');
var data = input.split('\r\n');
var Array = []
var add;
var gammaRateBin = '';
var epsilonRateBin = '';
// Above simple decleration of variables
function countOnes(data, position) {
    var count = 0;
    var compare = 0;
    for (let i in data) {
        compare = data[i].charAt(position);
        if (compare == 1) {
            count++;
        }
    }  
    return count;
} 

for (let i = 0; i < data[0].length; i++) {
    if (countOnes(data, i) > data.length/2) {
        gammaRateBin += '1';
        epsilonRateBin += '0';
    } else {
        gammaRateBin += '0';
        epsilonRateBin += '1'
    }
}
var gammaRate = parseInt(gammaRateBin, 2);
var epsilonRate = parseInt(epsilonRateBin, 2);
var powerConsumption = gammaRate*epsilonRate;
console.log(powerConsumption);
console.log(data[0].charAt())
// above works as intended
////////////////////////////////////
function newArray(data, position, char) {
    var newArray = [];
    var compare;
    for (let i in data) {
        compare = data[i].charAt(position);
        if (compare == char) {
            newArray.push(data[i]);
        }
    }
    return newArray;
}

var position = 0;
var iterativeDataO2 = data;
var iterativeDataCO2 = data;
while (iterativeDataO2.length > 1) {
    if (countOnes(iterativeDataO2, position) >= iterativeDataO2.length/2) {
        iterativeDataO2 = newArray(iterativeDataO2, position, '1');
    }   else {
        iterativeDataO2 = newArray(iterativeDataO2, position, '0');
    }
    position++;
}
position = 0;
while (iterativeDataCO2.length > 1) {
    if (countOnes(iterativeDataCO2, position) >= iterativeDataCO2.length/2) {
        iterativeDataCO2 = newArray(iterativeDataCO2, position, '0');
    }   else {
        iterativeDataCO2 = newArray(iterativeDataCO2, position, '1');
    }
    position++;
}
console.log(iterativeDataCO2)
var lifeSupportRate = parseInt(iterativeDataO2[0],2)*parseInt(iterativeDataCO2[0],2);
console.log(lifeSupportRate)