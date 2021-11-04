a ,m,d, n = map(int,input().split())

result = a

for _ in range(n-1):
    result = (result * m ) +1

print(result)
