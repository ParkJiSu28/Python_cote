dist  = input()

y =ord(dist[0]) -ord('a')

x =int(dist[1]) -1

answer = 0

if x+1 >= 0 and x+1<8 and y+2 >= 0 and y+2 < 8:
    answer+=1
if x-1 >= 0 and x-1<8 and y+2 >= 0 and y+2 < 8:
    answer+=1
if x+1 >= 0 and x+1<8 and y-2 >= 0 and y-2 < 8:
    answer +=1
if x-1 >= 0 and x-1<8 and y+2 >= 0 and y+2 < 8:
    answer +=1
if x+2 >= 0 and x+2<8 and y+1 >= 0 and y+1 < 8:
    answer +=1
if x+2 >= 0 and x+2<8 and y-1 >= 0 and y-1 < 8:
    answer +=1
if x-2 >= 0 and x-2<8 and y+1 >= 0 and y+1 < 8:
    answer +=1
if x-2 >= 0 and x-2<8 and y-1 >= 0 and y-1 < 8:
    answer +=1
print(answer)