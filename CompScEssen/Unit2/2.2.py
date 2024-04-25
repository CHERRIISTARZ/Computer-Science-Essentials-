#Car Maker 
#This code demonstrates how Object-Oriented programming (OOP) works
#In this case, you are building cars. The cars are the object
#The car(object) has properties (doors, color, wheel size, horsepower, etc.)
#Since each car is a different object, we use the code below to create as many cars as we want

class Car:
    def __init__(self, numOfDoors, color, horsePower, numOfWheels, colorOfWindows):
        #Update this code to include your two new properties from below
        self.numOfDoors = numOfDoors
        self.color = color
        self.horsePower = horsePower
        self.numOfWheels = numOfWheels
        self.colorOfWindows = colorOfWindows
        print("Car Successfully created!")

print("Welcome to the custom car maker app")
print()

#Add two more properties for a car object below. 
doors = input("How many doors would you like your car to have? ")
color = input("What color would you like your car to be? ")
hp = input("How much horsepower would you like your car to have? ")
wheels = input("How many wheels would you like your car to have?")
windowColor = input("What color would you like you car's windows to be?")

#update this code below to show your two new properties from above
c1 = Car(doors, color, hp, wheels, windowColor)
print("Your car will have", c1.numOfDoors, "doors .")
print("It will be the color", c1.color,".")
print("It will have", c1.horsePower, "horsepower .")
print("It will have", c1.numOfWheels, "wheels")
print("and will have the window color", c1.colorOfWindows, ".")
