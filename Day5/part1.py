
import math


textfile = open(
    'C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\AoC2015\\day5\\data\\input.txt', 'r')
input = textfile.read().split('\n')
# str = open('data\\input.txt', 'r').read()


# ab, cd, pq, or xy,
badList = ['ab', 'cd', 'pq', 'xy']


def check(s):
    varCount = 0
    print("Testing [{}]".format(s))
    for v in "aeiou":
        if v in s:
            varCount += s.count(v)

    if varCount >= 3:
        print("Passed Var count={}".format(varCount))
    else:
        print("Failed Var count={}".format(varCount))
        return False

    for b in badList:
        if b in s:
            print("Failed badlist check {}".format(b))
            return False

    for i, c in enumerate(s):

        if i < len(s)-1:
            if c == s[i+1]:
                print("Passed {} == {}".format(c, s[i+1]))
                return True

    print("Failed no double")
    return False


print(check("ugknbfddgicrmopn"))
print(check("aaa"))
print(check("jchzalrnumimnmhp"))
print(check("haegwjzuvuyypxyu"))
print(check("dvszwmarrgswjxmb"))

total = 0
for i in input:
    if check(i):
        total+=1

print(total)