def isPrime(num):
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            return 0
    return 1
sum=0
a=3
while(a<2000000):
    if(not a%3==0):
        if(isPrime(a)):
            print(a)
            sum=sum+a
    a=a+2
sum=sum+2
print(sum)