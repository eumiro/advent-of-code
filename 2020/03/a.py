lines = [line.strip() for line in open("input")]
print(sum(lines[i][(3 * i) % len(lines[0])] == "#" for i in range(len(lines))))