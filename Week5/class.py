class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  # Output: blue
print(car2.model)  # Output: SUV