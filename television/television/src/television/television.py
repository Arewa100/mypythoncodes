class Tv:
    def __init__(self):
        self.__channel:int = 1
        self.__volume_level:int = 0
        self.__is_on:bool = False


    def _is_on(self):
        return self.__is_on


    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def get_channel(self):
        if self.__tv_is_on():
            return self.__channel
        else:
            return 0

    def __tv_is_on(self):
            if self.__is_on:
                return True
            else:
                return False

    def set_channel(self, channel):
        if self.__television_is_on_and_channel_is_within_range(channel):
            self.__channel = channel
        else:
            return self.__channel

    def get_volume(self):
        if self.__tv_is_on():
            return self.__volume_level
        else:
            return 0

    def set_volume(self, volume):
        if self.__tv_is_on():
            self.__volume_level = volume
        else:
            return 0

    def channel_up(self):
        if self.__tv_is_on():
            self.__channel += 1
        else:
            return 0

    def channel_down(self):
        if self.__tv_is_on() and self.__channel > 1:
            self.__channel -= 1
        else:
            return 0

    def volume_up(self):
        if self.__tv_is_on():
            self.__volume_level += 1
        else:
            return 0

    def volume_down(self):
        if self.__tv_is_on() and self.__volume_level > 0:
            self.__volume_level -= 1
        else:
            return 0

    def __channel_within_range(self, channel):
        if channel >= 1 and channel <= 100:
            return True
        else:
            return False


    def __television_is_on_and_channel_is_within_range(self, channel):
        if self.__tv_is_on() and self.__channel_within_range(channel):
            return True
        else:
            return False

