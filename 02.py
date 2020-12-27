pre = 1
current = 2
sums = 0
while (current <= 4000000):
    if (current % 2 == 0):
        print(current)
        sums = sums + current
    current = pre + current;
    pre = current - pre
print('--------------------------')
print(sums)
