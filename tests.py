import sys
import json
from tests.config import API_TOKEN
from yaschedule.core import YaSchedule


yaschedule = YaSchedule(API_TOKEN)

moscow = 'c213'
spb = 'c2'

pulkovo = 's9600366'
sheremetevo = 's9600213'

x = yaschedule.get_schedule(moscow, spb, transport_types='train')
