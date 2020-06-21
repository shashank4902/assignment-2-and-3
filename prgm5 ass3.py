5#find the roots of quadratic equation
a=int(input("enter a value of quadratic equation:"))
b=int(input("enter a value of quadratic equation"))
c=int(input("enter a value of quadratic equation"))
discriminant=(b*b)-(4*a*c)
if (discriminant>0):
	root1=(-b+math.sqrt(discriminant)/(2*a))
	root2=(-b+math.sqrt(discriminant)/(2*a))
	print("two distinct real roots exists: root1=%2f and root2=%2f"%(root1,root2))
elif(discriminant==0):
		root1=root2=-b/(2*a)
    print("two equal and real roots exists: root1=%2f and root2=%2f"%(root1,root2))
elif(discriminant<0):
        	root1=root2=-b/(2*a)
        	imaginary=math.sqrt(-discriminant
        	)/(2*a)
        	print("two distinct complex roots exists: roor1=%2f+%2f and root2 =%2f-%2f"(root1,imaginary,root2,imaginary))