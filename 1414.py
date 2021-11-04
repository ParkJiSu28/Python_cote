s = input()

first = 0
second = 0

tmp= list(s)
for i in range(len(tmp)):
    if tmp[i] =='c' or tmp[i] =='C':
        first +=1
        if i+1 <len(tmp):
            if tmp[i+1] =='c' or tmp[i+1] == 'C':
                second +=1

print(first)
print(second)