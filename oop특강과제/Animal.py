class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("짖는소리")
        
class Dog(Animal):
    def speak(self):
        print("왈왈")
        
class Cat(Animal):
    def speak(self):
        print("냥냥")
        
