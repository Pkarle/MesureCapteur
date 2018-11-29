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

    print("Temperature: " + str(si.temperature()) + " deg C and Relative Humidity: " + str(si.humidity()) + " %RH")
    print("Dew point: " + str(si.dew_point()) + " deg C")
    t_ambient = 24.4
    print("Humidity Ambient for " + str(t_ambient) + " deg C is " + str(si.humid_ambient(t_ambient)) + "%RH")

    """
    
    print("MPL3115A2 temperature: " + str(mp.temperature()))
    print("Altitude: " + str(mp.altitude()))
    mpp = MPL3115A2(py, mode=PRESSURE)
    print("Pressure: " + str(mpp.pressure()))
    
    print("Light (channel Blue lux, channel Red lux): " + str(lt.light()))
        
    print("Acceleration: " + str(li.acceleration()))
    print("Roll: " + str(li.roll()))
    print("Pitch: " + str(li.pitch()))
    
    print("Battery voltage: " + str(py.read_battery_voltage()))
    
    """
    time.sleep(10)
