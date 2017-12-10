class cnt:
	def __init__(self):
		self.counter = 0
	def inc(self):
		self.counter += 1
		
x = cnt()
print(x.counter)#100
x.inc()
print(x.counter)
cnt.inc(x)
print(x.counter)

def create_new_atrib(x):
	x.new = 'keks'
	print(x.counter, x.new)

a = cnt()
create_new_atrib(a)
print(a.new)
#print(x.new)#Error

class myclass:
	f1 = 1337#kinda static in c++, but more compicated, see below
	def inc(self):
		self.f1 += 1
var = myclass()
print(var.f1)
var.inc()
print(var.f1)
var2 = myclass()
var2.inc()
print(var.f1, var2.f1)#'cause f1 is "static", prints the same 2 nums


print('__________')
#complicated example
class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1


a1 = A()
b1 = A()

a1.bar()
a1.foo()

c1 = A()

print(a1.val)
print(b1.val)
print(c1.val)










