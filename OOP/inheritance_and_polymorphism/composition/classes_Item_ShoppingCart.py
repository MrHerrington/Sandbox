class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}$'


class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            self.items = list()
        else:
            self.items = items

    def __str__(self):
        return '\n'.join(map(str, self.items))

    def add(self, item):
        self.items.append(item)

    def total(self):
        return sum(map(lambda x: x.price, self.items))

    def remove(self, name):
        self.items = [item for item in self.items if item.name != name]


# Test №1
item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)

# Test №2
shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])
shopping_cart.add(Item('Flannel Shirt', 22))

print(shopping_cart)
print(shopping_cart.total())

# Test №3
shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())
