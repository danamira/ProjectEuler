def isPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return 0
    return 1
x=0
i=2
## تابع بررسی اول بودن میتواند بهتر شود ( در حقیقت میشه محاسباتو نصف کرد ، بزرگترین مقسوم علیه هر عدد غیر خودش حداکثر نصفشه)
while(1):
    if(isPrime(i)) :
        x=x+1
    if(x==10001):
        print(i)
        break
    i=i+1
