text = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

text = open('input').read()

head, tail = text.split('\n\n')
rules = {}
for line in head.splitlines():
    key, values = line.split(': ')
    if values.startswith('"'):
        rules[int(key)] = values.strip('"')
    else:
        rules[int(key)] = [[int(x) for x in part.split()] for part in values.split(' | ')]


def build(rules, cur):
    if isinstance(rules[cur], str):
        return rules[cur]
    else:
        return '(' + '|'.join(''.join(build(rules, x) for x in part) for part in rules[cur]) + ')'


pattern = build(rules, 0)
print(pattern)
import re

print(sum(bool(re.fullmatch(pattern, line)) for line in tail.splitlines()))

#################

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

maxlen = max(len(line) for line in tail.splitlines())

def build2(rules, cur, depth):
    if depth:
        if isinstance(rules[cur], str):
            return rules[cur]
        else:
            return '(' + '|'.join(''.join(build2(rules, x, depth-1) for x in part) for part in rules[cur]) + ')'
    else:
        return ''

pattern2 = build2(rules, 0, maxlen)
print(sum(bool(re.fullmatch(pattern2, line)) for line in tail.splitlines()))
