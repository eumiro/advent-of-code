import itertools as it
import re

valid = 0

for nonempty, lines in it.groupby(open('input'), lambda x: bool(x.strip())):
    if nonempty:
        rec = dict(tuple(chunk.split(':')) for line in lines for chunk in line.split())
        try:
            if (1920 <= int(rec['byr']) <= 2002 and
                2010 <= int(rec['iyr']) <= 2020 and
                2020 <= int(rec['eyr']) <= 2030 and
                ((rec['hgt'][3:] == 'cm' and 150 <= int(rec['hgt'][:3]) <= 193) or (rec['hgt'][2:] == 'in' and 59 <= int(rec['hgt'][:2]) <= 76)) and
                re.match(r'^#[0-9a-f]{6}$', rec['hcl']) and
                rec['ecl'] in 'amb blu brn gry grn hzl oth'.split() and
                rec['pid'].isdigit() and len(rec['pid']) == 9):
                valid += 1
        except (KeyError, ValueError):
            pass
print(valid)
