print(sum(len(set(block.replace('\n', ''))) for block in open("input").read().split("\n\n")))

print(sum(len(set.intersection(*[set(line) for line in block.strip().split('\n')])) for block in open("input").read().split("\n\n")))
