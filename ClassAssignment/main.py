# The Base Class
# Archetype for other child animals.
class Animal:
    def __init__(self, name="Unknown Name", vertebrate=False, habitat="water"):
        # Set the default values if none are supplied
        self.name = name
        self.vertebrate = vertebrate
        self.habitat = habitat

# Inheritance: Arachnid "is an" Animal
class Arachnid(Animal):
    warm_blooded = False
    number_of_legs = 8
    # We change the default habitat from "water" to "land".
    habitat = "land"

# Inheritance: Bird "is an" Animal
class Bird(Animal):
    # Overriding parent traits, birds are vertebrates
    warm_blooded = True
    vertebrate = True
    
    # Adding new bird specific attributes
    number_of_legs = 2
    habitat = "land"
    can_fly = True        # Can be overridden for birds like Penguins
    has_feathers = True