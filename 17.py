def inEnglish(num):
    # This function only returns data for integers less than 1001 ( Due to the problem ) .
    a = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    if num <= 10:
        return a[num - 1]
    b = ['Elveen', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    if (num > 10 and num <= 19):
        return b[(num % 10) - 1]
    c = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    if (num >= 20 and num <= 99):
        if (num % 10 == 0):
            return c[int(num / 10) - 2]
        else:
            return '{}{}'.format(c[int(num / 10) - 2], a[int(num % 10) - 1])
    if (num >= 100 and num <= 999):
        if (num % 100 == 0):
            return '{}{}'.format(a[int(num / 100) - 1], 'Hundred')
        else:
            return '{}{}And{}'.format(a[int(num / 100) - 1], 'Hundred', inEnglish(int(num % 100)))
    if (num == 1000):
        return 'OneThousand'


result = 0
for i in range(1, 1001):
    result += len(inEnglish(i))
print(result)
