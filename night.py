wh = input()

w = int(wh[1])
h = ['a','b','c','d','f','g','h']

cnt  = 0

for int_h in h:
    cnt+=1
    if wh[0] == int_h:
        int_h = cnt
        break

steps = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
result =0
for step in steps:
    next_row =w+step[0]
    next_column = int_h+step[1]
    # 해당 위치로 가능한지 판단
    if next_row >=1 and next_column <=8 and next_column >=1 and next_row <=8:
        result+=1

print(result)