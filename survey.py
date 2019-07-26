#tcs codevita servey question
#a survey of some questions are taken with reference answers in hand
#once a person is surveyed, their answers are matched with reference answers and reference answer are updated with the given answer
#at last after all surveys, latest reference answers are matched with all the answers and winner is announced
from collections import Counter
l=[]
q=int(input("enter no of questions  "))
n=int(input("enter no of members  "))
r=[int(x) for x in input("enter the reference answers  ").split(" ")]
def updateresult(l,r,c,t):
    global n,q
    var=[0,0,0,0]
    opt=[1,2,3,4]
    for i in range(q):
        for j in range(t):
            if l[j][i]==1:
                var[0]=var[0]+1
            elif l[j][i]==2:
                var[1]=var[1]+1
            elif l[j][i]==3:
                var[2]=var[2]+1
            elif l[j][i]==4:
                var[3]=var[3]+1
    if r[i] == 1:
        var[0] = var[0] + 1
    elif r[i] == 2:
        var[1] = var[1] + 1
    elif r[i] == 3:
        var[2] = var[2] + 1
    elif r[i] == 4:
        var[3] = var[3] + 1
    d = Counter(var)
    if d[max(var)] == 1:
        r[i] = opt[var.index(max(var))]
    elif d[max(var)] > 1:
        r[i] = c[i]
    return r
for i in range(n):
    l.append([int(x) for x in input("enter the answers  ").split(" ")])
for i in range(n):
    count=0
    for j in range(q):
        if l[i][j]==r[j]:
            count=count+1
    print(count)
    r=updateresult(l,r,l[i],i)
    print(r)
ct=[]
for i in range(n):
    c=0
    for j in range(q):
        if l[i][j]==r[j]:
            c=c+1
    c=c-1
    ct.append(c)
print(ct.index(max(ct)),max(ct))
