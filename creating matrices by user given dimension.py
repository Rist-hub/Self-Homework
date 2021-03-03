#For First matrix
m = int(input("enter a no. for m columns of m*n matrix "))
n = int(input("enter a no. for n rows of m*n matrix "))
col_1 = []
a=1
while a<=m:    
    col_1.append(2)
    a=a+1

matrix_1 = []
r=1
while r<=n:
    matrix_1.append(col_1)
    r=r+1
print('matrix 1 = ',matrix_1)


#For second matrix
p = int(input("enter a no. for p columns of m*n matrix "))
q = int(input("enter a no. for q rows of m*n matrix "))
col_2 = []
a=1
while a<=p:    
    col_2.append(2)
    a=a+1

matrix_2 = []
r=1
while r<=q:
    matrix_2.append(col_2)
    r=r+1
print('matrix 2 = ',matrix_2)
