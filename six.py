#to print binary of decimal numer


print('enter the decimal number')
a=int(input())
b=[]
d=[]
c=0
rem=1
while c!=1:
	rem=a%2
	b.append(int(rem))
	c=a//2
	a=a//2

b.append(1)
b.reverse()
d=" ".join(map(str,b))    #mapping

print(d)

