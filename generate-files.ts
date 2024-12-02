import fs from "fs";

const start_data = `import fs from "fs";

const data = fs.readFileSync("./input.txt", "utf-8").split("\\n");

`;

// for (let i = 1; i <= 25; i++) {
//   const folder = `day${String(i).padStart(2, "0")}`;
//   fs.mkdir(folder, () => {
//     fs.writeFileSync(`${folder}/index.ts`, start_data);
//     fs.writeFileSync(`${folder}/input.txt`, "");
//   });
// }

for (let i = 1; i <= 25; i++) {
  const folder = `day${String(i).padStart(2, "0")}`;
  fs.writeFileSync(
    `${folder}/main.py`,
    `with open("./input.txt") as f:
    data = f.readlines()`
  );
}
