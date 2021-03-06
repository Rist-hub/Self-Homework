names = 'Tosha Trisha Matt Claudio Larita Despina Morton Marlena Julia Farah Porsche Raguel Shakita Marisa Marva Lida Emerita Andree Donnette Charleen Margrett Eva Philomena Meryl Mellis  Cathi Ehte Lorena Mathild  Georgene Ione Von Fredda Christina Terra Felisa Sandra Jermaine Clement Eric  Rosemary Norma Gala Bridgett Candis'
listname= names.split()
print(listname)
print('*'*80)
fetched_out=[]
letter = str(input("enter a letter : "))
for i in range(0,len(listname)):
    if letter in listname[i][0]:
        fetched_out.append(listname[i])
if len(fetched_out)>1:
    print('names involving letter ',letter,' : ',fetched_out)
elif len(fetched_out)==1:
    print('name involving letter ',letter,' : ',fetched_out)
else:
    print("No name exist with the letter ",letter)
            
            
            

    

