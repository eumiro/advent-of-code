import re

print(sum((m := re.match(r'^(\d+)\-(\d+) (\w): (\w+)$', line)) and sum(m.group(4)[int(m.group(x)) - 1] == m.group(3) for x in (1, 2)) == 1 for line in open('input')))