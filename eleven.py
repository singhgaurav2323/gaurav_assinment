# alpha numeric frequenents

print('enter the statements')
a=input()


b=a.split(" ")



num={}
aplha={}
alnu={}


pop=0


for i in range(len(b)):
	pop=b.count(b[i])
	if(b[i].isdigit()):
		num[b[i]]=pop
	elif(b[i].isalpha()):
		aplha[b[i]]=pop
	else :
		alnu[b[i]]=pop


print(num)
print(alnu)
print(aplha)
