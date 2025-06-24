class Bird:
    def make_sound(self):
        print("Bird sound")

class Parrot(Bird):
    def make_sound(self):
        print("Parrot says hello")

class Crow(Bird):
    def make_sound(self):
        print("Caw Caw")

# Using polymorphism
for bird in (Parrot(), Crow()):
    bird.make_sound()