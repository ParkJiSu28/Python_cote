galho =input()


open =0
close =0
for _ in range(len(galho)):
    if galho[_] =='(':
        open+=1
    else:
        close+=1


print(open,close)