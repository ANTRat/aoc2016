import re
import string
from collections import defaultdict

tests = {}
tests['aaaaa-bbb-z-y-x-123[abxyz]'] = True
tests['a-b-c-d-e-f-g-h-987[abcde]'] = True
tests['not-a-real-room-404[oarel]'] = True
tests['totally-real-room-200[decoy]'] = False


def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = bytes.maketrans(alphabet.encode(), shifted_alphabet.encode())
    return plaintext.translate(table)


def is_real_room(name):
    t = re.search('^([\w-]+)-(\d+)\[(\w+)\]', name)
    if not t:
        return False
    name, sector, checksum = t.groups()
    l = defaultdict(int)
    for a in name:
        if a != '-':
            l[a] += 1
    c = defaultdict(list)
    for a in sorted(l, key=l.get, reverse=True):
        c[l[a]].append(a)
    newcs = ''
    for g in sorted(c, reverse=True):
        for l in sorted(c[g]):
            newcs += l
    if newcs[:5] != checksum:
        return False
    return int(sector)


def run_tests():
    s = 0
    for t, e in tests.items():
        r = is_real_room(t)
        if r:
            s += r
    print(s)


part1 = 0
part2 = 0
goodrooms = []
for line in open('input/d4.txt'):
    r = is_real_room(line.strip())
    if r:
        goodrooms.append(line.strip())
        part1 += r
print('part1', part1)


def decode(name):
    t = re.search('^([\w-]+)-(\d+)', name)
    if not t:
        return False
    name, sector = t.groups()
    dec = caesar(name, int(sector) % 26)
    if dec[:5] == 'north':
        return sector
    else:
        return False


for r in goodrooms:
    t = decode(r)
    if t:
        print('part2', t)
