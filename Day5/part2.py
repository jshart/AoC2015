import math


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2015\\day5\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()


def check(s):
    varCount = 0
    print("Testing [{}]".format(s))

    doubleFound = False
    # check for any pair of characters that repeat in the string
    for i in range(len(s)-1):
        substr = s[i:i+2]
        #print(" \- Testing [{}]".format(substr))
        if substr in s[i+2:] or substr in s[0:i]:
            print(" \- Found [{}] in [{}]".format(substr, s))
            doubleFound = True

    if doubleFound == False:
        print(" \- No doubles found")
        return False

    for i, c in enumerate(s):

        if i < len(s)-2:
            if c == s[i+2]:
                print(" \- Passed {} == {}".format(c, s[i+2]))
                return True

    print(" \- Failed no double split by a char")
    return False


print(check("qjhvhtzxzqqjkmpb"))
print(check("xxyxx"))
print(check("uurcxstgmygtbstg"))
print(check("haegwjzuvuyypxyu"))
print(check("ieodomkazucvgmuy"))

total = 0
for i in input:
    if check(i):
        total+=1
print(total)
