def simu_eq(a1,b1,c1,a2,b2,c2):
    if (a1>0 and a2<0):
        y = (a2*c1+(-a1)*c2)/(a2*b1+(-a1)*b2)        
        print("y = ",y)
        x=(c1-b1*y)/a1
        print("x = ",x)
    elif (a1<0 and a2>0):
        y = ((-a2)*c1+a1*c2)/((-a2)*b1+a1*b2)
        print("y = ",y)
        x=(c1-b1*y)/a1
        print("x = ",x)     
    elif (a1<0 and a2<0):
        y = ((-a2)*c1+a1*c2)/((-a2)*b1+a1*b2)
        print("y = ",y)
        x=(c1-b1*y)/a1
        print("x = ",x)
    elif (a1>0 and a2>0):
        y = ((a2)*c1-(a1)*c2)/((a2)*b1-(a1)*b2)
        print("y = ",y)
        x=(c1-b1*y)/a1
        print("x = ",x)
   
print("enter values for eq 1 a1x+b1y=c1")
a1=int(input("enter for a1 :"))
b1=int(input("enter for b1 :"))
c1=int(input("enter for c1 :"))
print("enter values for eq 2 a2x+b2y=c2")
a2=int(input("enter for a2 :"))
b2=int(input("enter for b2 :"))
c2=int(input("enter for c2 :"))
simu_eq(a1,b1,c1,a2,b2,c2)
    
    
