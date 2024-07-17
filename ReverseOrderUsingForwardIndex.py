ls = [1,4,5]
tp = [2,3]
ls[1:1] = tp   
for i in range(len(ls)-1,-1,-1):
    print(ls[i], end=',')