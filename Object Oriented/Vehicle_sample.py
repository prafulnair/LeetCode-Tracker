from abc import ABC, abstractmethod  # Import ABC for abstract base classes and abstractmethod for defining abstract methods

# Encapsulation and Abstraction
class Vehicle(ABC):  # Abstract base class (ABC) for vehicles
    def __init__(self, make, model):
        self.make = make  # Public attribute for the make of the vehicle
        self.model = model  # Public attribute for the model of the vehicle
        self._fuel = 0  # Protected attribute for fuel, intended for internal use only

    # Abstract Method: Each subclass must implement its own version of this method
    @abstractmethod
    def start_engine(self):
        pass  # Placeholder for the engine start method, to be implemented by subclasses

    # Encapsulation with property decorator: Getter for fuel
    @property
    def fuel(self):
        return self._fuel  # Returns the current fuel level

    # Setter for fuel, which includes validation
    @fuel.setter
    def fuel(self, amount):
        if amount < 0:
            raise ValueError("Fuel amount cannot be negative")  # Ensure fuel amount is non-negative
        self._fuel = amount  # Set the fuel level if validation passes

    # Method to refuel the vehicle, increasing the fuel level
    def refuel(self, amount):
        self.fuel += amount  # Use the setter for fuel to add the amount
        print(f"Vehicle refueled to {self.fuel} liters")  # Print the current fuel level

    # General method to drive the vehicle
    def drive(self):
        if self.fuel > 0:
            print("Vehicle is driving")  # Print that the vehicle is in motion
            self._fuel -= 1  # Reduce fuel by 1 unit
        else:
            print("Out of fuel, please refuel")  # Message for when fuel is insufficient

# Inheritance and Polymorphism: Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)  # Call the superclass (Vehicle) constructor
        self.seats = seats  # Additional attribute for the number of seats in the car

    # Implementation of the abstract method start_engine for Car
    def start_engine(self):
        print("Car engine started")  # Print message indicating the car engine has started

    # Override drive method with specific behavior for Car
    def drive(self):
        if self.fuel > 0:
            print(f"Car with {self.seats} seats is driving")  # Print a message including the number of seats
            self._fuel -= 1  # Reduce fuel by 1 unit
        else:
            print("Car is out of fuel, please refuel")  # Message for low fuel

# Motorcycle class, inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)  # Call the superclass (Vehicle) constructor

    # Implementation of the abstract method start_engine for Motorcycle
    def start_engine(self):
        print("Motorcycle engine started")  # Print message indicating the motorcycle engine has started

    # Override drive method with specific behavior for Motorcycle
    def drive(self):
        if self.fuel > 0:
            print("Motorcycle is driving")  # Print a message for motorcycle driving
            self._fuel -= 1  # Reduce fuel by 1 unit
        else:
            print("Motorcycle is out of fuel, please refuel")  # Message for low fuel

# Interface (using an abstract class) to enforce that subclasses must implement charge_battery
class Electric(ABC):
    @abstractmethod
    def charge_battery(self):
        pass  # Placeholder for battery charging functionality, to be implemented by subclasses

# ElectricCar class, demonstrating multiple inheritance (inherits from Car and Electric)
class ElectricCar(Car, Electric):
    def __init__(self, make, model, seats, battery_level=0):
        super().__init__(make, model, seats)  # Call Car's constructor
        self.battery_level = battery_level  # Additional attribute specific to ElectricCar for battery level

    # Implementation of charge_battery from the Electric interface
    def charge_battery(self):
        self.battery_level = 100  # Set battery level to 100 to represent a full charge
        print("Battery fully charged")  # Print a message indicating the battery is fully charged

    # Override drive method with behavior specific to an electric car
    def drive(self):
        if self.battery_level > 0:
            print(f"Electric Car with {self.seats} seats is driving")  # Print a message for electric car driving
            self.battery_level -= 10  # Reduce battery level by 10 units per drive
        else:
            print("Battery is empty, please charge")  # Message for low battery

# Demonstration of Polymorphism: Function to drive any vehicle (Car, Motorcycle, or ElectricCar)
def vehicle_drive_demo(vehicle):
    vehicle.start_engine()  # Calls the start_engine method for the passed-in vehicle
    vehicle.drive()  # Calls the drive method for the passed-in vehicle

# Main Function to Run the Program
if __name__ == "__main__":
    # Encapsulation example
    print("Creating a Car object...")
    my_car = Car("Toyota", "Camry", 5)  # Create a Car object
    my_car.refuel(10)  # Refuel the car
    print(f"Fuel level: {my_car.fuel}")  # Print the current fuel level

    # Demonstrate Inheritance and Polymorphism
    print("\nDemonstrating Inheritance and Polymorphism with Car and Motorcycle:")
    vehicle_drive_demo(my_car)  # Pass Car to the vehicle_drive_demo function
    my_bike = Motorcycle("Harley", "Street 750")  # Create a Motorcycle object
    vehicle_drive_demo(my_bike)  # Pass Motorcycle to the vehicle_drive_demo function

    # Demonstrate Interface and Multiple Inheritance with ElectricCar
    print("\nCreating an Electric Car (multiple inheritance example):")
    my_electric_car = ElectricCar("Tesla", "Model S", 5)  # Create an ElectricCar object
    my_electric_car.charge_battery()  # Charge the electric car's battery
    vehicle_drive_demo(my_electric_car)  # Pass ElectricCar to the vehicle_drive_demo function
