# Answer to Simple Symbols
# https://www.coderbyte.com/information/Simple%20Symbols


def SimpleSymbols(str):
    if str[0].isalpha():
        return 'false'
    length = len(str)
    for i in range(1,length):
        isalpha = str[i].isalpha()
        if isalpha:
            if str[i-1] != '+':
                return 'false'
            if length > i+1:
                if str[i+1] != '+':
                    return 'false'
            else:
                return 'false'
    return 'true'
    
# keep this function call here  
print SimpleSymbols(raw_input())
