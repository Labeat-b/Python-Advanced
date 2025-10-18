class Dog():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{sound.name} makes this sound: Woof")

class Cat():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{sound.name} makes this sound: Meow")

class Bird():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{sound.name} makes this sound: Chirp")

dog = Dog("Bob")
cat = Cat("Frank")
bird= Bird("John")

for animal in (Dog, Cat, Bird):
    animal.sound()