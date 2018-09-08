# to convet into upper case whole input

char =input()

def upper_case(a):
	for i in range (len(a)):
		if(a[i].isupper()):
			print(a[i],end="")
			
		else :
			print(a[i].upper(),end="")


upper_case(char)
print("\r")



