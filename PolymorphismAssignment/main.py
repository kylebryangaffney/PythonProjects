# Parent class represents a generic musical instrument containing traits common to ALL instruments.

class Instrument:
    # The constructor with default arguments
    def __init__(self, brand="Unknown", model="Unknown", year_made=None):
        self.brand = brand
        self.model = model
        self.year_made = year_made

    # Setter method allows data entry after the object is created.
    def set_information(self):
        self.brand = input("Please enter the brand of the instrument: ")
        self.model = input("Please enter the model of the instrument: ")
        self.year_made = input("Please enter the year the instrument was made: ")

    # Getter method formats the object's current attribute data into a string
    def get_information(self):
        msg = f"\nBrand: {self.brand}\nModel: {self.model}\nYear Made: {self.year_made}\n"
        return msg



# Child class: String

class String(Instrument):
    # The constructor re-declares the parent's parameters and adds new ones.
    def __init__(self, brand="Unknown", model="Unknown", year_made=None, number_of_strings=4, is_fretted=False):
        self.brand = brand
        self.model = model
        self.year_made = year_made
        # String-specific attributes
        self.number_of_strings = number_of_strings
        self.is_fretted = is_fretted

    # Overrides the parent's set_information method to set string-specific data
    def set_information(self):
        self.brand = input("Please enter the brand of the instrument: ")
        self.model = input("Please enter the model of the instrument: ")
        self.year_made = input("Please enter the year the instrument was made: ")
        self.number_of_strings = input("Please enter the number of strings: ")
        # Logic to convert a string input (y/n) into a Boolean (True/False)
        is_fretted_answer = input("Is the instrument fretted? (y/n) ").lower()
        self.is_fretted = True if is_fretted_answer == "y" else False

    # Overriding get_information to include the new string-specific data.
    def get_information(self):
        # We build on top of the base from the original
        msg = f"\nBrand: {self.brand}\nModel: {self.model}\nYear Made: {self.year_made}\n"
        msg += f"Number of Strings: {self.number_of_strings}\nFretted: {self.is_fretted}\n"
        return msg


# Child class: Wind

class Wind(Instrument):
    def __init__(self, brand="Unknown", model="Unknown", year_made=None, key="Bb", needs_reed=False):
        self.brand = brand
        self.model = model
        self.year_made = year_made
        # Wind-specific attributes
        self.key = key
        self.needs_reed = needs_reed

    # Overriding set_information to gather wind-specific attributes
    def set_information(self):
        self.brand = input("Please enter the brand of the instrument: ")
        self.model = input("Please enter the model of the instrument: ")
        self.year_made = input("Please enter the year the instrument was made: ")
        self.key = input("Please enter the instrument's key: ")
        reed_answer = input("Does the instrument use a reed? (y/n) ").lower()
        self.needs_reed = True if reed_answer == "y" else False

    # Overriding get_information to display wind-specific information
    def get_information(self):
        msg = f"\nBrand: {self.brand}\nModel: {self.model}\nYear Made: {self.year_made}\n"
        msg += f"Key: {self.key}\nUses Reed: {self.needs_reed}\n"
        return msg


# --- Main Block ---
if __name__ == "__main__":
    # Create an instance of the String child class.
    # Because of our defaults in constructor, we choose to start with an empty object
    print("--- String Instrument Guitar ---")
    guitar = String()
    guitar.set_information() # Interactive update of guitar attributes

    # Create an instance of the Wind child class.
    print("--- Wind Instrument Saxophone ---")
    sax = Wind()
    sax.set_information() # Interactive update of 'sax' attributes

    # Printout the final state of both objects.
    print(guitar.get_information())
    print(sax.get_information())
