def rotate(n,d):
    array = []
    m=1
    while m<=n:        
        array.append(m)
        m=m+1
    print("original array = ",array)
    x=[]
    y=[]
    for i in range(0,len(array)):
        if array[i]<=d:
            x.append(array[i])
        elif array[i]>d:
            y.append(array[i])
    arr= [y,x]
    print("rotated array = ",arr)
    return
n = int(input("enter size of the array 'n' : "))
d=int(input("enter the number 'd' that is to be rotated by : "))
rot = rotate(n,d)

