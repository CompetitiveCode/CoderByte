#Answer to First Factorial - https://www.coderbyte.com/information/First%20Factorial

def FirstFactorial(num):
    if num == 1:
        return 1
    else:
        return FirstFactorial(num-1)*num

# keep this function call here  
print FirstFactorial(raw_input())