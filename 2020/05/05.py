print(max(int(line.translate(str.maketrans('FBLR', '0101')), 2) for line in open('input')))

pred, curr, succ = set(), set(), set()
for line in open('input'):
    num = int(line.translate(str.maketrans('FBLR', '0101')), 2)
    pred.add(num - 1)
    curr.add(num)
    succ.add(num + 1)
print(((pred & succ) - curr).pop())
