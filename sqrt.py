#SQUARE ROOT OF A GIVEN NUMBER
def sqrt(num):
	"""This function finds the suare root of a positive number"""
	x = num ** 0.5
	return x
n = int(input('Enter  a positive number whose square root is to be found: '))
sqrt_num = sqrt(n)
print('The square root of given number is %0.2f' %sqrt_num)