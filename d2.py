testi = 'ULL\nRRDDD\nLURDL\nUUUUD'
testa = '1985'


def run(code, part2=False):
    g = []
    g.append([1, 2, 3])
    g.append([4, 5, 6])
    g.append([7, 8, 9])
    x, y = 1, 1
    if part2:
        g = []
        g.append([None, None, 1, None, None])
        g.append([None, 2, 3, 4, None])
        g.append([5, 6, 7, 8, 9])
        g.append([None, 'A', 'B', 'C', None])
        g.append([None, None, 'D', None, None])
        x, y = 2, 0
    realcode = []
    for l in code.split('\n'):
        for c in l:
            nx = x
            ny = y
            if c == 'U':
                nx -= 1
            elif c == 'D':
                nx += 1
            elif c == 'L':
                ny -= 1
            elif c == 'R':
                ny += 1
            if nx >= 0 and ny >= 0:
                try:
                    tc = g[nx][ny]
                    if tc is not None:
                        x = nx
                        y = ny
                except IndexError:
                    pass
        realcode.append(str(g[x][y]))
    return ''.join(realcode)


assert run(testi) == testa
assert run(testi, True) == '5DB3'

p1 = run(open('input/d2.txt').read().strip())
p2 = run(open('input/d2.txt').read().strip(), True)
print('part1', p1)
print('part2', p2)
