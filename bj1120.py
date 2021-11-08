# a,b의 길이를 비교한다
# abc  abcdef 앞뒤로 추가하는 연산은 b와 동일하 것으로 한다고 가정하고
# b문자열에서 a문자열이 최소로 틀리는 숫자를 구한다.
# ex  adaabc
#    aababbc    ->틀린회수 2 여기서 앞에는 a를추가한다고 가정하면 제일 적은 횟수는 2이다.

a, b = input().split()
wrong = 9999
cnt = 0
first = len(a)
second = len(b)
compare = second - first
space = 0
if compare == 0:
    for i in range(first):
        if b[i] != a[i]:
            cnt += 1
    print(cnt)
else:
    for i in range(compare+1):
        for j in range(first):
            if b[j + space] != a[j]:
                cnt += 1
        wrong = min(wrong, cnt)

        space += 1
        cnt = 0
    print(wrong)
