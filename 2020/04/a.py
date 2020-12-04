import itertools as it

fields = set('byr iyr eyr hgt hcl ecl pid'.split())

valid = 0

for nonempty, lines in it.groupby(open("input"), lambda x: bool(x.strip())):
    if nonempty:
        rec = dict(tuple(chunk.split(':')) for line in lines for chunk in line.split())
        valid += all(field in rec for field in fields)

print(valid)