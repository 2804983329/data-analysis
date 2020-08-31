'''
a=6
if(a>7):
    print(a)
elif(a<2):
    print(a)
else:
    print("nnn")
'''
'''
a=0
while a<8:
    print("hello")
'''
'''
a=["a","c","b","d"]
for i in a:
    print(i)
'''
'''
for i in range(0,10):
    print(i)
'''
'''
for i in range(0,8):
    print("hello")
'''
'''
#中断一次循环，使用continue语句，中断一个循环，使用break；
for i in range(0,8):
    if(i==3):
        break
    print(i)
'''

for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j)+"   ",end="")
    print()

    
