import requests
import json

def set_of_synoms(text, lang):
    api_key = 'dict.1.1.20171217T160347Z.c014fa68efdd5e4a.0bbe21d3d530b534bd6bab22450cc2c9072cca41'
    url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?'
    
    params = {
    'key' : api_key,
    'lang' : lang,
    'text' : text
    }

    ans = set()
    res = requests.get(url, params=params)

    print(text)
    if "syn" in res.json()["def"][0]["tr"][0]:
        for i in res.json()["def"][0]["tr"][0]["syn"]:
            ans.add(i['text'])
    return ans

def map_en_ru(rutxt, entxt):

    list_of_sets = []
    for ru_word in rutxt:
        a = set_of_synoms(ru_word, 'ru-en')
        list_of_sets.append(a)
        
    list_of_lists = []
    for en_word in entxt:
        list_of_lists.append([])
        
        for ru_set in range(len(rutxt)):
            if (en_word in list_of_sets[ru_set]):
                list_of_lists[len(list_of_lists)-1].append(ru_set)
                
    print(list_of_sets)
    for en_word in range(len(entxt)):
        print(entxt[en_word], end = ":\n")
        for ru_word in range(len(list_of_lists[en_word])):
            print(rutxt[ru_word])
        print('_________')

rutxt = 'Да и какое право имел он судить о нем так поспешно и опрометчиво'.split()
entxt = 'And what right had he to criticise him in that hasty and unguarded manner'.split()
print(rutxt, entxt)

rutxt = ['Да', 'и', 'какой', 'право', 'иметь', 'он', 'судить', 'о', 'он', 'так', 'поспешно', 'и', 'опрометчиво']
entxt = ['And', 'what', 'right', 'had', 'he', 'to', 'criticise', 'he', 'in', 'that', 'hasty', 'and', 'unguarded', 'manner']
map_en_ru(rutxt, entxt)

print(set_of_synoms('поспешно', 'ru-ru'))

