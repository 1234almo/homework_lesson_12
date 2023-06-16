class Fruit:
    def __init__(self, name, colour, yummy):
        self.name = name
        self.colour = colour
        self.yummy = yummy

    def description(self):
        print(f"The {self.name} is {self.colour}.")

    def yummyness(self):
        print(f"The {self.name} tastes very {self.yummy}.")

    def __str__(self):
        return f"Fruit: {self.name}, Color: {self.colour}"
    

class Apple(Fruit):
    def __init__(self, name, colour, yummy, variety):
        super().__init__(name, colour, yummy)
        self.variety = variety
    
    def variety_fun(self):
        print(f"The {self.colour} {self.name} is a {self.variety}.")


class Banana(Fruit):
    def __init__(self, name, colour, yummy, length):
        super().__init__(name, colour, yummy)
        self.length = length
    
    def description(self):
        print(f"The {self.name} is {self.length} cm long.")
        super().description()
    
    
# Create instances of the classes
apple_obj = Apple("Apple", "red", "amazing", "Gala")
banana_obj = Banana("Banana", "yellow", "disgusting", 7)

# Invoke methods and print objects
apple_obj.description()
apple_obj.yummyness()
apple_obj.variety_fun()
print(apple_obj)
banana_obj.description()
banana_obj.yummyness()
print(banana_obj)
        