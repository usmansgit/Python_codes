class Time:
    def __init__(self, hh = 0, mm = 0):
        self.__hh = hh
        self.__mm = mm

    def printout(self):
        print(f"{self.__hh:d}:{self.__mm:02d}")

    def minutes_from_midnight(self):
        return self.__mm + self.__hh * 60

    def difference_in_minutes(self, time_object):
        return time_object.minutes_from_midnight() - self.minutes_from_midnight()

    def difference_as_time_object(self, time_object):
        time_difference = self.difference_in_minutes(time_object)
        hours = time_difference // 60
        minutes = time_difference % 60

        result_object = Time(hours, minutes)
        return result_object

    def is_earlier_than(self, time_object):
        return self.difference_in_minutes(time_object) > 0

