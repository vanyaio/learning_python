import requests
import json

def weather():
	api_url = "http://api.openweathermap.org/data/2.5/weather"
	city = input("city? ")
	params = {
		'q' : city,
		'appid' : '11c0d3dc6093f7442898ee49d2430d20',
		'units' : 'metric'
	}

	res = requests.get(api_url, params=params)
	print(res.headers["Content-Type"])
	print(res.json())
	data = res.json()
	print(data['main']['temp'])

def numbers():
	api_url = "http://numbersapi.com/"
	number = input("number? ")
	api_url = api_url + number + '/math?json=true'
	
	res = requests.get(api_url)
	#print(res.json())
	
	data = res.json()
	print(data['text'])

def dict():
	url = 'https://dictionary.yandex.net/api/v1/dicservice.json/getLangs?key='
	api_key = 'dict.1.1.20171217T160347Z.c014fa68efdd5e4a.0bbe21d3d530b534bd6bab22450cc2c9072cca41'
	url = url + api_key
	
	res1 = requests.get(url)
	print(res1.json())
	print('_____________________')
	print()
	print()
	
	text = input('text? ')
	'''
	url2 = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key='
	url2 = url2 + api_key
	url2 = url2 + '&lang=en-ru&text='
	url2 = url2 + text
	res2 = requests.get(url2)
	print(res2.json())
	print('_____________________')
	print()
	print()
	'''
	
	url3 = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?'
	params = {
		'key' : api_key,
		'lang' : 'en-ru',
		'text' : text
	}
	res3 = requests.get(url3, params=params)
	print(res3.json())
		
def trans():
	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?' 
	api_key = 'trnsl.1.1.20171217T164936Z.364a5a0e4b82abbd.67bce170e72f05f61f546d62ddb9a2148ab6b781'
	
	text = input('text? ')
	
	params = {
		'key' : api_key,
		'lang' : 'en-ru',
		'text' : text
	}
	res = requests.get(url, params=params)
	print(res.json())

dict()

