n=int(input("enter a no. for digital conversion = "))
sevenseg='a b c d e f g' 
listsevseg=sevenseg.split()
dict7={0:"a b c d e f", 1:"c d", 2:"b c d f e", 3:"b c g d e", 4:"a g c d", 5:"b a g d e" , 6:"a b f e d g", 7:"b c d",8:"a b c d e f g" , 9:"a b c d e g"}
for i in dict7:
    if i==n:
        print(dict7[i])
        listdic7=dict7[i].split()
        print(listdic7 , "no. of sticks = ", len(listdic7))
a=int(input("press 1 to add sticks , 2 to remove sticks = "))
s=int(input("enter no. of sticks to add/remove = "))
if a==1:
    add= len(listdic7)+s
    print("total no. of sticks now = ",add)
    print("posible combinations are : ")
    for j in dict7:
        if add==len(dict7[j].replace(" ","")):
            print(j," ",dict7[j])
if a==2:
    remove=len(listdic7)-s
    print("total no. of sticks now = ",remove)
    print("possible combinations are : ")
    for j in dict7:
        if remove==len(dict7[j].replace(" ","")):
            print(j," ",dict7[j])
   
                    


'''
Following figure represents the dictionary dict7, letters near each stick represents the segment which are defined as values to keys in dict7. 

                            b
                        _ _ _ _ _
                        
                      |           | 
                      |           |
                 a    |           |   c 
                      |           |
                      |     g     |
                        _ _ _ _ _
                        
                      |           | 
                      |           |
                 f    |           |   d 
                      |           |
                      |           |
                        _ _ _ _ _
                      
                            e        
                            
'''

                      
















                      

                
