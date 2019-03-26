#Answer to Longest Word - https://www.coderbyte.com/information/Longest%20Word

def LongestWord(sen): 
    res = 0
    rest = ""
    specialwords = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','/',';',':',',','<','>','.','?']
    for i in specialwords:
        sen = sen.replace(i," ")
    sen = sen.split()
    for i in sen:
        if res < len(i):
            res = len(i)
            rest = i
    return rest
    
print LongestWord(raw_input())