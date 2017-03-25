a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b:"))
r0 = (a**2+b**2)**0.5
print("The radius of the first circle is r0= %0.2f" %r0)

c = int(input("Enter the value of c:"))
d= int(input("Enter the value of d:"))  
r1 = (c**2+d**2)**0.5
print("The radius of the second circle is r1= %0.2f" %r1)

D = ((c-a)**2 + (d-b)**2)**0.5
print (D)
if(abs(r0-r1) < D< r0+r1):
	print("circles intersect")
else:
	print("circles do not intersect")