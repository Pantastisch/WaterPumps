# Challenge

## Target

Your water pumps send a lot of data to your service. Every 30 seconds they send an update of their current energy consumption. Every 1h one of your rain gauges send information about the current rainfall measures. Save the data and lets do some analysis with it! Note: If you get a timeout error on the test run your implementation is not efficient enough.

```python
import datetime
import numpy as np
import arrow


class WaterPumpAnalyzer:
    def __init__(self):
        # Create your storage attributes here.
        pass

    def handle_message(self, data: dict):
        # This method gets called with the raw data. Implement this in Scenario 1.
        pass

    def get_raw_data(self, timestamp: str, device: str, location: str) -> dict:
        # Implement this in Scenario 1
        pass

    def is_error_mode(self, start: datetime.date, end: datetime.date, location: str) -> bool:
        # Implement this in Scenario 2,3 and 4
        pass
```

## Szenario 1: Saving and accessing the raw data

Our water pumps send data via a message bus about their current status. To do further analysis with this data you need to save the data of water pumps and rain gauges for later usage. This is too easy for you? Think about the fastest and most space efficient way to do this!

>The method `handle_message` gets called with every data update of every device in the network. You need to save every data that is needed for the later analysis. You can save the data in every Python data structure you want.

When the method `handle_message` gets called with `{'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'pump', 'location': 'Hamburg', 'energy_consumption': 1269}` it should be saved. This message is sent every 30 seconds by every pump to your service.

>The method `get_raw_data` should return the data that was saved before. For "pump" devices it should return the `energy_consumption` value for all water pumps. When it is called with the parameter that describe the previous data: `get_raw_data(timestamp="2020-02-10T11:33:00.299356+01:00", device="pump", location="Hamburg")` it should return the `1269` .

For later analysis you will also need to save the data which is sent by `"rain_gauge"` devices. When the `handle_message` method is called with this data it should also be saved.

>When the `handle_message` method is called with `{'time': '2020-02-10T11:33:00.299356+01:00', 'device': 'rain_gauge', 'location': 'Dresden', 'value': 47}` it should be saved. This message is sent every hour to your service.

The method `get_raw_data` should return the `value` for all `"rain_gauge"` devices. When its get called with `get_raw_data(timestamp='2020-02-10T11:33:00.299356+01:00', device="rain_gauge", location="Dresden")` it should return `47`

>This should work for other data entries as well.

## Szenario 2: Analyzing water pump failures

To find failues of the water pumps you need to implement an analysis based on their power consumption an the current rain conditions. When the power consumption increases it could have two reasons: 1. The pump is broken or 2. The amount of rain water also increased. You have to find out what it is!

>The analysis result shoud be returned by the `is_error_mode` method. It should return `False` if there is no error or `True` when the pump is in an error state for the given date range.

The error state is defined as follows: When the energy consumption of a pump rises over 20% of its average but the rain is not over 20% of the average it should return `True` and in all other cases `False` . The average of the energy consumption and the rain amount should be compared with the values of the period with the same length before the start-date. Example: when the method gets called with start: 03.10. and end 04.10. then compare the values of 01.10 - 02.10. with the values of 03.10. - 04.10.

![ater-pump.png](/pic/water-pump.png)

>Given is the data of the pumps in the two cities `Berlin` and `Hamburg` .

For the energy consumption of the pump and the rain amount in Berlin is in the average and does not increase.

>The method `is_error_mode(start=13.02.2020, end=14.02.2020, location="Berlin")` is called.

The power consumption and the rain amount in the ranges `13.02.2020 - 14.02.2020` and `11.02.2020 - 12.02.2020` are nearly equal. Your method should return `False` .

>The energy consumption of the pump in Hamburg raises over 20% of its normal value, but also does the rain.

The method `is_error_mode(start=13.02.2020, end=14.02.2020, location="Hamburg")` gets called.

>Since the power consumption increases because of the rain it should also return `False` .

## Szenario 3: Analyzing pumps that are in error state

Now let's have a look into more examples.

>Given is the data of the pumps in `Zuerich` and `Wuppertal` .

The energy consumption of the pump in Zuerich increases over 20% of the average, but the rain does not! The pump should be in error state!

>When the method is called with `is_error_mode(03.02.2020, 04.02.2020, "Zuerich")` it should return `True` .

The power consumption of the pump in Wuppertal is in average. When the method is called with `is_error_mode(03.02.2020, 04.02.2020, "Wuppertal")` it should return `False` .

>This should also work with different cities and date ranges as well.

## Szenario 4: Optimizing and the Real Money Competition

Find the fastest and most memory efficient solution!

>Find ways to optimize your solution. Try to make it as fast as you can and use only the space that you need. Think about what happens when you solution gets called with millions of datasets. You can use `numpy` if you want.

Some information about the **Real-Money-Competition**:

>The take part in the competition your solution has to be fully functional (i.e. no hard-coded values).

The Test-Data for the competition will be different than for the challenge. We will use much more data and more cities. The sampling rate (1/30s for energy consumptions, 1/1h rain gauge) can be different.

>In the competition the test data set will be very large but is only read once (using your `handle_message` method for every sample). With this data we do 20 analysis (using your `is_error_mode` method).

The ranges for the i`s_error_mode` requests can be up to one month. We will test short ranges (1-3 days) and long ranges (up to 1 month). The test setup will be equal for all participants.

>We will determine the winner by evaluating the overall run time of your code and the memory usage. For scoring we use the same measuring as FaaS-Providers (`1MB ≙ 1ms`).

To take part finish the challenge before `19.02.2020 15:00 Uhr`. We will announce the winners at the `20.02.2020`
