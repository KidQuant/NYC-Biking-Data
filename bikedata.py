import pandas as pd
from datetime import datetime


df = pd.read_csv('crashes.csv')
df.info()

df = df[['CRASH DATE', 
    'CRASH TIME', 
    'LATITUDE', 
    'LONGITUDE', 
    'LOCATION',
    'NUMBER OF CYCLIST INJURED',
    'NUMBER OF CYCLIST KILLED',
    'CONTRIBUTING FACTOR VEHICLE 1',
    'CONTRIBUTING FACTOR VEHICLE 2',
    'VEHICLE TYPE CODE 1',
    'VEHICLE TYPE CODE 2']]

df = df[(df['NUMBER OF CYCLIST INJURED'] > 0) | (df['NUMBER OF CYCLIST KILLED'] > 0)]

df = df.reset_index(drop=True)

df.info()
 
df = df[df['VEHICLE TYPE CODE 2'].notna()]
df = df[df['LOCATION'].notna()]

df.columns = [x.lower() for  x in df.columns]
df.columns = [x.replace(' ', '_').lower() for x in df.columns]

list(df.columns)

df.shape

accidents_info_df = df[['crash_date', 
                        'crash_time', 
                        'number_of_cyclist_injured',
                        'number_of_cyclist_killed',
                        'contributing_factor_vehicle_1',
                        'contributing_factor_vehicle_2',
                        'vehicle_type_code_1',
                        'vehicle_type_code_2']]



accidents_info_df.shape

accidents_info_df[accidents_info_df['vehicle_type_code_2'] == 'Bike']['contributing_factor_vehicle_1'].value_counts()

accidents_info_df[accidents_info_df['vehicle_type_code_1'] == 'Bike']['contributing_factor_vehicle_1'].value_counts()

