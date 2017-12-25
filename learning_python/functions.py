def underline():
	print('_________')
	
def printab(a, b):
	print(a)
	print(b)
	
#printab(a = 10, 20) non-keyword arg after keyword arg
printab(10, b = 20)

lst = [10, 20]
printab(*lst)

arg = {'a' : 10, 'b' : 20}
print(arg)
printab(**arg)

underline()

def print_abc(a, b, *args):
	print(a)
	print(b)
	for arg in args:
		print(arg)

print_abc(10, 20, -10, 234)
 
underline()
 

#kind weird way to change immut in func, dunno how common it is
x = True
def my_not(a):
	 a[0] = not a[0]
	 print(a)
	 a = 'ok'
	 print(a)

x = [x]
my_not(x)
print(x)	





