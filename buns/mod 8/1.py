class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    def __str__(self):
        return f"Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}"

    def isInArea(self, pos_x, pos_y, length, width):
        if pos_x <= self.coordinates[0] <= pos_x + length and \
                pos_y <= self.coordinates[1] <= pos_y + width:
            return True
        return False


class Passenger(Transport):
    def __init__(self):
        self.__passengers_capacity = None
        self.__number_of_passengers = None

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self):
        self.__carrying = None

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Auto(Transport):
    def __init__(self, color, coordinates, speed, brand, year, number, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number)
        super().init(*args, **kwargs)
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Ship(Transport):
    def __init__(self, name, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port


class Car(Auto):
    def __init__(self, coordinates, speed, brand, year, number, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number)
        super().init(*args, **kwargs)


class Bus(Auto, Passenger):
    def __init__(self, coordinates, speed, brand, year, number, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number)
        super().init(*args, **kwargs)


class CargoAuto(Auto, Cargo):
    def __init__(self, coordinates, speed, brand, year, number, *args, **kwargs):
        super().__init__(coordinates, speed, brand, year, number)
        super().init(*args, **kwargs)


class Boat(Ship):
    def __init__(self, name, port, *args, **kwargs):
        super().__init__(name, port, *args, **kwargs)
        super().init(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, name, port, *args, **kwargs):
        super().__init__(name, port, *args, **kwargs)
        super().init(*args, **kwargs)


class CargoShip(Ship, Cargo):
    def __init__(self, name, port, *args, **kwargs):
        super().__init__(name, port, *args, **kwargs)
        super().init(*args, **kwargs)


class Seaplane(Plane, Ship):
    def __init__(self, height, *args, **kwargs):
        super().__init__(height, *args, **kwargs)
        super().init(*args, **kwargs)
