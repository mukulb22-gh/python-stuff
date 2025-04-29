#Iterator design pattern with dairy productclass DairyProduct:

# class DairyProduct
class DairyProduct:
    def __init__(self, name, expiration_date):
        self.name = name
        self.expiration_date = expiration_date

    def __str__(self):
        return f"{self.name} (Expires: {self.expiration_date})"

# class DairyIterator
class DairyIterator:
    def __init__(self, dairy_products):
        self.dairy_products = dairy_products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dairy_products):
            product = self.dairy_products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


# class DairCollection
class DairyCollection:
    def __init__(self):
        self.dairy_products = []

    def add_product(self, product):
        self.dairy_products.append(product)

    def __iter__(self):
        return DairyIterator(self.dairy_products)


if __name__ == "__main__":
    dairy_collection = DairyCollection()
    dairy_collection.add_product(DairyProduct("Milk", "2025-04-15"))
    dairy_collection.add_product(DairyProduct("Yogurt", "2025-04-20"))
    dairy_collection.add_product(DairyProduct("Cheese", "2025-04-10"))

    for product in dairy_collection:
        print(product)
         examples

