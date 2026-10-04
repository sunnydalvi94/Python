class Animal:
    def eat():
        return ('it is eating')                                                   

class Dog(Animal):
    def bark():
        return ('it is barking')


print(Dog.eat())
print(Dog.bark())

