import hashlib

puzzle_input = open('input/d5.txt').read().strip()


def run(door):
    i = 0
    code1 = []
    code2 = [None, None, None, None, None, None, None, None]
    while True:
        s = "{}{}".format(door, i).encode()
        h = hashlib.md5(s).hexdigest()
        if h[:5] == '00000':
            if len(code1) <= 7:
                code1 += h[5]
            if h[5] in '01234567' and code2[int(h[5])] is None:
                code2[int(h[5])] = h[6]
            print(i, h, code1, code2)
        i += 1
        try:
            if len(code1) == len(code2) == 8:
                # noinspection PyTypeChecker
                return ''.join(code1), ''.join(code2)
        except TypeError:
            pass


# assert run('abc') == ('18f47a30', '05ace8e3')

p1, p2 = run(puzzle_input)
print('part1', p1)
print('part2', p2)
