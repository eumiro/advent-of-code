rels = {}  # {child: {(parent), ...}}
for line in open('input'):
    if 'no other' in line:
        continue
    words = line.split()
    for child_pos in range(5, len(words), 4):
        rels.setdefault(' '.join(words[child_pos:child_pos + 2]), set()).add(' '.join(words[0:2]))

todos = set(rels['shiny gold'])
seen = set(rels['shiny gold'])
while todos:
    candidates = rels.get(todos.pop(), set())
    seen.update(candidates)
    todos.update(candidates)
print(len(seen))

#---+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----8----+----9----+----0


rels = {}  # {parent: {(nb, child), ...}}
for line in open('input'):
    if 'no other' in line:
        continue
    words = line.split()
    for child_pos in range(4, len(words), 4):
        rels.setdefault(' '.join(words[0:2]), set()).add((int(words[child_pos]), ' '.join(words[child_pos+1:child_pos + 3])))

def count_children(parent):
    return sum(nb * count_children(child) for nb, child in rels.get(parent, set())) + 1
print(count_children('shiny gold') - 1)