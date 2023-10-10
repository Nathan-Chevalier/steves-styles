from .clothing import Clothing 
from seasons import ColdWeather
class Sweater(Clothing, ColdWeather):
    def __init__(self, name, color, price, material, sku):
        Clothing.__init__(self, name, color, price, material, sku)
        ColdWeather.__init__(self)