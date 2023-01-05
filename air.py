from lib import SDS011
import time
from datetime import datetime

sensor = SDS011('/dev/ttyUSB0', use_query_mode=True)

sensor.sleep(sleep=False)
time.sleep(30)  # ramp up time
results = sensor.query()
sensor.sleep()

with open('/home/sam/airqual/airqual.txt', 'a+') as f:
    f.write(f'{datetime.now()},{results[0]},{results[1]}\n')

