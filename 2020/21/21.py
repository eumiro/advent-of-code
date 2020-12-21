text = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

text = open('input').read()

from collections import Counter

ais = {}
cands = Counter()
for line in text.splitlines():
    head, _, tail = line.rstrip(')').partition(' (contains ')
    ings = head.split()
    algs = tail.split(', ')
    for alg in algs:
        ais.setdefault(alg, []).append(set(ings))
    cands.update(ings)

ias = {}
while ais:
    for alg, ing_sets in list(ais.items()):
        pop_ings = set()
        commons = set.intersection(*ing_sets)
        if len(commons) == 1:
            common = commons.pop()
            cands[common] = 0
            pop_ings.add(common)
            ais.pop(alg)
            ias[common] = alg
            for x_alg, x_ing_sets in list(ais.items()):
                for x_ing_set in x_ing_sets:
                    x_ing_set -= pop_ings

print(sum(cands.values()))
print(','.join(sorted(ias, key=ias.get)))
