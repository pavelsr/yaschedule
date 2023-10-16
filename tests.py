import logging
import sys
import json
from tests.config import API_TOKEN
from yaschedule.core import YaSchedule

logging.basicConfig(level='INFO')


yaschedule = YaSchedule(API_TOKEN)

moscow = 'c213'
spb = 'c2'

pulkovo = 's9600366'
sheremetevo = 's9600213'

test_case1 = yaschedule.get_schedule(moscow, spb, transport_types='train')
test_case2 = yaschedule.get_station_schedule(station='s9600366', transport_types='plane')
