while (True):
	try:
		x = int(input())
		y = int(input())
		print(x / y)
		break
	except (ZeroDivisionError, TypeError) as Err:
		print('Error: ', end = ' ')
		print(Err)
	except:
		print('Error')
	finally:
		print('i work allways')
		

print('lol')

def greet(name):
	if name[0].isupper():
		return "Hello " + name
	else:
		raise ValueError()

while True:
	try:
		name = input()
		print(greet(name))
		break
	except ValueError:
		print('S bolshoy pishi pes')
		
class my_error(Exception):#any custom exception looks loke that
	pass
	
	
class NonPositiveError(Exception):
	pass
class PositiveList(list):
	def append(self, x):
		if (x > 0):
			list.append(self, x)
		else:
			raise NonPositiveError
			
	


