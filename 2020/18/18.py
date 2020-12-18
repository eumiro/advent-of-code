text = """1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
"""

text = open('input').read()

lines = text.splitlines()

import re


def calc(m):
    a = int(m.group(1))
    b = int(m.group(3))
    return str(a + b if m.group(2) == '+' else a * b)

def p1(line):
    line = f'({line})'
    while not line.isdigit():
        line = re.sub(r'\((\d+)\)', r'\1', line)
        line = re.sub(r'(?<=\()(\d+) ([+*]) (\d+)', calc, line)
    return int(line)


def prod(m):
    res = 1
    for part in m.group(0).split(' * '):
        res *= int(part)
    return str(res)


def p2(line):
    line = f'({line})'
    while not re.fullmatch(r'\d+', line):
        while True:
            new = re.sub(r'\((\d+)\)', r'\1', line)
            new = re.sub(r'(\d+) \+ (\d+)', lambda m: str(int(m.group(1)) + int(m.group(2))), new)
            if line == new:
                break
            line = new
        line = re.sub(r'(?<=\()\d+(?: \* \d+)+?(?=\))', prod, line)
    return int(line)

print(sum(p1(line) for line in lines))
print(sum(p2(line) for line in lines))

