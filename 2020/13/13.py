lines = """939
7,13,x,x,59,x,31,19""".splitlines()
lines = open('input').read().splitlines()

start = int(lines[0])
t = start
buses = [int(x) for x in lines[1].split(',') if x != 'x']
while True:
    candidates = [bus for bus in buses if not (t % bus)]
    if candidates:
        print(candidates[0] * (t - start))
        break
    t += 1


buses = [(int(x), offset) for offset, x in enumerate(lines[1].split(',')) if x != 'x']
res = 0
mult = 1
for bus, offset in buses:
    while (res + offset) % bus:
        res += mult
    mult *= bus
print(res)
