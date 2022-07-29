class MyClass:
    pass


class AnotherClass:
    pass


first = MyClass()
print(first)
first.var = "A variable"

print(first.var)


class MyClass:
    var = "From the class"


first = MyClass()
second = MyClass()
print(first)
first.var = "A variable"

print(second.var)
print(first.var)


class MyClass:
    def amethod(self):
        pass


my_class = MyClass()

my_class.amethod()


from typing import Self


class Person:
    def __init__(self, name: str) -> None:
        self.__name = name


person1 = Person("Tola")
print(person1._Person__name)


class Person:
    def __init__(self, name: str) -> None:
        self._name = name


    @property
    def name(self):
        print("I love you")
        return self._name


    @name.setter
    def name(self, name):
        print("Setter")
        if "f" in name:
             print("Fuck off")
             return
        self._name = name



person1 = Person("Tola")
person1.name = "Pelumi e"

print(person1.name)







