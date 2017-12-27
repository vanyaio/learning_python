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



arr = []
while True:
        ans = int(input("continue? 1/0 "))
        if (ans == 0):
                break;
        text = input("text? ")
        ru_words = count_words(text)
        ru_sents = count_sents(text)
        ru_sighs = len(text)
        print(ru_words, ru_sents, ru_sighs)
        print('__________________')

        
        text = input("text? ")
        en_words = count_words(text)
        en_sents = count_sents(text)
        en_sighs = len(text)
        print(en_words, en_sents, en_sighs)

        arr.append([float(ru_words)/en_words, float(ru_sents)/en_sents, float(ru_sighs)/en_sighs])
        print([float(ru_words)/en_words, float(ru_sents)/en_sents, float(ru_sighs)/en_sighs])
