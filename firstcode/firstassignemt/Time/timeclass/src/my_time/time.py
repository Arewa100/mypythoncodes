class MyTime:
    """this is a time object class"""
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hour_valid(hours)
        self._minute_valid(minutes)
        self._seconds_valid(seconds)
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hours(self):
        """this is my hour getter"""
        return self.__hours

    @hours.setter
    def hours(self, hour):
        """this is hour setter, initialises the hour attribute of the time object"""
        self._hour_valid(hour)
        self.__hours = hour

    def _hour_valid(self, hour):
        """a helper method to validate hour input from user"""
        hour_is_valid = 23 > hour >= 0
        if not hour_is_valid:
            raise ValueError(f"hour {hour} must be less than or equal to 23")

    @property
    def minutes(self):
        """this is my minutes getter"""
        return self.__minutes

    @minutes.setter
    def minutes(self, minute):
        """this is my minutes setter, initialises the minute attribute of the time object"""
        self._minute_valid(minute)
        self.__minutes = minute

    def _minute_valid(self, minute):
        minute_is_valid = 0 <= minute <= 59
        if not minute_is_valid:
            raise ValueError(f"minute {minute} must be greater than zero or less than or equal to or equal to 59")

    @property
    def second(self):
        return self.__seconds

    @second.setter
    def second(self, seconds):
        self._minute_valid(seconds)
        self.__seconds = seconds

    def _seconds_valid(self, seconds):
        seconds_is_valid = 0 <= seconds < 59
        if not seconds_is_valid:
            raise ValueError(f"seconds {seconds} must be greater than zero or less than or equal to 59")