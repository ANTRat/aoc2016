import re

sample1 = "abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn".split("\n")
sample2 = "aba[bab]xyz\nxyx[xyx]xyx\naaa[kek]eke\nzazbz[bzb]cdb".split("\n")
puzzle_input = open('input/d7.txt').read().strip().split('\n')


def check(p):
    for i in range(len(p)):
        a = p[i:i + 2]
        b = p[i + 2:i + 4:][::-1]
        if a == b and len(a) == 2 and a[0] != a[1]:
            return True
    return False


def run(puzzle):
    part1 = 0
    part2 = 0
    for line in puzzle:
        a = re.split('[\[\]]', line)
        good = False
        for i, b in enumerate(a):
            if i % 2 == 0:  # even
                if check(b):
                    good = True
        for i, b in enumerate(a):
            if i % 2 != 0:  # even
                if check(b):
                    good = False
        if good:
            # print('good',a)
            part1 += 1

            # print(a)
    return part1


def check2(p):
    for i in range(len(p)):
        a = p[i:i + 3]
        if len(a) == 3 and a[0] != a[1] and a[0] == a[2]:
            yield a


def run2(puzzle):
    part1 = 0
    part2 = 0
    for line in puzzle:
        a = re.split('[\[\]]', line)
        good = False
        good1 = set()
        good2 = set()
        for i, b in enumerate(a):
            if i % 2 == 0:  # even (outside)
                for z in check2(b):
                    good1.add(z)
        for i, b in enumerate(a):
            if i % 2 != 0:  # even
                for z in check2(b):
                    good2.add(z)
        for g in good2:
            if g[1] + g[0] + g[1] in good1:
                good = True
        if good:
            part1 += 1

            # print(a)
    return part1


t1 = run(sample1)
assert t1 == 2
t2 = run2(sample2)
assert t2 == 3

p1 = run(puzzle_input)
p2 = run2(puzzle_input)
print('part1', p1)
print('part2', p2)
