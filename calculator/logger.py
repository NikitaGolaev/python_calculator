from datetime import datetime
from time import time


def logger_file(data):
    time_data = datetime.now().strftime('%H:%M (%D)')
    with open('log.csv', 'a') as file:
        file.write(f'{time_data}; {data} \n')
