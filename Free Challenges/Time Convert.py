# Answer to Time Convert
# https://www.coderbyte.com/information/Time%20Convert


def TimeConvert(num):
    h,m = divmod(num, 60)
    return str(h)+":"+str(m)
    
# keep this function call here  
print TimeConvert(raw_input())
