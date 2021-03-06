a=int(input("enter a number to check if it's prime or composite = "))
L=[]
n=1000
i=0
while i<n:
    i=i+1
    L.append(i)
#print(L)
fact=[]
for j in L:
   if a%j==0:
       fact.append(j)
       j=j+1
if len(fact)>2:
    print("composite")
else:
    print("prime")
print("and it's factors are - " ,fact)
