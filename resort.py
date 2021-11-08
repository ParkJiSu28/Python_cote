s = list(input())

c = []
d = []

for x in s:
    if ord(x) >= ord('A'):
        c.append(x)
    else:
        d.append(int(x))

c.sort()

sum =0
for a in d:
    sum +=a
c.append(sum)

for x in c:
    print(x, end='')
