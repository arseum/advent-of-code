import fs from 'node:fs'
let data = fs.readFileSync('input', 'utf8');
const regexMul = /mul\(\d{1,3},\d{1,3}\)/g;

let total = 0

data = data.split('don\'t()')

let reelData = data[0]
data.slice(1,).forEach(l => {
    // console.log(l.split('do()'))
    console.log(l.length)
    reelData += l.split('do()').slice(1,)
})

const correspondances = reelData.match(regexMul);
correspondances.forEach(s => {
    s = s.slice(4, -1).split(',')
    console.log(s)
    total += s[0] * s[1]
})

console.log(total)