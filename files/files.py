#rw - clear, a - add to next
f = open("text.txt", "r")

x = f.read(5)
print(x)
print(repr(x))

y = f.read()
print(y)
f.close()



