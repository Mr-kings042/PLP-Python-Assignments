class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_info(self):
        return f"Superhero: {self.name}\nPower: {self.power}\nCity: {self.city}"

# Creating instances of Superhero
hero1 = Superhero("Spider-Man", "Web-slinging", "New York")
hero2 = Superhero("Batman", "Martial Arts", "Gotham")

# Displaying superhero information
print(hero1.display_info())
print(hero2.display_info())


# polymorphism
class Animal:
    def move(self):
      pass

class Dog(Animal):
    def move(self):
        return "Running"

class Cat(Animal):
    def move(self):
        return "Jumping"

class Bird(Animal):
    def move(self):
        return "Flying"

# Function to demonstrate polymorphism
def animal_movement(animal):
    print(f"The {animal.__class__.__name__} is {animal.move()}.")

# Creating instances of each animal
dog = Dog()
cat = Cat()
bird = Bird()

# Demonstrating polymorphism
animal_movement(dog)   
animal_movement(cat)   
animal_movement(bird)


class Vehicle:
    def move(self):
        pass  # Base class does not implement move()

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

def demonstrate_polymorphism(objects):
    for obj in objects:
        print(obj.move())

# Create instances of animals and vehicles
car = Car()
plane = Plane()

# List of instances
objects = [ car, plane]

# Demonstrate polymorphism
demonstrate_polymorphism(objects)