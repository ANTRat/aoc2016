from collections import defaultdict

puzzle_input_sample = open('input/d6test.txt').read().strip().split('\n')
puzzle_input = open('input/d6.txt').read().strip().split('\n')


def run(puzzle):
    c = defaultdict(lambda: defaultdict(int))
    for message in puzzle:
        for slot, char in enumerate(message):
            c[slot][char] += 1
    p1 = p2 = ''
    for chars in c.values():
        s = sorted(chars, key=lambda x: chars[x])
        p1 += s[-1]
        p2 += s[0]
    return p1, p2


test = run(puzzle_input_sample)
assert test == ('easter', 'advent')

part1, part2 = run(puzzle_input)
print('part1', part1)
print('part2', part2)
