import math

#up=2070 down=2003 right=2027 left=2092

# this pattern seens to reliable load a list into data
with open ("data\\input.txt", "r") as myfile:
    data=myfile.read().splitlines()

for str in data: 
    print(str)
    
up=0
down=0
right=0
left=0
for c in str:
    if (c=='^'):
        up+=1
    if (c=='v'):
        down+=1
    if (c=='>'):
        right+=1
    if (c=='<'):
        left+=1
      
print(f'up={up} down={down} right={right} left={left}')
print('exiting...')
#print(mySet)
exit

#print(data)

# i=0
# j=0
# for c in str:
#     j=j+1
#     if c=='(':
#         i=i+1
#     if c==')':
#         i=i-1
#     if i==-1:
#         print(f'basement at step {j}')
#         break
    
# print(f'final answer:{i}')