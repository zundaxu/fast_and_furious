from WunderWeather import weather
import arrow
import csv
from datetime import date, timedelta

KEY = '534fe8de0c6c00ce'
LOCATION = 'NY/New York'
EXTRACTOR = weather.Extract(KEY)

def get_all_dates(start_y, start_m, start_d, end_y, end_m, end_d):
	'''
	Input:
	  e.g. 2017, 1, 1, 2017, 12, 31

	Return: a list
	'''

	d1 = date(start_y, start_m, start_d)
	d2 = date(end_y, end_m, end_d)
	delta = d2 - d1
	date_list = []
	for i in range(delta.days + 1):
		rv = d1 + timedelta(days=i)
		rv = rv.strftime('%Y%m%d')
		date_list.append(rv)

	return date_list



def get_weather(date):
	'''
	date : e.g. '20170801'

	data you can get: 'date', 'utcdate', 'tempm', 'tempi', 'dewptm', 
	'dewpti', 'hum', 'wspdm', 'wspdi', 'wgustm', 'wgusti', 'wdird', 
	'wdire', 'vism', 'visi', 'pressurem', 'pressurei', 'windchillm', 
	'windchilli', 'heatindexm', 'heatindexi', 'precipm', 'precipi', 
	'conds', 'icon', 'fog', 'rain', 'snow', 'hail', 'thunder', 'tornado', 
	'metar'
	'''

	d =  arrow.get(date, 'YYYYMMDD')
	response = EXTRACTOR.date(LOCATION, d.format('YYYYMMDD'))
	obs_list = response.data.observations
	for obs in obs_list:
		hour = obs['date']['hour']
		minute = obs['date']['min']
		visi = obs['visi']
		rain = obs['rain']
		snow = obs['snow']
		conds = obs['conds']
		data_list = [date, hour, minute, visi, rain, snow, conds]
		with open('weather.csv', 'a') as f:
			wb = csv.writer(f, delimiter = ',')
			wb.writerow(data_list)

	return 

if __name__ == '__main__':
	date_list = get_all_dates(2017, 1, 1, 2017, 12, 31) 
	for date in date_list:
		get_weather(date)



