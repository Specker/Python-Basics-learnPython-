# Print a list of all attributes of the given Vehicle object.

class Vehicle:
    name = "UAZ"
    kind = "car"
    color = "Black-ish"
    value = -100.00 # Take it of my hands... 
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

print(dir(Vehicle))