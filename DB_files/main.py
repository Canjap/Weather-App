from sense_hat import SenseHat
from db_funcs import connect, add_values
from time import sleep

sense = SenseHat()
sense.clear()
values = [] # add_values alr takes in arbitrary num of args, dont makr this a list later
i = 0
# 
# while i < 10:
#     sleep(1)
#     temp = str(sense.get_temperature())
#     humidity = str(sense.get_humidity())
#     pressure = str(sense.get_pressure())
#     values.append(
#         """
#         INSERT INTO weather VALUES ({}, {}, {})
#         """.format(temp, humidity, pressure)
#         )
    
while i < 10:
    sleep(1)
    temp = str(sense.get_temperature_from_pressure())
    humidity = str(sense.get_humidity())
    pressure = str(sense.get_pressure())
    add_values(temp, humidity, pressure)
    i += 1