puzzle_input = open('input/d12.txt').read().strip().split('\n')
sample1 = "cpy 41 a\ninc a\ninc a\ndec a\njnz a 2\ndec a".split('\n')
sample1a = 42


def run(puzzle, part2=False):
    i = 0
    reg = dict(a=0, b=0, c=0, d=0)
    if part2:
        reg['c'] = 1
    while True:
        if i >= len(puzzle):
            break
        c = puzzle[i].split(' ')
        if c[0] == 'cpy':
            if c[1] in reg:
                reg[c[2]] = reg[c[1]]
            else:
                reg[c[2]] = int(c[1])
            i += 1
        elif c[0] == 'inc':
            reg[c[1]] += 1
            i += 1
        elif c[0] == 'dec':
            reg[c[1]] += -1
            i += 1
        elif c[0] == 'jnz':
            if c[1] in reg:
                if reg[c[1]] != 0:
                    i += int(c[2])
                else:
                    i += 1
            else:
                if int(c[1]) != 0:
                    i += int(c[2])
                else:
                    i += 1
        else:
            raise RuntimeError('bad opcode')
    return reg['a']


t = run(sample1)
assert t == sample1a

p1 = run(puzzle_input)
print('part1', p1)
p2 = run(puzzle_input, True)
print('part2', p2)
