from math import sqrt


def divsors(num):
    divs = []
    o = []
    for i in range(1, round(sqrt(num)) + 1):
        if (num % i == 0):
            divs.append(i)
            o.append(i)
    for t in o:
        divs.append(int(num / t))

    return divs


i = 1
while 1:
    t = int(i * (i + 1) / 2)
    print(t)
    print(len(divsors(t)))
    print('-------------')
    if len(divsors(t)) > 500:
        break
    i = i + 1
