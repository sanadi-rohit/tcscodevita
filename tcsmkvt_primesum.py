#Consecutive Prime Sum Some prime numbers can be expressed as Sum of other consecutive prime numbers. 
#For example 5 = 2 + 3 17 = 2 + 3 + 5 + 7 41 = 2 + 3 + 5 + 7 + 11 + 13 
#Your task is to find out how many prime numbers which satisfy this property are present in the range 3 to N subject to a constraint that summation should always start with number 2.
#Write code to find out number of prime numbers that satisfy the above mentioned property in a given range. 
#Input Format: First line contains a number N Output Format: Print the total number of all such prime numbers which are less than or equal to N. 
#Constraints: 2<N<=12,000,000,000
l=[]
result=[]
def is_prime(m):
    flag=1
    for k in range(2,m):
        if m%k==0:
            flag=0
            return flag
    return flag
n=int(input("enter the number: "))
for j in range(2,n):
        if is_prime(j):
            l.append(j)
print(l)
for i in l:
    j=0
    s=0
    str=''
    while j<l.index(i):
        s=s+l[j]
        str=str+f'{l[j]}'
        j=j+1
        if s==i:
            result.append(i)
            print(str)
            break
        str=str+'+'
print(result)
