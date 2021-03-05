import math


def devisors(num):
    result = []
    x = int(math.sqrt(num))
    for i in range(1, x + 1):
        if num % i == 0:
            result.append(i)
            if not i == 1:
                result.append(int(num / i))
    return result


def dsum(num):
    return sum(devisors(num))


result = 0
for x in range(1, 10001):
    y = math.pow(x, 1.17)
    if dsum(dsum(x)) == x:
        if not dsum(x) == x:
            result += x
            print(x)
print('--------------------------')
print(result)
