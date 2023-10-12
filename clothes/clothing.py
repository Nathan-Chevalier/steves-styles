class Clothing:
    def __init__(self, name, color, price, material, sku):
        # ? Checks to see if the initialized value of name is a string
        if not isinstance(name, str):
            raise TypeError('Please input a string for name')
        self.name = name
        # ? Checks to see if the initialized value of name is a string
        if not isinstance(color, str):
            raise TypeError('Please input a string for color')
        self.color = color
        # ? Checks to see if the price is an integer or float
        if not isinstance(price, (float, int)):
            raise TypeError('Please input an integer or float for price')
        self.__price = price
        if not isinstance(sku, (str, int)):
            raise TypeError('Please input an alphanumeric value for SKU')
        self.__sku = sku
        # ? Checks to see if the initialized value of name is a string
        if not isinstance(material, str):
            raise TypeError('Please input a string for material')
        self.material = material
        # ? Initialized empties for future components below
        self.seasons = []
        self.min_comfort = []
        self.max_comfort = []
        self.sizes = []
        self.departments = []

    def __str__(self):
        string = f"The {self.color} {self.material} {self.name} is available for ${self.price} in the following departments: \n"
        if len(self.departments) >= 1 and len(self.departments) < 4:
            for department in self.departments:
                string += f"\t* The {department}\n"
            string += f"The {self.name} is appropriate for these weather conditions (Between {min(self.min_comfort)}F and {max(self.max_comfort)}F): \n"
            for season in self.seasons:
                string += f"\t* {season}\n"
            return string
        else:
            string += f"\t* All Departments\nThe {self.name} is appropriate for these weather conditions: \n"
            for season in self.seasons:
                string += f"\t* {season}\n"
            return string

    def sale(self, percentage):  # ? Method that displays and sets the new discount price based on percentage
        if type(percentage) not in (int, float):
            raise TypeError('Please input an integer or float for price')
        percentage = percentage * 0.01
        discount = self.price * percentage
        discount = round(discount, 2)
        discount_price = self.price - discount
        discount_price = round(discount_price, 2)
        self.price = discount_price

        print(
            f"What great luck! The {self.name} is currently on sale at {percentage:.0%} off for ${discount_price:.2f}, that's a savings of ${discount:.2f}!")

    @property  # ? Ensures that the private value is used when price is evoked
    def price(self):
        try:
            return self.__price
        except AttributeError:
            return 0

    @price.setter  # ? Ensures that when price is set it must be an int or float
    def price(self, new_price):
        if type(new_price) is float or type(new_price) is int:
            self.__price = new_price
        else:
            raise TypeError('Please input a number for price')

    @property  # ? Returns available sizes, returns "All sizes" if no size or all sizes are specified
    def available_sizes(self):
        if len(self.departments) > 0 and len(self.departments) < 4:
            print(f'The {self.name} is available in the following sizes:')
            for size in self.sizes:
                print(f'\t* {size}')
        else:
            print(f'The {self.name} is available in all sizes!')

    @property  # ? Returns appropriate seasons, returns "All seasons" if no season or all seasons are specified
    def appropriate_seasons(self):
        string = f"{self.name} - Appropriate for the following seasons:\n"
        if len(self.seasons) > 0 and len(self.seasons) < 3:
            for season in self.seasons:
                string += f'\t* {season}'
            print(string)
        else:
            string += 'All seasons'
            print(string)

    @property
    def sku(self):
        return self.__sku

    @sku.setter  # ? Ensures SKU cannot be overridden once initialized
    def sku(self, num):
        pass
