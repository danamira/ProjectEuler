x=600851475143
t = round(x/2)
result=0
for i in range(1,t) :
	if(not i%3 ==0 and x%i==0):
		print(i)
		result=i
print(result)