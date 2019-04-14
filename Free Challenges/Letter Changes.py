#Answer to Letter Changes - https://www.coderbyte.com/information/Letter%20Changes

def LetterChanges(string):
    newstr = ""
    vowel = ['a','e','i','o','u']
    for i in string:
        temp = i
        if i.isalpha():
            temp = chr(ord(temp)+1)
        if temp in vowel:
            temp = temp.upper()
        newstr += temp
    # code goes here 
    return newstr
    
# keep this function call here  
print LetterChanges(raw_input())