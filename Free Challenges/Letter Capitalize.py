# Answer to Letter Capitalize
# https://www.coderbyte.com/information/Letter%20Capitalize


def LetterCapitalize(s):
    l = s.split()
    for i in range(len(l)):
        l[i] = l[i][0].upper() + l[i][1:]
    return ' '.join(l)

print LetterCapitalize(raw_input())
