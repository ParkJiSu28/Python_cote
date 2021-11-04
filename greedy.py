n = 1260
count = 0

array = [500,100,50,10]

for coin in array:
    count += n // count
    n %= coin


n,k = map(int,input().split())

result = 0

while True:
    target = (n//k)*k
    result += (n -target)
    n = target
    if n <k:
        break
    result +=1
    n//=k
    
result +=(n-1)

data = input()


result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <=1 or result <=1:
        result += num
    else:
        result *= num