from .clothing import Clothing
from seasons import ColdWeather, CoolWeather
from departments import Mens, Womens, Youths, Childrens


class Sweater(Clothing, Mens, Womens):  # Mix-in strategy for composition
    def __init__(self, name, color, price, material, sku):
        Clothing.__init__(self, name, color, price, material, sku)
        Mens.__init__(self)
        Womens.__init__(self)
        CoolWeather.__init__(self)
        ColdWeather.__init__(self)
