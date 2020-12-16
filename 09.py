def square(num):
    return num*num
c=1
x=1
while(x==1):
    for b in range(1,c):
        for a in range(1,b):
            if(square(a)+square(b)==square(c)):
                print(a,b,c)
                print('-----------------------')
                if(a+b+c==1000):
                    print('Done')
                    print('Answer is :',a*b*c)
                    x=0
                if(c>1000):
                    print('Not found !')
                    x=0
    c=c+1
