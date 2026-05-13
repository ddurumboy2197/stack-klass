class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Mammal(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def nurse(self):
        print(f"{self.name} is nursing its young.")


class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Canis lupus familiaris")
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Felis catus")
        self.breed = breed

    def meow(self):
        print(f"{self.name} is meowing.")


dog = Dog("Rex", 3, "Golden Retriever")
dog.eat()
dog.sleep()
dog.nurse()
dog.bark()

cat = Cat("Whiskers", 2, "Siamese")
cat.eat()
cat.sleep()
cat.nurse()
cat.meow()
```

Kodda ikkita klass, `Dog` va `Cat`, `Mammal` klassidan merosxo'rlik qiladi. `Mammal` klassi `Animal` klassidan merosxo'rlik qiladi. Bu klasslarning har biri o'ziga xos xususiyatlar va metodlarga ega.
