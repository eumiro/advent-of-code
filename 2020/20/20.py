lines = open('test').read().splitlines()
lines = open('input').read().splitlines()

import itertools as it
from collections import Counter

all_edges = {}
for nonempty, xlines in it.groupby(lines, bool):
    if nonempty:
        key = int(next(xlines)[5:-1])
        tt = list(xlines)
        edges = [
            min(tt[0], tt[0][::-1]),
            min([t[-1] for t in tt], [t[-1] for t in tt[::-1]]),
            min(tt[-1], tt[-1][::-1]),
            min([t[0] for t in tt], [t[0] for t in tt[::-1]]),
        ]
        for edge in edges:
            all_edges.setdefault(''.join(edge), set()).add(key)
outer = Counter(
    min(keys) for edge, keys in all_edges.items() if len(keys) == 1)
prod = 1
for key, number in outer.items():
    if number == 2:
        prod *= key
print(prod)


################################################


class Tile:
    def __init__(self, key, lines):
        self.key = key
        edge_lists = [
            min(lines[0][:], lines[0][::-1]),
            min([line[-1] for line in lines],
                [line[-1] for line in lines[::-1]]),
            min(lines[-1][:], lines[-1][::-1]),
            min([line[0] for line in lines],
                [line[0] for line in lines[::-1]]),
        ]
        self.edges = [''.join(edge) for edge in edge_lists]
        self.body = [line[1:-1] for line in lines[1:-1]]
        self.neighbors = [0] * 4
        self.step = 0
        self.rotate_flip()

    @classmethod
    def from_lines(cls, lines):
        return cls(int(lines[0][5:-1]), list(lines[1:]))

    def __str__(self):
        return (f"<Tile {self.key} neighboring to "
               f"{sorted(n for n in self.neighbors if n)}>")

    def __lt__(self, other):
        return self.key < other.key

    @property
    def degree(self):
        return sum(bool(neighbor) for neighbor in self.neighbors)

    def rotate_flip(self):
        if self.step % 4:
            self.edges.insert(0, self.edges.pop())
            self.neighbors.insert(0, self.neighbors.pop())
            self.body = [[line[x] for line in self.body[::-1]] for x in
                         range(len(self.body))]
        else:
            self.edges = self.edges[::-1]
            self.neighbors = self.neighbors[::-1]
            self.body = [
                [self.body[x][y] for x in range(len(self.body))]
                for y in range(len(self.body))
            ]
        self.step += 1

    def add_neighbor(self, neighbor):
        for i, edge in enumerate(self.edges):
            if edge in neighbor.edges:
                self.neighbors[i] = neighbor.key


tiles = {0: Tile(0, ['.' * 12 for _ in range(12)])}
for nonempty, xlines in it.groupby(lines, bool):
    if nonempty:
        tile = Tile.from_lines(list(xlines))
        tiles[tile.key] = tile
        for edge in tile.edges:
            all_edges.setdefault(edge, set()).add(tile.key)
for keys in all_edges.values():
    if len(keys) == 2:
        a, b = tuple(keys)
        tiles[a].add_neighbor(tiles[b])
        tiles[b].add_neighbor(tiles[a])

size = int((len(tiles) - 1) ** 0.5) + 2
grid = [[None] * size for _ in range(size)]
for i in range(len(grid)):
    for index in (0, -1):
        grid[index][i] = grid[i][index] = tiles[0]
first = next(tile for tile in tiles.values() if tile.degree == 2)
while not (first.neighbors[1] and first.neighbors[2]):
    first.rotate_flip()
grid[1][1] = first

seen = {0}

for y, row in enumerate(grid):
    for x, key in enumerate(row):
        if key is None:
            cands = set()
            if grid[y][x - 1].key:
                if grid[y][x - 1].neighbors[1]:
                    cands.add(grid[y][x - 1].neighbors[1])
            if grid[y - 1][x].key:
                if grid[y - 1][x].neighbors[2]:
                    cands.add(grid[y - 1][x].neighbors[2])
            cands -= seen
            key = cands.pop()
            tile = tiles[key]
            while (tile.neighbors[3] != grid[y][x - 1].key or
                   tile.neighbors[0] != grid[y - 1][x].key):
                tile.rotate_flip()
            grid[y][x] = tile
            seen.add(key)
big = [
    [
        char
        for tile in bigrow[1:-1]
        for char in tile.body[y]
    ]
    for bigrow in grid[1:-1]
    for y in range(8)
]

monsterlines = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]
monster = set()
for dy, line in enumerate(monsterlines):
    for dx, char in enumerate(line):
        if char == '#':
            monster.add((dy, dx))
monster_h = max(dy for dy, dx in monster)
monster_w = max(dx for dy, dx in monster)

nb_big = sum(line.count('#') for line in big)

for step in range(1, 9):
    nb_monsters = 0
    for y in range(len(big) - monster_h):
        for x in range(len(big[0]) - monster_w):
            if all(big[y + dy][x + dx] == '#' for dy, dx in monster):
                nb_monsters += 1
    if nb_monsters:
        print(nb_big - nb_monsters * len(monster))
        break
    if step % 4:
        big = [[line[x] for line in big]
               for x in range(len(big[0]))]
    else:
        big = [
            [big[x][y] for x in range(len(big[0]))]
            for y in range(len(big))
        ]
    step += 1
