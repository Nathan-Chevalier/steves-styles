class Clothing:
    def __init__(self, name, color, price, material, sku):
        self.name = name
        self.color = color
        self.price = price
        self.__sku = sku
        self.material = material
        self.seasons = []
        self.sizes = []
        self.departments = []

    def __str__(self):
        string = f"The {self.color} {self.material} {self.name} is available in the following departments: \n"
        for department in self.departments:
            string += f"\t* The {department}\n"
        string += f"The {self.name} is appropriate for these weather conditions: \n"
        for season in self.seasons:
            string += f"\t* {season}\n"
        return string

    def sale(self, percentage):
        percentage = percentage * 0.01
        discount = self.price * percentage
        discount = round(discount, 2)
        discount_price = self.price - discount
        discount_price = round(discount_price, 2)

        print(
            f"What great luck! The {self.name} is currently on sale for ${discount_price:.2f}, that's a savings of ${discount:.2f}!")

    @property
    def sku(self):
        return self.__sku

    @property
    def available_sizes(self):
        print(f'The {self.name} is available in the following sizes:')
        for size in self.sizes:
            print(f'\t* {size}')

    @sku.setter  # Ensures SKU cannot be overridden once initialized
    def sku(self, num):
        pass
