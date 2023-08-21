from sense_hat import SenseHat
from db_funcs import *
from time import sleep

sense = SenseHat()
sense.clear()
# add_values alr takes in arbitrary num of args, dont makr this a list later
i = 0

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
delete_all()
while i < 5:
    sleep(1)
    temp = str(int(sense.get_temperature_from_pressure())-10.0) #adjusting for temp sensors erroer (abt ten degrees)
    humidity = str(int(sense.get_humidity()))
    pressure = str(int(sense.get_pressure()))
    sql = """
        INSERT INTO weather VALUES ({}, {}, {}, NOW())
        """.format(temp, humidity, pressure)
        
    add_values(sql=sql)
    i += 1
show_table()
