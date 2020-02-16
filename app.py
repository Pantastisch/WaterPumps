import datetime

stub_handle_message_time = list()
# Szenario 1, Data 1
stub_handle_message_time.append({'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 1269})

# Szenario 1, Data 2
stub_handle_message_time.append({'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Dresden', 'value': 47})

# Szenario 2, Data 1
stub_handle_message_time.append({'time': '2020-02-11T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Berlin', 'energy_consumption': 1200})
stub_handle_message_time.append({'time': '2020-02-12T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Berlin', 'energy_consumption': 1200})
stub_handle_message_time.append({'time': '2020-02-13T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Berlin', 'energy_consumption': 3000})
stub_handle_message_time.append({'time': '2020-02-14T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Berlin', 'energy_consumption': 3000})
stub_handle_message_time.append({'time': '2020-02-11T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Berlin', 'value': 30})
stub_handle_message_time.append({'time': '2020-02-12T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Berlin', 'value': 30})
stub_handle_message_time.append({'time': '2020-02-13T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Berlin', 'value': 100})
stub_handle_message_time.append({'time': '2020-02-14T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Berlin', 'value': 100})

# Szenario 2, Data 2
stub_handle_message_time.append({'time': '2020-02-11T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 1200})
stub_handle_message_time.append({'time': '2020-02-12T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 1200})
stub_handle_message_time.append({'time': '2020-02-13T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 3000})
stub_handle_message_time.append({'time': '2020-02-14T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 3000})
stub_handle_message_time.append({'time': '2020-02-11T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Hamburg', 'value': 0})
stub_handle_message_time.append({'time': '2020-02-12T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Hamburg', 'value': 0})
stub_handle_message_time.append({'time': '2020-02-13T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Hamburg', 'value': 0})
stub_handle_message_time.append({'time': '2020-02-14T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Hamburg', 'value': 0})

# Szenario 3, Data 1
stub_handle_message_time.append({'time': '2020-02-01T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Zuerich', 'energy_consumption': 1281.223385633678})
stub_handle_message_time.append({'time': '2020-02-02T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Zuerich', 'energy_consumption': 1281.223385633678})
stub_handle_message_time.append({'time': '2020-02-03T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Zuerich', 'energy_consumption': 2593.6619250000026})
stub_handle_message_time.append({'time': '2020-02-04T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Zuerich', 'energy_consumption': 2593.6619250000026})
stub_handle_message_time.append({'time': '2020-02-01T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Zuerich', 'value': 2.1041666666666665})
stub_handle_message_time.append({'time': '2020-02-02T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Zuerich', 'value': 2.1041666666666665})
stub_handle_message_time.append({'time': '2020-02-03T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Zuerich', 'value': 2.4791666666666665})
stub_handle_message_time.append({'time': '2020-02-04T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Zuerich', 'value': 2.4791666666666665})

# Szenario 3, Data 2
stub_handle_message_time.append({'time': '2020-02-01T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Wuppertal', 'energy_consumption': 100})
stub_handle_message_time.append({'time': '2020-02-02T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Wuppertal', 'energy_consumption': 100})
stub_handle_message_time.append({'time': '2020-02-03T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Wuppertal', 'energy_consumption': 120})
stub_handle_message_time.append({'time': '2020-02-04T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Wuppertal', 'energy_consumption': 120})
stub_handle_message_time.append({'time': '2020-02-01T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Wuppertal', 'value': 100})
stub_handle_message_time.append({'time': '2020-02-02T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Wuppertal', 'value': 100})
stub_handle_message_time.append({'time': '2020-02-03T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Wuppertal', 'value': 120})
stub_handle_message_time.append({'time': '2020-02-04T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Wuppertal', 'value': 120})

def main():
    a = WaterPumpAnalyzer()

    for x in stub_handle_message_time:
        a.handle_message(x)

    # Szenario 1, Data 1
    print(a.get_raw_data(timestamp="2020-02-10T11:33:00.299356+01:00", device="pump", location="Hamburg"))
    # Expect 1269

    # Szenario 1, Data 2
    print(a.get_raw_data(timestamp='2020-02-10T11:33:00.299356+01:00', device="rain_gauge", location="Dresden"))
    # Expect 47

    # # Szenario 2, Data 1
    start = datetime.date(2020, 2, 13)
    end = datetime.date(2020, 2, 14)
    print(str(a.is_error_mode(start=start, end=end, location="Berlin")))
    # # Expect False

    # # Szenario 2, Data 2
    start = datetime.date(2020, 2, 13)
    end = datetime.date(2020, 2, 14)
    print(str(a.is_error_mode(start=start, end=end, location="Hamburg")))
    # # Expect True

    # Szenario 3, Data 1
    start = datetime.date(2020, 2, 3)
    end = datetime.date(2020, 2, 4)
    print(str(a.is_error_mode(start=start, end=end, location="Zuerich")))
    # Expect True

    # Szenario 3, Data 2
    start = datetime.date(2020, 2, 3)
    end = datetime.date(2020, 2, 4)
    print(str(a.is_error_mode(start=start, end=end, location="Wuppertal")))
    # Expect False

    pass

import datetime

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
        return self.location(location).measurement(device, timestamp)

    def is_error_mode(self, start: datetime.date, end: datetime.date, location: str) -> bool:
        return self.location(location).is_error_mode(start, end)

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
            value = (data.get('energy_consumption'))
            self.pump.add_measurement(time, value)
        elif (device == 'rain_gauge'):
            value = (data.get('value'))
            self.rain_gauge.add_measurement(time, value)
        else:
            raise ValueError('Unknown device_type "' + device + '"')

    def is_error_mode(self, start, end):
        pump_delta_average = self.pump.periode_delta_average_percent(start, end)
        rain_gauge_delta_average = self.rain_gauge.periode_delta_average_percent(start, end)

        if (pump_delta_average > self.pump.average_threshold and
            rain_gauge_delta_average <= self.rain_gauge.average_threshold):
            return True
        else:
            return False

    def measurement(self, device, time):
        time = self._make_datetime(time)

        if (device == 'pump'):
            measurement = self.pump.measurement(time)
        elif (device == 'rain_gauge'):
            measurement = self.rain_gauge.measurement(time)
        else:
            raise ValueError('Unknown device_type "' + device + '"')

        return measurement

    def _make_datetime(self, time):
        return datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%f%z')

class WaterPumpAnalyzerDevice:

    def __init__(self, device_type):
        self.__measurements__ = list()
        self.__average_threshold__ = 20

    @property
    def average_threshold(self):
        return self.__average_threshold__

    @average_threshold.setter
    def average_threshold(self, threshold):
        self.__average_threshold__ = threshold

    @property
    def measurements(self):
        return self.__measurements__

    def add_measurement(self, time, value):
        self.measurements.append(WaterPumpAnalyzerMeasurement(time, value))

    def average(self, start, end):
        measurements = self.measurements_in_periode(start, end)
        measurements_count = len(measurements)

        if measurements_count == 0:
            return 0
        else:
            return sum(measurements) / measurements_count

    def measurement(self, time):
        return [x.value for x in self.measurements if x.time == time][0]

    def measurements_in_periode(self, start, end):
        return [x.value for x in self.measurements if (x.time.date() >= start and x.time.date() <= end)]

    def periode_delta_average_percent(self, start, end):
        periode = end - start + datetime.timedelta(1)

        last_start = start - periode
        last_end = end - periode

        average = self.average(start, end)
        last_average = self.average(last_start, last_end)

        if last_average == 0 and average == 0:
            delta_average = 0 
        elif last_average != 0:
            delta_average = average / last_average * 100 - 100
        else:
            delta_average = 100

        return delta_average

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