text = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

text2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

text3 = open('input').read()

lines = iter(text3.splitlines())
cc = {}
for line in lines:
    if not line:
        break
    head, _, tail = line.partition(": ")
    rngs = []
    for part in tail.split(' or '):
        start, _, end = part.partition('-')
        rngs.append((int(start), int(end)))
    cc[head] = rngs

assert next(lines) == 'your ticket:'
your_ticket = [int(x) for x in next(lines).split(',')]

assert not next(lines)
assert next(lines) == 'nearby tickets:'
nearby_tickets = [[int(x) for x in line.split(',')] for line in lines]

error_rate = 0
for nt in nearby_tickets:
    for value in nt:
        for rngs in cc.values():
            if any(start <= value <= end for start, end in rngs):
                break
        else:
            error_rate += value
print(error_rate)

##############

all_cands = [set(cc) for _ in cc]
for nt in nearby_tickets:
    row_cands = [set() for _ in cc]
    for cands, value in zip(row_cands, nt):
        for name, rngs in cc.items():
            if any(start <= value <= end for start, end in rngs):
                cands.add(name)
    if all(row_cands):
        for all_cand, row_cand in zip(all_cands, row_cands):
            all_cand.intersection_update(row_cand)
mapping = {}
while len(mapping) < len(cc):
    mapping = {max(all_cand): pos for pos, all_cand in enumerate(all_cands) if len(all_cand) == 1}
    for all_cand in all_cands:
        if len(all_cand) > 1:
            all_cand.difference_update(mapping)

prod = 1
for name, pos in mapping.items():
    if name.startswith('departure'):
        prod *= your_ticket[pos]
print(prod)
