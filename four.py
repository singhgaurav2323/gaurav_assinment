a=[5,7,9,3,2,1,4,2,6,3,0,9,8]

# element less than 5

for i in range (len(a)):
	if(a[i]<5):
		print(a[i])



# list of element less than 5
b=[]

for i in range (len(a)):
	if(a[i]<5):
		b.append(a[i])

print(b)

#list comprehenssion


new=[a[i] for i in range(len(a)) if (a[i] < 5) ]

print(new)

# check for number in list


item=int(input())
pos=0

for i in range(len(a)):
	if(a[i]==item):
		pos=1

if(pos==1):
	print('match found !!!!!',)
else :
	print('no match found !!!!!')
