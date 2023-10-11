class Clothing:
    def __init__(self, name, color, price, material, sku):
        self.name = name
        self.color = color
        if type(price) not in (int, float):
            raise TypeError('Please input an integer or float for price')
        self.__price = price
        self.__sku = sku
        self.material = material
        self.seasons = []
        self.sizes = []
        self.departments = []

    def __str__(self):
        string = f"The {self.color} {self.material} {self.name} is available for ${self.price} in the following departments: \n"
        if len(self.departments) > 0 and len(self.departments) < 3:
            for department in self.departments:
                string += f"\t* The {department}\n"
            string += f"The {self.name} is appropriate for these weather conditions: \n"
            for season in self.seasons:
                string += f"\t* {season}\n"
            return string
        else:
            string += f"\t* All Departments\nThe {self.name} is appropriate for these weather conditions: \n"
            for season in self.seasons:
                string += f"\t* {season}\n"
            return string

    def sale(self, percentage):
        percentage = percentage * 0.01
        discount = self.price * percentage
        discount = round(discount, 2)
        discount_price = self.price - discount
        discount_price = round(discount_price, 2)
        self.price = discount_price

        print(
            f"What great luck! The {self.name} is currently on sale at {percentage:.0%} off for ${discount_price:.2f}, that's a savings of ${discount:.2f}!")

    @property
    def price(self):
        try:
            return self.__price
        except AttributeError:
            return 0

    @price.setter
    def price(self, new_price):
        if type(new_price) is float or type(new_price) is int:
            self.__price = new_price
        else:
            raise TypeError('Please input a number for price')

    @property
    def sku(self):
        return self.__sku

    @property
    def available_sizes(self):
        if len(self.departments) > 0 and len(self.departments) < 3:
            print(f'The {self.name} is available in the following sizes:')
            for size in self.sizes:
                print(f'\t* {size}')
        else:
            print(f'The {self.name} is available in all sizes!')

    @sku.setter  # Ensures SKU cannot be overridden once initialized
    def sku(self, num):
        pass
