def occurence(letter_string):
    c=0
    _list = []
    for i in letter_string:
        if i==letter:
            _list.append(i)
            c=c+1
    if len(_list)>1:
        print("letter",letter,"from the given string {",letter_string,"} occured",c,"times")
    else:
        print("letter",letter,"from the given string {",letter_string,"} occured",c,"time")
    return    
letter_string ='hhjooldlfslfopdjsvvbdfgjhjjfkjvnaiojfkvlfvklkvjf'
letter=str(input("enter a letter to find it's frequency of occurence : "))
call=occurence(letter_string)
