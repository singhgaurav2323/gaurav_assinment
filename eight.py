''' pattern
	1
	23
	345
	4567
	56789
'''

print('enter the limit of pattern')
a=int(input())
print('the pattern is ',"\r")

for i in range(a) :
	for j in range(i+1):
		i=i+1
		print(i,end="")
		
	print("\r")
