class parking_meter:
    def __init__(self, purchased_parking):
        self.purchased_parking = purchased_parking

    @property
    def purchased_parking(self):
        return self._purchased_parking

    @purchased_parking.setter
    def purchased_parking(self,value):
        if not value >= 0:
            raise ValueError("Minutes Purchased must be greater than or equal to 0")
        if not isinstance(value, int):
            raise ValueError("Minutes Purchased must be an Integer")
        self._purchased_parking = value
