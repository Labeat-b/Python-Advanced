class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello I am {self.name} and I am {self.age} years old.")

person1 = Person("John",  25)
person2 = Person("Doe", 23)

person1.greet()
person2.greet()