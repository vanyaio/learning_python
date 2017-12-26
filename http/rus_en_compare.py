alpf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alpf = list(alpf)

def count_words(text):
	l = 0
	r = l
	cnt = 0
	now_word = False
	
	while (l < len(text)):
		if now_word:
			if (r == (len(text) - 1)):
				cnt += 1
				break
			else:
				if (text[r] in alpf):
					r += 1
				else:
					cnt += 1
					l = r
					now_word = False
		else:
			if (text[l] in alpf):
				 now_word = True
				 r = l
			else:
				l += 1
	return cnt
	
def count_sents(text):
	cnt = 0
	for i in text:
		if (i == '.'):
			cnt += 1
	return cnt
	
text = input("text? ")
print(count_words(text), count_sents(text))
print('__________________')
text = input("text? ")
print(count_words(text), count_sents(text))
