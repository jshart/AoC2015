
import math

# def calculateFuel(fuel):
#     r=math.floor(fuel/3)
#     f=r-2
#     if(f<0):
#         f=0

#     if (f>0):
#         f=f+calculateFuel(f)
#     return f

# input = [String(x) for x in open("data/input.txt").read().split()]
# #input =[12,14,1969,100756]
# t=0
# for i in input:
#     f=calculateFuel(i)
#     t=t+f
#     print("i="+str(i)+" f="+str(f)+" t="+str(t))

# print("total:"+str(t))


str = open('C:\\Users\\jsh27\\OneDrive\\Documents\\GitHub\\Python\\AoC2015_day1_part1\\data\\input.txt', 'r').read()
#str = open('data\\input.txt', 'r').read()

print(str)

i=0
j=0
for c in str:
    j=j+1
    if c=='(':
        i=i+1
    if c==')':
        i=i-1
    if i==-1:
        print(f'basement at step {j}')
        break
    
print(f'final answer:{i}')