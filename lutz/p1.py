#!/usr/bin/env python3
import os, sys
from subprocess import Popen, PIPE, call

def separ():
	print('___________')

def f1():	
	a = os.popen('pwd').read()
	print(a)
	print('kek')
	#os.system('python3 p1.py')#recusively call this programm
	os.system('python3 helloworld.py')

def f2():
	import subprocess
	subprocess.call('python3 helloworld.py', shell=True)#kinda same

def f3():
	os.chdir('fil')
	print(os.popen('pwd').read())
	os.chdir('..')
	print(os.popen('pwd').read())

def f4():
	print('pwd: ', os.getcwd())
	print('my sys.path: ', sys.path[:6])

def f5():
	print(sys.argv)
	
def f6():
	print('Hello stream world')                     # print sends to sys.stdout
	while True:
		try:
			reply = input('Enter a number>')        # input reads sys.stdin
		except EOFError:
			print('end')
			break                                   # raises an except on eof
		else:                                       # input given as a string
			num = int(reply)
			print("%d squared is %d" % (num, num ** 2))
		
	print('Bye')

def f7():
	a = input()
	print(a)

def f8():
	pipe = os.popen('python3 helloworld.py')
	print(pipe.read())
	
def f9():
	print(0)
	pipe = os.popen('python3 helloworld.py', 'w')
	print(10)
	pipe.write('Kek\n')
	print(11)

def f10():
	pipe = Popen('python3 helloworld.py', shell=True, stdout=PIPE)
	print(pipe.stdout.read())

f10()
	
