from config import API_TOKEN
from yaschedule.core import YaSchedule
import json

yaschedule = YaSchedule(API_TOKEN)

moscow = 'c213'
spb = 'c2'

pulkovo = 's9600366'
sheremetevo = 's9600213'

r = yaschedule.get_stations_schedule(pulkovo, sheremetevo)
print(r)
with open('schedule_example.json', 'w') as file:
    file.write(json.dumps(r, indent=4))

