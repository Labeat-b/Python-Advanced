class MyClass:
    def __init__(self):
        self._protected_varibale = "This is a protected variable"
    def _protected_method(self):
        print("This is a protected method")

my_class = MyClass()

print(my_class._protected_varibale)
my_class._protected_method()