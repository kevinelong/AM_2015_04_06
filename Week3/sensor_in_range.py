__author__ = 'kevinlong'


class Sensor():
    def __init__(self, name, lower_threshold, upper_threshold, initial_value):
        self.name = name
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.value = initial_value

    def is_high_enough(self):
        return self.value > self.lower_threshold

    def is_low_enough(self):
        return self.value < self.upper_threshold

    def is_within_limits(self):
        return self.is_high_enough() and self.is_low_enough()


if __name__ is "__main__":
    ph_sensor = Sensor("PH", -5, 5, 0)
    print(ph_sensor.is_within_limits())
    ph_sensor.value = 6
    print(ph_sensor.is_within_limits())

