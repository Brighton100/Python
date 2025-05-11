# Base Class: Superhero
class Superhero:
    def __init__(self, name, power, strength, origin):
        # Constructor to initialize superhero attributes
        self.name = name
        self.power = power
        self.strength = strength
        self.origin = origin

    # Method to demonstrate the use of power
    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

    # Method to show superhero's strength
    def show_strength(self):
        print(f"{self.name} has {self.strength} strength!")

    # Method to introduce the superhero
    def introduce(self):
        print(f"Hi, I'm {self.name}, from {self.origin}!")

# Subclass: Superman (Inherits from Superhero)
class Superman(Superhero):
    def __init__(self, name, strength, origin, speed):
        # Calling the constructor of the parent class (Superhero)
        super().__init__(name, "Super Strength and Flight", strength, origin)
        self.speed = speed  # Superman's speed as an additional attribute

    # Overriding the use_power method to add a unique feature
    def use_power(self):
        print(f"{self.name} uses super speed and flies at {self.speed} mph!")

# Create a Superhero object
hero = Superhero("Iron Man", "Repulsor Beam", 75, "Earth")
hero.introduce()
hero.use_power()
hero.show_strength()

# Create a Superman object (inherits from Superhero)
superman = Superman("Superman", 100, "Kryptonian Planet", 500)
superman.introduce()
superman.use_power()
superman.show_strength()
