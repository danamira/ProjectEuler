i=1
for x in range(1,21):
    i=i*x
print(i)
def check(num):
    for t in range(1,21):
        if(not num%t==0):
            return 0
    return 1
for l in range(1,20):
    if(check(i/l)):
        i=i/l
    else:
        print(l)
print(i)
//// بررسی شود