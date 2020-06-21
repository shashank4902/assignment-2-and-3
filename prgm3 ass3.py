3#prime or not
num=int(input("enter a number"))
i=2
count=0
while i<=num :
	if num%i==0 :
		count+=1
		if count==2 :
			print("this number is not prime number")
			break
			i+=1
			if count<=1 :
				print("this is prime number")