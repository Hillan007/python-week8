class Vehicle:
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed
    
    def move(self):
        pass
    
    def get_info(self):
        return f"{self.color} {self.name} with max speed of {self.max_speed} km/h"

class Car(Vehicle):
    def __init__(self, name, color, max_speed, num_wheels):
        super().__init__(name, color, max_speed)
        self.num_wheels = num_wheels
    
    def move(self):
        return f"🚗 The {self.color} {self.name} is driving on {self.num_wheels} wheels"

class Plane(Vehicle):
    def __init__(self, name, color, max_speed, max_altitude):
        super().__init__(name, color, max_speed)
        self.max_altitude = max_altitude
    
    def move(self):
        return f"✈️ The {self.color} {self.name} is flying at {self.max_altitude} feet"

class Boat(Vehicle):
    def __init__(self, name, color, max_speed, water_type):
        super().__init__(name, color, max_speed)
        self.water_type = water_type
    
    def move(self):
        return f"🚢 The {self.color} {self.name} is sailing in {self.water_type} waters"

# Testing the vehicles
if __name__ == "__main__":
    # Create different vehicles
    car = Car("Mercedes", "Silver", 250, 4)
    plane = Plane("Boeing 747", "White", 920, 35000)
    boat = Boat("Yacht", "Blue", 70, "ocean")
    
    # Store vehicles in a list to demonstrate polymorphism
    vehicles = [car, plane, boat]
    
    # Display info and movement for each vehicle
    for vehicle in vehicles:
        print(vehicle.get_info())
        print(vehicle.move())
        print()