dic = {'a' : 1, 'b' : 2}

iterator = iter(dic)

print(next(iterator))
print(next(iterator))

#so every iterator must have next atribute
#and every iterated object must have iter(obj)
#loop for is smth like:
'''
while (True):
	try:
		i = next()
		print(i)
	except StopIteration:
		break
'''

from random import random
class rand_iter:
	def __init__(self, k):
		self.k = k
		self.i = 0
		
	def __next__(self):
		if (self.i < self.k):
			self.i = self.i + 1
			return random()
		else:
			raise StopIteration
			
	def __iter__(self):
		return self
		
for x in rand_iter(10):
	print(x)
print('________________')

#generators, from one yeild to next, when no more yields - throw stopiteration
def rand_gen(k):
	for i in range(k):
		yield random()
gen = rand_gen(3)
for i in gen:
	print(i)
print('________________')



class double_it:
	def __init__(self, lst):
		self.lst = lst
		self.i = 0
		
	def __next__(self):
		if self.i < len(self.lst):
			self.i += 2
			return self.lst[self.i - 2], self.lst[self.i - 1]
		else:
			raise StopIteration
			
class my_list(list):
	def __iter__(self):
		return double_it(self)
		
x1 = my_list([1, 2, 3, 4])
for pair in x1:
	print(pair)
	
	
print('________________')	
def prime_gen():
	k = 2
	yield 2
	k += 1
	while (True):
		flag = True
		for i in range(k):
			if (i == 0) or (i == 1):
				continue
			if k % i == 0:
				flag = False
				break
		if flag:
			yield k
		k += 1
	
x = iter(prime_gen())
print(next(x))
print(next(x))
print(next(x))
print(next(x))

