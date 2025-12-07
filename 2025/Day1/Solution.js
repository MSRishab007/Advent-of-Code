const fs = require('fs');
const path = "2025/Day1/input.txt"; // Path to your input file

let answer1 = 0;
let answer2 = 0;
let current = 50;

try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split(/\r?\n/);

    for (const line of lines) {

        const direction = line[0];
        let value = parseInt(line.slice(1), 10);
        answer2 += Math.floor(value / 100);
        value = value % 100;

        if (direction === 'L') {
            if (current !== 0 && (current - value) <= 0) {
                answer2 += 1;
            }
            current -= value;
        } else if (direction === 'R') {
            current += value;
            if (current >= 100) {
                answer2 += 1;
            }
        }
        current = current % 100;
        if (current < 0) current += 100;
        if (current === 0) {
            answer1 += 1;
        }
    }

    console.log("First Answer:", answer1);
    console.log("Second Answer:", answer2);

} catch (err) {
    console.error("Error reading file:", err.message);
}
