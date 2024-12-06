import * as _ from "lodash";
import fs from "fs";

const data = fs
  .readFileSync("./input.txt", "utf-8")
  .split("\n")
  .map((line) => [...line.split(""), "\n"]);

let y = -1;
for (let i = 0; i < data.length; i++) {
  if (data[i].includes("^")) {
    y = i;
    break;
  }
}
let x = data[y].indexOf("^");
let dx = 0;
let dy = -1;

let mat: Set<number>[][] = [];
for (let j = 0; j < data.length; j++) {
  mat.push([]);
  for (let i = 0; i < data[0].length; i++) {
    mat[j][i] = new Set<number>([0]);
  }
}
mat[y][x].add(1);
let count = 1;
let count2 = 0;

console.log(
  JSON.stringify(data[data.length - 1]),
  data[data.length - 1].length
);
console.log(x, y, dx, dy, data.length, data[0].length);

while (
  0 <= y + dy &&
  y + dy < data.length &&
  0 <= x + dx &&
  x + dx < data[0].length
) {
  if (count > 4700 && count < 4725) {
    console.log(x, y);
  }
  if (data[y + dy][x + dx] == "#") {
    if (dx == 0) {
      dx = -dy;
      dy = 0;
    } else {
      dy = dx;
      dx = 0;
    }
  }

  x += dx;
  y += dy;

  if (mat[y][x].size == 1) {
    count += 1;
    mat[y][x].add(
      1 +
        [
          [0, -1],
          [1, 0],
          [0, 1],
          [-1, 0],
        ].indexOf([dx, dy])
    );
  }

  //   let newx = x;
  //   let newy = y;
  //   let ndx, ndy;
  //   if (dx == 0) {
  //     ndx = -dy;
  //     ndy = 0;
  //   } else {
  //     ndy = dx;
  //     ndx = 0;
  //   }

  //   let new_mat = _.cloneDeep(mat);

  //   while (
  //     0 <= newy + ndy &&
  //     newy + ndy < data.length &&
  //     0 <= newx + ndx &&
  //     newx + ndx < data[0].length
  //   ) {
  //     if (data[newy + ndy][newx + ndx] == "#") {
  //       if (ndx == 0) {
  //         ndx = -ndy;
  //         ndy = 0;
  //       } else {
  //         ndy = ndx;
  //         ndx = 0;
  //       }
  //     }

  //     newx += ndx;
  //     newy += ndy;

  //     const dir_num =
  //       1 +
  //       [
  //         [0, -1],
  //         [1, 0],
  //         [0, 1],
  //         [-1, 0],
  //       ].indexOf([ndx, ndy]);

  //     new_mat[newy][newx].add(dir_num);

  //     if (new_mat[newy][newx].has(dir_num)) {
  //       count2 += 1;
  //       break;
  //     }
  //   }
}
console.log(count);

console.log(count2);
