from WunderWeather import weather
import arrow
import csv

KEY = '534fe8de0c6c00ce'
LOCATION = 'NY/New York'
EXTRACTOR = weather.Extract(KEY)

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
		temp = obs['tempm']
		conds = obs['conds']
		data_list = [date, hour, minute, temp, conds]
		with open('weather.csv', 'a') as f:
			wb = csv.writer(f, delimiter = ',')
			wb.writerow(data_list)

	return 

