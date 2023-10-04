class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.spec = None

    def get_spec(self):
        return self.spec


class Dog(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Cat(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Bird(Animal):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Pet:
    def fabric(type_c, name, age, spec):
        if type_c == "Dog":
            return Dog(name, age, spec)
        elif type_c == "Cat":
            return Cat(name, age, spec)
        elif type_c == "Bird":
            return Bird(name, age, spec)
        
class Pet1:
    def __new__(cls, type_c, name, age, spec):
        if type_c == "Dog":
            return Dog(name, age, spec)
        elif type_c == "Cat":
            return Cat(name, age, spec)
        elif type_c == "Bird":
            return  Bird(name, age, spec)


pet1 = Dog("Bob", 5, "Jump")
pet2 = Cat("Felix", 3, "Miau")
pet3 = Bird("Own", 4, "Sign")
pet4 = Pet.fabric("Dog", "Jack", 4, "Sleep")
print(type(pet4))
pet5 = Pet.fabric("Cat", "Barsik", 4, "Wow")
print(type(pet5))
pet6 = Pet1('Bird', 'Carl', 23, 'Fiu')
print(type(pet6))


for pet in [pet1, pet2, pet3, pet4, pet5, pet6]:
    print(pet.get_spec())
