text = '389125467'
text = '326519478'

import itertools as it
from collections import deque

cups = deque(int(x) for x in text)
labels = it.cycle(sorted(cups, reverse=True))
for move in range(100):
    cur = cups.popleft()
    while next(labels) != cur:
        pass
    out = [cups.popleft() for _ in range(3)]
    cups.appendleft(cur)
    new = next(it.dropwhile(lambda x: x in out, labels))
    while new != cups[-1]:
        cups.rotate(-1)
    cups.extend(out)
    while cur != cups[-1]:
        cups.rotate(-1)
while 1 != cups[0]:
    cups.rotate(-1)
cups.popleft()
print(''.join(str(i) for i in cups))

#######################

cups = [int(x) for x in text]
cups.extend(range(10, 1_000_001))
cw = dict(zip(cups, cups[1:]))
cw[cups[-1]] = cups[0]
cur = cups[0]
for move in range(10_000_000):
    out = [cw[cur], cw[cw[cur]], cw[cw[cw[cur]]]]
    cw[cur] = cw[out[-1]]
    dst = cur - 1
    while dst in out or dst == 0:
        if dst == 0:
            dst = max(cw)
        else:
            dst -= 1
    cw[out[-1]] = cw[dst]
    cw[dst] = out[0]
    cur = cw[cur]
print(cw[1] * cw[cw[1]])
