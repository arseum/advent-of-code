import fs from 'node:fs'
const data = fs.readFileSync('input', 'utf8');
const regexMul = /mul\(\d{1,3},\d{1,3}\)/g;

let total = 0

const correspondances = data.match(regexMul);
correspondances.forEach(s => {
    s = s.slice(4, -1).split(',')
    console.log(s)
    total += s[0] * s[1]
})

console.log(total)