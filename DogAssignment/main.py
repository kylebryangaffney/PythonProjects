class Dog:
    def __init__(self, name):
        self._num_of_teeth = 42      # Protected
        self.__name = name           # Private

    # Getter/setter for protected teeth attribute
    def get_num_of_teeth(self):
        return self._num_of_teeth

    def set_num_of_teeth(self, new_num_of_teeth):
        self._num_of_teeth = new_num_of_teeth

    # Getter for private name attribute, you could make a setter also, but that does not seem necessary
    def get_name(self):
        return self.__name



# Create object
dexter = Dog("Dexter")

# Get protected teeth
dexter_teeth = dexter.get_num_of_teeth()
print(dexter_teeth)           # Output: 42

# set protected teeth
dexter.set_num_of_teeth(32)
print(dexter.get_num_of_teeth())  # Output: 32

# Getting private name with getter
print(dexter.get_name())      # Output: Dexter

