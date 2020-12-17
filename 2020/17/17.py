text = """.#.
..#
###
"""

text = open('input').read()

import itertools as it

cur = set()
for y, line in enumerate(text.splitlines()):
    for x, char in enumerate(line):
        if char == '#':
            cur.add((x, y, 0))
for step in range(1, 6 + 1):
    xs = {x for x, y, z in cur}
    ys = {y for x, y, z in cur}
    zs = {z for x, y, z in cur}
    new = set()
    for nx, ny, nz in it.product(range(min(xs) - 1, max(xs) + 2),
                                 range(min(ys) - 1, max(ys) + 2),
                                 range(min(zs) - 1, max(zs) + 2)):
        neighbors = 0
        for dx, dy, dz in it.product((-1, 0, 1), repeat=3):
            if not dx == dy == dz == 0 and (nx + dx, ny + dy, nz + dz) in cur:
                neighbors += 1
        if ((nx, ny, nz) in cur and neighbors in (2, 3)) or ((nx, ny, nz) not in cur and neighbors == 3):
            new.add((nx, ny, nz))
    cur = new
print(len(cur))

########################

cur = set()
for y, line in enumerate(text.splitlines()):
    for x, char in enumerate(line):
        if char == '#':
            cur.add((x, y, 0, 0))
for step in range(1, 6 + 1):
    xs = {x for x, y, z, w in cur}
    ys = {y for x, y, z, w in cur}
    zs = {z for x, y, z, w in cur}
    ws = {w for x, y, z, w in cur}
    new = set()
    for nx, ny, nz, nw in it.product(range(min(xs) - 1, max(xs) + 2),
                                 range(min(ys) - 1, max(ys) + 2),
                                 range(min(zs) - 1, max(zs) + 2),
                                     range(min(ws) - 1, max(ws) + 2)):
        neighbors = 0
        for dx, dy, dz, dw in it.product((-1, 0, 1), repeat=4):
            if not dx == dy == dz == dw == 0 and (nx + dx, ny + dy, nz + dz, nw + dw) in cur:
                neighbors += 1
        if ((nx, ny, nz, nw) in cur and neighbors in (2, 3)) or ((nx, ny, nz, nw) not in cur and neighbors == 3):
            new.add((nx, ny, nz, nw))
    cur = new
print(len(cur))

