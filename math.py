import math
def quadratic(a, b, c):
#a = int(input("a="))
#b = int(input("b="))
#c = int(input("c="))
#	if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))) :
#       raise TypeError('bad operand type')
	x1=(-b+math.sqrt(b**2-4*a*c))/2
	x2=(-b-math.sqrt(b**2-4*a*c))/2
#print("x1 = %.1f,x2 = %.1f" % (x1,x2))
	#return x1,x2
	#return ('(%.1f,%.1f)' % (x1,x2))
	return ('%.1f,%.1f' % (x1,x2))
#if __main__ == "main()"
print(quadratic(1,2,1))
