s = input()

tmp = list(s)

answer = 0
for i in range(len(tmp)):
    if tmp[i] =='l':
        if i+3 <len(tmp):
            if tmp[i+1] =='o' and tmp[i+2] =='v' and tmp[i+3] =='e':
                answer +=1

print(answer)

