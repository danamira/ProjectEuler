# به چهل حرکت نیاز داریم که از آنها بیست تا به سمت راست و بیست تا به سمت پایین هستند
# کافیست بیست حرکت را در جایگاه های ترتیبی چهل حرکت انتخاب کنیم پس پاسخ ترکیب بیست از چهل است .
from math import factorial

result = factorial(40) / factorial(20) / factorial(20)
result = int(result)
print(result)
