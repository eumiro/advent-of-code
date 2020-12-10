srcs = sorted(int(x) for x in open('input').read().splitlines())

from collections import Counter

vals = [0] + srcs + [srcs[-1] + 3]
diffs = Counter(b - a for a, b in zip(vals, vals[1:]))
print(diffs[1] * diffs[3])



from functools import lru_cache

@lru_cache(maxsize=len(srcs))
def arrange(cur, srcs):
    if srcs:
        return sum(arrange(srcs[i], srcs[i+1:]) for i in range(3) if i < len(srcs) and srcs[i] <= cur + 3)
    else:
        return 1
print(arrange(0, tuple(srcs)))
