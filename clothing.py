class Clothing:
    def __init__(self, name, color, price, sku):
        self.name = name
        self.color = color
        self.price = price
        self.__sku = sku

    @property
    def sku(self):
        return self.__sku

    @sku.setter
    def sku(self, num):
        pass
