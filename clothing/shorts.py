from .clothing import Clothing
from seasons import HotWeather
# from departments import Mens


class Shorts(Clothing, HotWeather):
    def __init__(self, name, color, price, material, sku):
        Clothing.__init__(self, name, color, price, material, sku)
        HotWeather.__init__(self)
        # Mens.__init__(self)
