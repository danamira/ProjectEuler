#Problem23:Non-abundant sums

import math
def get_divisors(num):
    result=[]
    for i in range(2,round(math.sqrt(num)+1)):
        if num%i==0:
            result.append(int(i))
            if not num/i==i:
                result.append(int(num/i))
    return result
def is_abundant(num):
    return sum(get_divisors(num))>num
result=0
list=[]
for t in range(1,15000):
    if(is_abundant(t)):
        list.append(t)
print(list)
for i in range(24,28124):
    m=12
    found=0
    for t in list:
        if(found==0 and i/2+1>t and is_abundant(i-t)):
            found=1
            print('hooorray: ',i,'=',t,'+',i-t)
            print(i)
            result+=i
print('-----------------------------')
print(result)