lines = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".splitlines()

lines = open('input').read().splitlines()

data = {}
mask = None
for line in lines:
    left, _, right = line.split()
    if left == 'mask':
        mask = right
    else:
        old = data.get(left, 0)
        new = 0
        for i, m in enumerate(mask[::-1]):
            if m == '1':
                new += 2**i
            elif m == 'X':
                new += int(right) & 2**i
        data[left] = new
print(sum(data.values()))




lines = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".splitlines()

lines = open('input').read().splitlines()

import itertools as it

data = {}
mask = None
for line in lines:
    left, _, right = line.split()
    if left == 'mask':
        mask = [None if x == 'X' else int(x) for x in right]
    else:
        wildcard = [int(x) for x in f'{int(left[4:-1]):036b}']
        for mm in it.product(*[[0, 1] if m is None else [m or w] for m, w in zip(mask, wildcard)]):
            address = int(''.join(str(x) for x in mm), 2)
            data[address] = int(right)
print(sum(data.values()))

