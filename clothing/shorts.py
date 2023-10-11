from .clothing import Clothing
from seasons import HotWeather



class Shorts(Clothing, HotWeather):
    def __init__(self, name, color, price, material, sku):
        Clothing.__init__(self, name, color, price, material, sku)
        HotWeather.__init__(self)

