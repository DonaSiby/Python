class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# Create an instance of the Apple class
apple = Apple("red", "sweet")

# Format and print the message directly
print("This apple is {} and its flavor is {}".format(apple.color, apple.flavor))


class Apple1:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

# Create an instance of the Apple class
apple1 = Apple1("red", "sweet")

# When we print the apple object, it uses the default representation
print(apple1)


class Apple2:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

# Create an instance of the Apple class
apple2 = Apple2("red", "sweet")

# When we print the apple object, it uses the __str__ method
print(apple2)

