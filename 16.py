a = str(2 ** 1000)
result = 0
counter = 0
print(a[0:1])
while (counter < len(a)):
    result += int(a[counter:counter + 1])
    counter = counter + 1
print(result)