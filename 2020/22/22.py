text = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""

# text = open('input').read()

adeck, bdeck = text.split('\n\n')

aa = [int(x) for x in adeck.splitlines()[1:]]
bb = [int(x) for x in bdeck.splitlines()[1:]]

while aa and bb:
    a = aa.pop(0)
    b = bb.pop(0)
    if a > b:
        aa += [a, b]
    else:
        bb += [b, a]
if aa:
    print(sum(i * x for i, x in enumerate(aa[::-1], 1)))
if bb:
    print(sum(i * x for i, x in enumerate(bb[::-1], 1)))

print('===============')


def game(aa, bb):
    seen = set()
    while aa and bb:
        if (tuple(aa), tuple(bb)) in seen:
            return True
        seen.add((tuple(aa), tuple(bb)))

        a = aa.pop(0)
        b = bb.pop(0)
        if a <= len(aa) and b <= len(bb):
            awins = game(aa[:a], bb[:b])
        else:
            awins = a > b
        if awins:
            aa += [a, b]
        else:
            bb += [b, a]
    return bool(aa)


aa = [int(x) for x in adeck.splitlines()[1:]]
bb = [int(x) for x in bdeck.splitlines()[1:]]

awins = game(aa, bb)
if awins:
    print(sum(i * x for i, x in enumerate(aa[::-1], 1)))
else:
    print(sum(i * x for i, x in enumerate(bb[::-1], 1)))
