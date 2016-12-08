puzzle_input = open('input/d8.txt').read().strip().split('\n')


def run(puzzle):
    def rotate(l, n):
        return l[-n:] + l[:-n]

    screen = []
    for x in range(6):
        screen.append(list('0' * 50))

    for line in puzzle:
        if line[:4] == 'rect':
            a, b = map(int, line[5:].split('x'))
            for x in range(a):
                for y in range(b):
                    screen[y][x] = '1'
        elif line[:10] == 'rotate row':
            a, b = map(int, line[13:].split(' by '))
            screen[a] = rotate(screen[a], b)
        elif line[:13] == 'rotate column':
            a, b = map(int, line[16:].split(' by '))
            col = []
            for x in range(6):
                col.append(screen[x][a])
            for i, x in enumerate(rotate(col, b)):
                screen[i][a] = x
    part1 = ''.join(map(''.join, screen)).count('1')
    part2 = '\n' + '\n'.join(map(''.join, screen)).replace('0', ' ').replace('1', '#')
    return part1, part2


p1, p2 = run(puzzle_input)
print('part1', p1)
print('part2', p2)
