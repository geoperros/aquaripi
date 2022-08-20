# aquaripi

Experimentations with the dht11 and ds18b20 sensors and a relay controlling a pc case fan, in order to activly cool the aquarium using evaporative cooling.

GetTemp.py Prints into the terminal the air temperature humidity, and the water temperature.
GetTemp_test2.py uses Adafruits DHT library to read the temperature and humidity and logs it into a txt file.
relay.py gets the temperature provided from the ds18b20 sensor and decides if the temperature is high enough in order to arm the relay and spin the fan to cool the water.

Work in progress.