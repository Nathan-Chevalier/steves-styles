from .clothing import Clothing
from seasons import ColdWeather, CoolWeather
from departments import Mens, Womens


class Sweater(Clothing, ColdWeather, Mens, Womens):
    def __init__(self, name, color, price, material, sku):
        Clothing.__init__(self, name, color, price, material, sku)
        ColdWeather.__init__(self)
        CoolWeather.__init__(self)
        Mens.__init__(self)
        Womens.__init__(self)
