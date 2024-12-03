import re

with open("./input.txt") as f:
    data = f.read()

pattern = "(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
matches = re.findall(pattern, data)

total = 0
do = True

for m in matches:
    if m[1]:
        do = True
    elif m[2]:
        do = False
    elif do:
        num1, num2 = m[0][4:-1].split(",")
        total += int(num1) * int(num2)

print(total)
