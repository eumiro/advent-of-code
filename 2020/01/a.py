values = {int(line) for line in open("input")}
print(max(a * (2020 - a) for a in values if 2020 - a in values))