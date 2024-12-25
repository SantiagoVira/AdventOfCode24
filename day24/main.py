import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
raw_wires, raw_gates = parse_input("./input.txt", Parse.two_lines)
wires = {line.split(": ")[0]: int(line.split(": ")[1])
         for line in raw_wires.splitlines()}


def get_number(letter, wires):
    keys = [k for k in wires.keys() if k.startswith(letter)]
    keys.sort()
    total = 0
    for pow, k in enumerate(keys):
        total += 2 ** pow * wires[k]

    return total


gates = []
gates_seen = set()

gates_q = deque(raw_gates.splitlines())

while gates_q:
    gate = gates_q.popleft()
    split = gate.replace(" OR ", "/").replace(" AND ",
                                              "/").replace(" XOR ", "/").replace(" -> ", "/").split("/")
    if split[0] not in wires and split[0] not in gates_seen or split[1] not in wires and split[1] not in gates_seen:
        gates_q.append(gate)
    else:
        gates.append(gate)
        gates_seen.add(split[2])

equations = {}
out_to_ins = {}


ANDS = []
XORS = []
ORS = []

new_gates = "\n".join(gates)

print(new_gates)

for gate in gates:
    split = gate.replace(" OR ", "/").replace(" AND ",
                                              "/").replace(" XOR ", "/").replace(" -> ", "/").split("/")
    if "XOR" in gate:
        wires[split[2]] = wires[split[0]] ^ wires[split[1]]
        if split[0][0] == "x" and split[1][0] == "y" or split[1][0] == "x" and split[0][0] == "y" and split[0][1:] == split[1][1:]:
            XORS.append((split[2], int(split[0][1:])))
            new_gates = new_gates.replace(split[2], f"XOR{split[0][1:]}")
    elif "AND" in gate:
        wires[split[2]] = wires[split[0]] & wires[split[1]]
        if split[0][0] == "x" and split[1][0] == "y" or split[1][0] == "x" and split[0][0] == "y" and split[0][1:] == split[1][1:]:
            ANDS.append((split[2], int(split[0][1:])))
            new_gates = new_gates.replace(split[2], f"AND{split[0][1:]}")
    else:
        wires[split[2]] = wires[split[0]] | wires[split[1]]
        if split[0][0] == "x" and split[1][0] == "y" or split[1][0] == "x" and split[0][0] == "y":
            ORS.append(gate)

    equations[split[2]] = "(" + " ".join([equations.get(
        split[0], split[0]), gate[4:7].strip(), equations.get(split[1], split[1])]) + ")"
    out_to_ins[split[2]] = (split[0], gate[4:7].strip(), split[1])


# print("\n".join(str(wire) for wire in sorted(ANDS, key=lambda x: x[1])))
print(new_gates)

x_num = get_number("x", wires)
y_num = get_number("y", wires)

goal = bin(x_num + y_num)[2:]
curr = bin(get_number("z", wires))[2:]

for i, c in enumerate(curr):
    z_code = f"z{str(45-i).zfill(2)}"
    if c != goal[i]:
        out_in = out_to_ins[z_code]
        # print(f"{z_code} = {equations[z_code]}\n")
        culprits = []
        print(f"{z_code} = {out_in} ({wires[out_in[0]]}, {wires[out_in[2]]})")

print(len(goal))


# z09 is in the final answer

# Z09, RKF, VCG, Z24, JGB, Z20, rrs, rvc

print(",".join(sorted(
    [l.strip() for l in "Z09, RKF, VCG, Z24, JGB, Z20, rrs, rvc".lower().split(",")])))

'''
# WORKING BACKWARDS FROM EACH WRONG Z WIRE
    # AND
        # 0, 0 -> should be 1
            # investigate both
        # 1, 0 -> should be 1
            # investigate right
        # 0, 1 -> should be 1
            # investigate left
        # 1, 1 -> should be 0
            # investigate left, right, both
    # OR
        # 0, 0 -> should be 1
            # investigate left, right, and both
        # 1, 0 -> should be 0
            # investigate left
        # 0, 1 -> should be 0
            # investigate right
        # 1, 1 -> should be 0
            # investigate both
    # XOR
        # 0, 0 -> should be 1
            # investigate left, right
        # 1, 0 -> should be 0
            # investigate left, right
        # 0, 1 -> should be 0
            # investigate left, right
        # 1, 1 -> should be 1
            # investigate left, right

WORKING BACKWARDS FROM EACH WRONG Z WIRE
    AND
        if a == b
            investigate both
        if a == 1
            investigate right
        if b == 1
            investigate left
    OR
        if a == b
            investigate both
        if a == 0
            investigate right
        if b == 0
            investigate left
    XOR
        investigate left
        investigate right
'''
