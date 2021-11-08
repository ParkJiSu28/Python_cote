word = list(map(int,input()))
end = len(word)
mid =len(word)//2

left_sum = 0
right_sum = 0

for x in range(mid):
    left_sum += word[x]

for y in range(mid, end):
    right_sum += word[y]

if left_sum -right_sum != 0:
    print('READY')
else:
    print('LUCKY')
