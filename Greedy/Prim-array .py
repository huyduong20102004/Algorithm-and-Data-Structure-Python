input = [
    
    [0,4,7,0,0,0,0,0,6,0],
    [4,0,0,8,9,0,0,0,0,0],
    [7,0,0,6,0,0,0,0,2,0],
    [0,8,6,0,7,3,0,4,0,0],
    [0,9,0,7,0,4,0,0,0,0],
    [0,0,0,3,4,0,1,0,0,0],
    [0,0,0,0,0,1,0,2,0,3],
    [0,0,0,4,0,0,2,0,5,4],
    [6,0,2,0,0,0,0,5,0,0],
    [0,0,0,0,0,0,3,4,0,0]
]
a = []
k = []
phe = []
for i in range(10):
    for j in range(10):
        if input[i][j] not in k:
            k.append(input[i][j])
k = sorted(k)
for f in k:
    if f !=0:
       for i in range(10):
        for j in range(10):
          if input[i][j] ==f: 
            test = True
            for b in phe:
                if i in b and j in b:
                    test = False
                    break
            if test:
                phe1 = None
                phe2 = None
                for l in range(len(phe)):
                   if i in phe[l]:
                      phe1 = l
                   if j in phe[l]:
                      phe2 = l
                if phe1 is not None and phe2 is not None:
                   phe[phe1]=phe[phe1]+phe[phe2]
                   phe.pop(phe2)
                elif  phe2 is  None and phe1 is not None:
                   phe[phe1].append(j)
                elif  phe1 is None and phe2 is not None:
                   phe[phe2].append(i)
                else:
                   phe.append([i,j])
                a.append((i,j,f))
for i in a:
   print(i)
print(phe)               
                 