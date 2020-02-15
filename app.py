import datetime
# import numpy as np
# import arrow

stub_handle_message_time = list()
stub_handle_message_time.append({'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 1269})
stub_handle_message_time.append({'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Dresden', 'value': 47})

def main():
    a = WaterPumpAnalyzer()

    # Szenario 1, Data 1
    a.handle_message(stub_handle_message_time[0])
    print(a.get_raw_data(timestamp="2020-02-10T11:33:00.299356+01:00", device="pump", location="Hamburg"))

    # Szenario 1, Data 2
    a.handle_message(stub_handle_message_time[1])
    print(a.get_raw_data(timestamp='2020-02-10T11:33:00.299356+01:00', device="rain_gauge", location="Dresden"))

    pass

class WaterPumpAnalyzer:
    def __init__(self):
        self.__locations__ = list()

    @property
    def locations(self):
        return self.__locations__

    def handle_message(self, data: dict):
        location = data.get('location')

        if (self._is_location_in_locations(location) is False):
            self._add_location(location)

        self.location(location).add_measurement(data)

    def get_raw_data(self, timestamp: str, device: str, location: str) -> dict:
        return self.location(location).get_measurement(device, timestamp)

    def is_error_mode(self, start: datetime.date, end: datetime.date, location: str) -> bool:
        pass

    def location(self, location):
        return self._get_fitting_locations(location)[0]

    def _add_location(self, location):
        self.locations.append(WaterPumpAnalyzerLocation(location))

    def _get_fitting_locations(self, location):
        return [x for x in self.locations if (x.location == location)]

    def _is_location_in_locations(self, location):
        return any(self._get_fitting_locations(location))

class WaterPumpAnalyzerLocation:

    def __init__(self, location):
        self.__location__ = location
        self.__pump__ = WaterPumpAnalyzerDevice('pump')
        self.__rain_gauge__ = WaterPumpAnalyzerDevice('rain_gauge')

    @property
    def location(self):
        return self.__location__

    @property
    def pump(self):
        return self.__pump__

    @property
    def rain_gauge(self):
        return self.__rain_gauge__

    def add_measurement(self, data):
        device = data.get('device')
        time = self._make_datetime(data.get('time'))

        if (device == 'pump'):
            value = data.get('energy_consumption')
            self.pump.add_measurement(time, value)
        elif (device == 'rain_gauge'):
            value = data.get('value')
            self.rain_gauge.add_measurement(time, value)
        else:
            raise ValueError('Unknown device_type "' + device + '"')

    def get_measurement(self, device, time):
        time = self._make_datetime(time)

        if (device == 'pump'):
            measurement = self.pump.get_measurement(time)
        elif (device == 'rain_gauge'):
            measurement = self.rain_gauge.get_measurement(time)
        else:
            raise ValueError('Unknown device_type "' + device + '"')

        return measurement

    def _make_datetime(self, time):
        return datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')

class WaterPumpAnalyzerDevice:

    def __init__(self, device_type):
        self.__measurements__ = list()

    @property
    def measurements(self):
        return self.__measurements__

    def add_measurement(self, time, value):
        self.measurements.append(WaterPumpAnalyzerMeasurement(time, value))

    def get_measurement(self, time):
        return [x.value for x in self.measurements if x.time == time][0]

class WaterPumpAnalyzerMeasurement:

    def __init__(self, time, value):
        self.__time__ = time
        self.__value__ = value

    @property
    def time(self):
        return self.__time__

    @property
    def value(self):
        return self.__value__

if __name__ == "__main__":
    main()