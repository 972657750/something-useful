import random
times=0
dict={}
while times < 1000:#这里输入你要生成的随机数个数
    times=times+1
    number=random.randint(0,100)#这里输入你要生成随机数的范围
    if number in dict.keys():
        dict[number]=dict[number]+1
    else:
        dict[number]=1
print(sorted(dict.items(),key=lambda d: d[0]))
   
