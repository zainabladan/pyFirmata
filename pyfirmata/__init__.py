from .pyfirmata import *  # NOQA
# TODO: should change above import to an explicit list, but people might rely on
# it, so do it in a backwards breaking release
from .boards import BOARDS

__version__ = '1.0.3'  # Use bumpversion!


# shortcut classes

class Arduino(Board):
    """
    A board that will set itself up as a normal Arduino.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino'])
        super(Arduino, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Arduino {0.name} on {0.sp.port}".format(self)


class ArduinoMega(Board):
    """
    A board that will set itself up as an Arduino Mega.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino_mega'])
        super(ArduinoMega, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Arduino Mega {0.name} on {0.sp.port}".format(self)


class ArduinoDue(Board):
    """
    A board that will set itself up as an Arduino Due.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino_due'])
        super(ArduinoDue, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Arduino Due {0.name} on {0.sp.port}".format(self)


class ArduinoNano(Board):
    """
    A board that will set itself up as an Arduino Due.
    """
    def __init__(self, *args, **kwargs):
        args = list(args)
        args.append(BOARDS['arduino_nano'])
        super(nano, self).__init__(*args, **kwargs)

    def __str__(self):
        return "Arduino Nano {0.name} on {0.sp.port}".format(self)
