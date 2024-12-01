import fs from "fs";

const data = fs.readFileSync("./input.txt", "utf-8").split("\n");

const lefts: number[] = [];
const rights: number[] = [];
const rights_dict = {};

for (const line of data) {
  const data = line.split(" ");
  const l = Number(data[0]);
  const r = Number(data[3]);

  lefts.push(Number(l));
  rights.push(r);
  if (r in rights_dict) {
    rights_dict[r] += 1;
  } else {
    rights_dict[r] = 1;
  }
}

lefts.sort();

let sum = 0;

for (let i = 0; i < lefts.length; i++) {
  sum += Math.abs(lefts[i] - rights[i]);
}

console.log(sum);

let total = 0;

for (let i = 0; i < lefts.length; i++) {
  const l = lefts[i];
  const count =
    rights_dict[l.toString()] !== undefined ? rights_dict[l.toString()] : 0;

  total += l * count;
}

console.log(total);
