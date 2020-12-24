text = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""

text = open('input').read()

from collections import Counter
import re

black = {}
for line in text.splitlines():
    cnt = Counter(re.findall(r'[sn]?[we]', line))
    xw = cnt['w'] - cnt['e']
    nw = cnt['nw'] - cnt['se']
    sw = cnt['sw'] - cnt['ne']
    dx = 2 * xw + nw + sw
    dy = nw - sw
    black[(dx, dy)] = not black.get((dx, dy), False)
print(sum(black.values()))

#################################

# use black from p1

offsets = ((2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
for day in range(100):
    new = {}
    for x in range(min(x for x, y in black) - 2, max(x for x, y in black) + 3):
        for y in range(min(y for x, y in black) - 1, max(y for x, y in black) + 2):
            neighbors = sum(black.get((x + dx, y + dy), False) for dx, dy in offsets)
            if black.get((x, y), False) and (neighbors == 0 or neighbors > 2):
                new[(x, y)] = False
            elif not black.get((x, y), False) and neighbors == 2:
                new[(x, y)] = True
    black.update(new)
    print(day, sum(black.values()))

