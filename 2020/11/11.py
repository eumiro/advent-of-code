lines = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()
lines = [list(line) for line in open('input').read().splitlines()]


def p1(parent):
    neighbors = {}
    h, w = len(parent), len(parent[0])
    for x in range(w):
        for y in range(h):
            if parent[y][x] == 'L':
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if not (dx == dy == 0) and (0 <= x + dx < w) and (0 <= y + dy < h):
                            if parent[y + dy][x + dx] == 'L':
                                neighbors.setdefault((y, x), []).append((y + dy, x + dx))
    parent = [[c.replace('L', '#') for c in line] for line in parent]

    while True:
        change = False
        child = [list(line) for line in parent]
        for x in range(w):
            for y in range(h):
                if parent[y][x] == 'L' and not any(parent[ny][nx] == '#' for ny, nx in neighbors[(y, x)]):
                    child[y][x] = '#'
                    change = True
                elif parent[y][x] == '#' and sum(parent[ny][nx] == '#' for ny, nx in neighbors[(y, x)]) >= 4:
                    child[y][x] = 'L'
                    change = True
        if not change:
            print(sum(line.count('#') for line in child))
            break
        parent = child


def p2(parent):
    neigbbors = {}
    h, w = len(parent), len(parent[0])

    for x in range(w):
        for y in range(h):
            if parent[y][x] == 'L':
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if not dx == dy == 0:
                            for i in range(1, max(w, h)):
                                if not (0 <= x + i * dx < w) or not (0 <= y + i * dy < h):
                                    break
                                if parent[y + i * dy][x + i * dx] == 'L':
                                    neigbbors.setdefault((y, x), []).append((y + i * dy, x + i * dx))
                                    break
    parent = [[c.replace('L', '#') for c in line] for line in parent]

    while True:
        child = [list(line) for line in parent]
        change = False
        for x in range(w):
            for y in range(h):
                if parent[y][x] == 'L' and not any(parent[ny][nx] == '#' for ny, nx in neigbbors[(y, x)]):
                    child[y][x] = '#'
                    change = True
                elif parent[y][x] == '#' and sum(parent[ny][nx] == '#' for ny, nx in neigbbors[(y, x)]) >= 5:
                    child[y][x] = 'L'
                    change = True
        if not change:
            print(sum(line.count('#') for line in child))
            break
        parent = child


p1(lines)
p2(lines)
