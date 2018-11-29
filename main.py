from pysense import Pysense
from LIS2HH12 import LIS2HH12
from SI7006A20 import SI7006A20
from LTR329ALS01 import LTR329ALS01
from MPL3115A2 import MPL3115A2, ALTITUDE, PRESSURE
import time

py = Pysense()
mp = MPL3115A2(py, mode=ALTITUDE)
si = SI7006A20(py)
lt = LTR329ALS01(py)
li = LIS2HH12(py)

while True:

    #Display Temperature
    print("Temperature--------------------------------")
    print("Temperature: " + str(si.temperature()) + " deg C and Relative ")

    #Display Humidity
    print("Humidity-----------------------------------")
    print("Humidity: " + str(si.humidity()) + " %RH")

    #Display Dew Point
    print("Dew Point----------------------------------")
    print("Dew point: " + str(si.dew_point()) + " deg C")

    #Display T Ambient
    print("T Ambient----------------------------------")
    t_ambient = 24.4
    print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")

    time.sleep(10)
