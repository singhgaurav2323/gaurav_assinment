# factorial of number

n=int(input())
seq=[]
fact=1

for i in range(1,n+1):
	fact=fact*i

print('factorial is', fact)
b=str(fact)

for i in range(len(b)):
	seq.append(int(b[i]))

print(seq)

