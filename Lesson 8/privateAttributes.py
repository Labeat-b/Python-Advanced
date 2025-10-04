class MyClass:
    def __init__(self):
        self.__private_varibale = "This is a private variable"
    def __private_method(self):
        print("This is a private method")

my_class = MyClass()

#Error attributes
print(my_class.__private_variable)
my_class.__private_method