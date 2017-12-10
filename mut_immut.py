def underline():
	print('_________')
	
#id - identificator for object
x = [1, 2, 3]
print(id(x))
print(id([1,2,3]))
underline()

#is - does two vars refer to the same obj?
x = [1, 2, 3]
y = x
print(y is x) #true
print(y is [1, 2, 3]) #false
underline()


x = [1, 2, 3]
y = x
x.append(4)
print(x)
print(y)
underline()


#mutable: list, dict, set, 
#immutable: numbers, bool,  tuple, string, frozenset
#when creates immutable obj, always create new part in memory
#not always true for immutable, for example false, true has only 2 id 
x = [1, 2, 3]
y = x
y.append(4)
s = "123"
t = s
t = t + "4"
print(str(x) + " " + s)
underline()

x = 10
y = 10
print(id(x) == id(y))
x = []
y = []
print(id(x) == id(y))
underline()

#program that counts different objs in a list
objects = []
ids = set()
for obj in objects:
	ids.add(id(obj))
print(ids)
print(len(ids))
underline()

#funcs
def foo_mut(a):
	a.append(10)
a = [1]
foo_mut(a)
print a


def foo_immut(a):
	a = a + a
a = 10
foo_immut(a)
print(a)
a = 'abc'
foo_immut(a)
print a
a = a + a
print a
	
	










