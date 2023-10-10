class Clothing:
    def __init__(self, name, color, price, material, sku):
        self.name = name
        self.color = color
        self.price = price
        self.__sku = sku
        self.material = material
        self.min_comfort = 0
        self.max_comfort = 0
        self.sizes = []

    @property
    def sku(self):
        return self.__sku

    @sku.setter  # Ensures SKU cannot be overridden once initialized
    def sku(self, num):
        pass
