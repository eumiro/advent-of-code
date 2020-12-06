print(sum(len(set.union       (*[set(line) for line in block.split()])) for block in open("input").read().split("\n\n")))
print(sum(len(set.intersection(*[set(line) for line in block.split()])) for block in open("input").read().split("\n\n")))
