# people left on philaland. need to introduce coins like 1,2,3,4...
# input: enter value of of costliest item on island.
# output: give the value of the minimum of number of coins that will be used to buy the item.
l=[]
n=int(input("enter no of cases  "))
for i in range(n):
    l.append(int(input("enter thw costliest item value  ")))
for i in l:
    j=0
    s=0
    while s<=i:
        s=pow(2,j)
        j=j+1
    print(j-1)
