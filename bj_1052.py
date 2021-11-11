# 1. N개의 물병의 물(1L씩)을 재분배하여 k개를 넘지 않는 비어 있지 않는 물병 만들기
# 같은 양의 물이 들어 있는 물병 두개 고름
# 2. 한개의 물병에 다른 한쪽에 있는 물을 모두 부음
# 3. 반복 -> 비어있는 물병 못마들면 새로운 물병삼(1L)
# ex) 3물병 k =1

n, k = map(int, (input().split()))

result = 0
while True:
    cnt = 0
    tmp = n
    while tmp != 0:
        if tmp % 2 != 0:
            cnt += 1
        tmp = tmp // 2

    if cnt <= k:
        break
    n += 1
    result += 1

print(result)
