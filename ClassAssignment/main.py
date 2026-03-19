class Animal:
    name = "Unknown Name"
    vertebrate = False
    habitat = "water"

class Arachnid(Animal):
    warm_blooded = False
    number_of_legs = 8
    habitat = "land"

class Bird(Animal):
    warm_blooded = True
    vertebrate = True
    number_of_legs = 2
    habitat = "land"
    can_fly = True        # can be overridden for penguins 
    has_feathers = True