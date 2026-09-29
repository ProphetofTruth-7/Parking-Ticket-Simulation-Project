class ParkedCar:
    def __init__(self, make, model, color, license_number, minutes_parked):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self):
        return self._make
    @property
    def model(self):
        return self._model
    @property
    def color(self):
        return self._color
    @property
    def license_number(self):
        return self._license_number
    @property
    def minutes_parked(self):
        return self._minutes_parked

    
    @make.setter
    def make(self,value):
        if not isinstance(value, str):
            raise ValueError("Make must be a string")
        self._make = value

    @model.setter
    def model(self,value):
        if not isinstance(value, str):
            raise ValueError("Model must be a string")
        self._model = value

    @color.setter
    def color(self,value):
        if not isinstance(value, str):
            raise ValueError("Color must be a string")
        self._color = value

    @license_number.setter
    def license_number(self,value):
        if not isinstance(value, str):
            raise ValueError("License Number must be a string")
        self._license_number = value

    @minutes_parked.setter
    def minutes_parked(self,value):
        if not value >= 0:
            raise ValueError("Minutes Parked must be greater than or equal to 0")
        if not isinstance(value, int):
            raise ValueError("Minutes Parked must be an Integer")
        self._minutes_parked = value