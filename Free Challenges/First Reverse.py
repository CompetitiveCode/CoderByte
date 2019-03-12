#Answer to First Reverse - https://www.coderbyte.com/information/First%20Reverse

def FirstReverse(str):
    string = ""
    for i in str:
        string = i + string
    return string
    
# keep this function call here  
print FirstReverse(raw_input())