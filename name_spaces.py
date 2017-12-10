def underline():
	print('_________')
	
x = 'ok'
y = 'hey'
def foo():#when calling foo, it creates its own namespace
	x = 10#what x is it? let's find out, start looking from now ns - x isn't created
	print(x)
	print(y)#it's from namespace, that called foo()
	return 2 * x
foo()
print(x)
underline()

#loops and if statements are different from C
#they do NOT create theirs namespaces 
if (x == 'ok'):
	a = 'okok'
	x = x + a
print(a)#created in global ns:( wtf??
underline()


#
kek = True

def f():
	kek = False
	def g():
		global kek#kek of global ns
		kek = True
	g()
	print(kek)
	
def f1():
	kek = False
	def g1():
		nonlocal kek#kek of first found ns, in this case - f1
		kek = True
	g1()
	print(kek)
f()
f1()
