import pandas as pd 
# # import map_weather_trip
# import numpy as np

DIR = '../data/taxi_data/'

COLUMNS = ['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       	   'passenger_count', 'trip_distance', 'pickup_longitude',
           'pickup_latitude', 'RatecodeID', 'store_and_fwd_flag',
           'dropoff_longitude', 'dropoff_latitude', 'payment_type', 
           'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
           'improvement_surcharge', 'total_amount']


def draw_one_sample(filename):

	dirname = DIR + filename
	print(dirname)
	df = pd.read_csv(dirname)
	df = df.dropna(how='any')
	sample_df = df.sample(n = 1000)

	return sample_df

FILENAMES = ['yellow_tripdata_2015-07.csv', 'yellow_tripdata_2015-08.csv', \
			 'yellow_tripdata_2015-09.csv', 'yellow_tripdata_2015-10.csv', \
			 'yellow_tripdata_2015-11.csv', 'yellow_tripdata_2015-12.csv', \
			 'yellow_tripdata_2016-01.csv', 'yellow_tripdata_2016-02.csv', \
			 'yellow_tripdata_2016-03.csv', 'yellow_tripdata_2016-04.csv', \
			 'yellow_tripdata_2016-05.csv', 'yellow_tripdata_2016-06.csv']


if __name__ == '__main__':
	df_list = []
	for file in FILENAMES:
		df_list.append(draw_one_sample(file))
	rv = pd.concat(df_list)
	rv.to_csv('../data/sample_trip.csv')







