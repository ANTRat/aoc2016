import itertools
import re

part1 = 0
part2 = 0


def is_triangle(sides):
    for a in itertools.permutations(sides):
        if a[0] + a[1] <= a[2]:
            return False
    return True


v0, v1, v2 = [], [], []

for line in open('input/d3.txt'):
    l = list(map(int, re.split('\s+', line.strip())))
    if is_triangle(l):
        part1 += 1
    v0.append(l[0])
    v1.append(l[1])
    v2.append(l[2])
    if len(v0) == 3:
        if is_triangle(v0):
            part2 += 1
        if is_triangle(v1):
            part2 += 1
        if is_triangle(v2):
            part2 += 1
        v0, v1, v2 = [], [], []

print('part1', part1)
print('part2', part2)
