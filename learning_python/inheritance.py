#inheritance
class myList(list):
	def even_len(self):
		return len(self) % 2 == 0




class d: pass
class e: pass
class b(d, e): pass
class c: pass
class a(b, c): pass

print(a.mro())#method resolution order - works pretty strange,diff in py2 in py3,google
#binds earliest found method 

class evenLenMix:
	def even_len1(self):
		return len(self) % 2 == 0
class myList1(list, evenLenMix):
	def pop(self):
		x = super(myList1, self).pop()#~list.pop(self)
		#x = list.pop(self)
		print("Last value is", x)
		return(x) 
x = myList1([1, 2, 3])
print(x.even_len1())
y = x.pop()

print('_______________')
#just another a little bit interesting example

class Base:
    def __init__(self):
        self.val = 0

    def add_one(self):
        self.val += 1

    def add_many(self, x):
        for i in range(x):
            self.add_one()

class Derived(Base):
    def add_one(self):
        self.val += 10


a = Derived()
a.add_one()

b = Derived()
b.add_many(3)

print(a.val)
print(b.val)


#don't look below, mro works really strange
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass
print(E.mro())
