s = input()
tmp = list(s)
idx = 0
answer = ""

for i in range(len(tmp)):
    if tmp[i] == 't':
        idx =i+1
        answer = answer+str(idx)+' '

print(answer)