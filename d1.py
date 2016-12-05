from collections import defaultdict

tests = {}
tests['R2, L3'] = 5
tests['R2, R2, R2'] = 2
tests['R5, L5, R5, R3'] = 12


def run(path, part2=False):
    p = path.split(', ')
    visited = defaultdict(int)
    x, y, direction = 0, 0, 0
    for s in p:
        turn, num = s[0], int(s[1:])
        if turn == 'R':
            direction = (direction + 1) % 4
        if turn == 'L':
            direction = (direction - 1) % 4
        if direction == 0:
            for a in range(y, y + num):
                visited[(x, a)] += 1
                if visited[(x, a)] >= 2 and part2:
                    return abs(x) + abs(a)
            y += num
        elif direction == 1:
            for a in range(x, x + num):
                visited[(a, y)] += 1
                if visited[(a, y)] >= 2 and part2:
                    return abs(a) + abs(y)
            x += num
        elif direction == 2:
            for a in range(y, y - num, -1):
                visited[(x, a)] += 1
                if visited[(x, a)] >= 2 and part2:
                    return abs(x) + abs(a)
            y -= num
        elif direction == 3:
            for a in range(x, x - num, -1):
                visited[(a, y)] += 1
                if visited[(x, a)] >= 2 and part2:
                    return abs(a) + abs(y)
            x -= num
        else:
            print("PANIC")
    return abs(x) + abs(y)


test = run('R8, R4, R4, R8', True)
assert test == 4

if __name__ == '__main__':
    for test, expected in tests.items():
        answer = run(test)
        # print(test, expected, answer, answer == expected)
        assert answer == expected
    route = open('input/d1.txt').read()
    p1 = run(route)
    p2 = run(route, True)
    print('part1', p1)
    print('part2', p2)
