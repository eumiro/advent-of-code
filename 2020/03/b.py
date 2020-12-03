lines = [line.strip() for line in open("input")]
prod = 1
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    prod *= sum(lines[dy * i][(dx * i) % len(lines[0])] == "#" for i in range(len(lines) // dy))
print(prod)