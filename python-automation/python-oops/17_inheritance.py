class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

#creating object
d = Dog()
d.speak()  # Inherited method from Animal
d.bark()   # Method from Dog class