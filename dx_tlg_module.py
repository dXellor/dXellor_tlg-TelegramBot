import time, datetime
import random
import requests
import json
import sys

def LoadDic(dic):
	d = {}

	with open(dic) as dicti:
		d = eval(dicti.read())

	return d

def ParseToMinutes(hours, minutes):
	return int(hours)*60 + int(minutes)

files = LoadDic('dic/files_dic.txt')
api_keys = LoadDic('dic/apikeys_dic.txt')

def Start():
	m = ''

	with open(files['STR'], 'r', encoding="utf8") as f:
		for line in f:
			m += line

	return m

def Help():
	m = ''

	with open(files['HLP'], 'r', encoding="utf8") as f:
		for line in f:
			m += line

	return m

def Greetings():
	return "Hello there!"

def CurrentTime():
	return datetime.datetime.now()

def Quote(mark):
	x = []
	global files

	try:
		with open(files[mark] , 'r', encoding="utf8") as f:
				for line in f:
					x.append(line)
		q = random.choice(x)
	except:
		q = 'An error occurred!'
	finally:
		return q

def AddQuote(mark, quote):
	global files
	r = ''

	try:
		with open(files[mark] , 'w', encoding="utf8") as f:
			f.writelines(quote)
		r = 'Quote is successfully added to ' + str(mark) + ' file'
		with open('files/quotes/quote_updates.txt', 'w', encoding="utf8") as f:
			f.writelines(quote + ' // ' + files[mark] + ' // ' +  str(CurrentTime().date()))
	except:
		r = 'An error occurred!'
	finally:
		return r

def getWeather(param):
	global api_keys
	parameters = {
		'q' : param,
		'appid' : api_keys['OpenWeatherAPI'],
		'units' : 'metric'
	}
	url = 'http://api.openweathermap.org/data/2.5/weather?'
	response = requests.get(url, params = parameters)
	#print(response.status_code)
	data = response.json()

	return data

def Weather(par):
	d = ''

	try:
		data = getWeather(par)
		d += 'Weather: ' + str(data['weather'][0]['main']) + '\n'
		d += 'Description: ' + str(data['weather'][0]['description']) + '\n'
		d += 'Temperature: ' + str(data['main']['temp']) + ' °C' + '\n'
		d += 'Air Pressure: ' + str(data['main']['pressure']) + ' bar' + '\n'
		d += 'Humidity: ' + str(data['main']['humidity']) + ' %' + '\n'
	except:
		d = 'An error occurred!'
	finally:
		return d

def getCrypto():
	parameters = {
		'vs_currency' : 'usd',
		'per_page' : 5
	}
	url = 'https://api.coingecko.com/api/v3/coins/markets?'
	response = requests.get(url, params = parameters)
	print(response.status_code)
	data = response.json()

	return data

def Crypto():
	d = ''

	try:
		data = getCrypto()
		for item in data:
			d += 'Coin: ' + item['name'] + '\n'
			d += 'Symbol: ' + item['symbol'] + '\n'
			d += 'Price: ' + '$' + str(item['current_price']) + '\n'
			d += 'Market Cap rank: ' + str(item['market_cap_rank']) + '\n'
			d += 'Market Cap: ' + '$' + str(item['market_cap']) + '\n\n'
	except:
		d = 'An error occurred!'
	finally:
		return d

def Bus(to):
	bus_list = []
	ct = CurrentTime()
	index = []
	br = 0
	message = ''

	try:
		with open(files[to], 'r', encoding="utf-8") as f:
			for line in f:
				bus_list.append(line)
		
		min_time = 1440

		while(br < 2):
			for bus in bus_list:
				time = ParseToMinutes(bus.split(':')[1], bus.split(':')[2])
				if(time < ParseToMinutes(ct.hour, ct.minute)):
					continue
				if(time < min_time):
					min_time = time
					temp_bus = bus			

			index.append(temp_bus)
			br += 1
			bus_list.remove(temp_bus)
			min_time = 1440

		message += str('Najblizi bus je ' + index[0].split(":")[0] + ' u: ' + index[0].split(":")[1] + ':' + index[0].split(":")[2] + '\n')
		message += str('Nakon njega najblizi bus je ' + index[1].split(":")[0] + ' u: ' + index[1].split(":")[1] + ':' + index[1].split(":")[2] + '\n')

	except:
		message = 'An error ocured!'

	finally:
		return message

def Contact():
	s = ''
	s += 'Developer contact:\n'
	s += 'Email: dxellor@gmail.com\n'
	s += 'GitHub: https://github.com/dXellor'

	return s

#def SetReminder():