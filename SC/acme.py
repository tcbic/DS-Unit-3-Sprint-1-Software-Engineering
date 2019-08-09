import random

#Define the class Product.
class Product:
    """Create the class Product to better organize the goods 
    and sales of ACME."""
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)
    
    #Add methods.
    def stealability(self):
        """Calculates price divided by weight and returns a message."""
        ratio = self.price/self.weight
        if ratio < .5:
            return "Not so stealable..."
        elif ratio >= .5 and ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """Calculates flammability times weight and returns a message."""
        prob = self.flammability * self.weight
        if prob < 10:
            return "...fizzle."
        elif prob >= 10 and prob < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"

#Define inheritance.
class BoxingGlove(Product):
    """Create a subclass of Product called BoxingGlove."""
    def __init__(self, name):
        super().__init__(name)
        self.weight = 10
    def explode(self):
        return "...it's a glove."
    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight <= 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
