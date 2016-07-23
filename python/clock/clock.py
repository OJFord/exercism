class Clock:

    def __init__(self, hour: int, minute: int):
        self._hour = int(hour)
        self._minute = int(minute)
        self._normalise()

    def __eq__(self, other) -> bool:
        return (self._hour == other._hour) and (self._minute == other._minute)

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        return '{:02d}:{:02d}'.format(self._hour, self._minute)

    def _normalise(self):
        self._hour += self._minute // 60
        self._hour %= 24
        self._minute %= 60

    def add(self, minutes: int):
        self._minute += minutes
        self._normalise()
        return self
