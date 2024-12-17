import sys
sys.path.append("..")
from helpers import *  # noqa

# between 8**15 and 8**16 - 1
# A, B, C = 46337277, 0, 0
# pointer = 0
program = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0]


# def combo(n):
#     if n <= 3:
#         return n
#     if n <= 6:
#         return [A, B, C][n-4]

#     return 0


# def run(A, B, C, program):
#     pointer = 0
#     outs = []

#     while pointer < len(program):
#         opcode, operand = program[pointer], program[pointer+1]

#         match opcode:
#             case 0:
#                 A = A // (2 ** combo(operand))
#             case 1:
#                 B ^= operand
#             case 2:
#                 B = combo(operand) % 8
#             case 3:
#                 if A != 0:
#                     pointer = operand
#             case 4:
#                 B ^= C
#             case 5:
#                 outs.append(combo(operand) % 8)
#             case 6:
#                 B = A // (2 ** combo(operand))
#             case 7:
#                 C = A // (2 ** combo(operand))

#         if opcode != 3 or A == 0:
#             pointer += 2

#     return outs

def get_out(A):
    return A & 0b111 ^ 0b101 ^ (A >> (A & 0b111 ^ 1)) & 0b111


# (current A, idx)
options = deque([(0, 15)])
val = float("inf")

while options:
    a, idx = options.popleft()
    for i in range(8):
        new_a = a * 8 + i
        if get_out(new_a) == program[idx]:
            if idx > 0:
                options.append((new_a, idx - 1))
            elif idx == 0:
                val = min(val, new_a)

print(val)
