class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_raw_value(distance: object) -> int:
        if isinstance(distance, Distance):
            return distance.km
        else:
            return distance

    def __add__(self, distance: object) -> object:
        value1 = Distance.get_raw_value(self)
        value2 = Distance.get_raw_value(distance)
        return Distance(value1 + value2)

    def __iadd__(self, distance: object) -> object:
        self.km += Distance.get_raw_value(distance)
        return self

    def __mul__(self, amount: int) -> object:
        return Distance(self.km * amount)

    def __truediv__(self, amount: int) -> object:
        return Distance(round(self.km / amount, 2))

    def __lt__(self, distance: object) -> bool:
        return (
            Distance.get_raw_value(self) < Distance.get_raw_value(distance)
        )

    def __gt__(self, distance: object) -> bool:
        return (
            Distance.get_raw_value(self) > Distance.get_raw_value(distance)
        )

    def __eq__(self, distance: object) -> bool:
        return (
            Distance.get_raw_value(self) == Distance.get_raw_value(distance)
        )

    def __le__(self, distance: object) -> bool:
        return (
            Distance.get_raw_value(self) <= Distance.get_raw_value(distance)
        )

    def __ge__(self, distance: object) -> bool:
        return (
            Distance.get_raw_value(self) >= Distance.get_raw_value(distance)
        )
