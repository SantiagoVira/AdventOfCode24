import math
from collections import Counter, deque, defaultdict
from typing import TypeVar, List, Tuple, Callable
from copy import deepcopy
import itertools
from functools import cache


T = TypeVar('T')


class Parse:
    def chars(string: str) -> List[str]:
        return list(string)

    def chars2d(string: str) -> List[List[str]]:
        return [list(line) for line in string.splitlines()]

    def ints(string: str) -> List[int]:
        return [int(c) for c in string]

    def ints2d(string: str) -> List[List[int]]:
        return [[int(c) for c in line] for line in string.splitlines()]

    def lines(string: str) -> List[str]:
        return string.splitlines()

    def two_lines(string: str) -> List[str]:
        return string.split("\n\n")


def parse_input(path: str, parser: Callable[[str], T] = Parse.chars2d) -> T:
    with open(path) as f:
        return parser(f.read())


def check_list(arr: List[T], i: int, target: T) -> bool:
    return i in range(len(arr)) and arr[i] == target


def check_list2d(mat: List[List[T]], x: int, y: int, target: T) -> bool:
    return y in range(len(mat)) and x in range(len(mat[y])) and mat[y][x] == target


def cardinal_moves_indicies(w: int, h: int, x: int, y: int, include_all: bool = False, factor: int = 1) -> List[Tuple[int, int]]:
    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    final = []
    for m in moves:
        if include_all or (m[0] * factor + x in range(w) and m[1] * factor + y in range(h)):
            final.append((m[0] * factor + x, m[1] * factor + y))

    return final


def diagonal_moves_indices(w: int, h: int, x: int, y: int, include_all: bool = False) -> List[Tuple[int, int]]:
    moves = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
    final = []
    for m in moves:
        if include_all or (m[0] + x in range(w) and m[1] + y in range(h)):
            final.append((m[0] + x, m[1] + y))

    return final


def omni_moves_indicies(w: int, h: int, x: int, y: int, include_all: bool = False) -> List[Tuple[int, int]]:
    final = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if include_all or ((dy != 0 or dx != 0) and x + dx in range(w) and y + dy in range(h)):
                final.append((x + dx, y+dy))

    return final
