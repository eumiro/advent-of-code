lines = """F10
N3
F7
R90
F11
""".splitlines()
lines = open('input').read().splitlines()

x, y = 0, 0
az = 90
for line in lines:
    op = line[0]
    val = int(line[1:])
    if op == 'N':
        y -= val
    elif op == 'E':
        x += val
    elif op == 'S':
        y += val
    elif op == 'W':
        x -= val
    elif op == 'F':
        if az == 0:
            y -= val
        elif az == 90:
            x += val
        elif az == 180:
            y += val
        elif az == 270:
            x -= val
    elif op == 'R':
        az = (az + val) % 360
    elif op == 'L':
        az = (az - val) % 360
print(abs(x) + abs(y))

x, y = 0, 0
dx, dy = 10, -1
daz = 90
for line in lines:
    if not line:
        continue
    op = line[0]
    val = int(line[1:])
    if op == 'N':
        dy -= val
    elif op == 'E':
        dx += val
    elif op == 'S':
        dy += val
    elif op == 'W':
        dx -= val
    elif op == 'F':
        x += dx * val
        y += dy * val
    elif op == 'R':
        for _ in range(val // 90):
            dx, dy = -dy, dx
    elif op == 'L':
        for _ in range(val // 90):
            dx, dy = dy, -dx
print(abs(x) + abs(y))
