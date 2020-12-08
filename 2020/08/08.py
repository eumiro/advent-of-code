def process(lines):
    pos, acc, seen = 0, 0, set()
    while True:
        seen.add(pos)
        ins, val = lines[pos]
        if ins == 'jmp':
            pos += val
        elif ins == 'acc':
            acc += val
            pos += 1
        elif ins == "nop":
            pos += 1
        if pos in seen or pos == len(lines):
            break
    return acc, pos


lines = []
for line in open('input'):
    parts = line.split()
    lines.append((parts[0], int(parts[1])))


print(process(lines)[0])


for i, (ins, val) in enumerate(lines):
    if ins == 'acc':
        continue
    tmp = list(lines)
    if ins == 'jmp':
        tmp[i] = ('nop', val)
    else:
        tmp[i] = ('jmp', val)
    acc, pos = process(tmp)
    if pos == len(lines):
        print(acc)
        break