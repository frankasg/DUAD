class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers(self, person: Person):
        if len(self.passengers) >= self.max_passengers:
            print("El bus está lleno")
            return
        self.passengers.append(person)

    def remove_passengers(self, person: Person):
        if len(self.passengers) == 0:
            print("Ya no hay más pasajeros")
            return
        self.passengers.remove(person)

bus = Bus(3)

person1 = Person("Frank", 38)
bus.add_passengers(person1)

person2 = Person("Eduardo", 78)
bus.add_passengers(person2)

person3 = Person("Gloria", 65)
bus.add_passengers(person3)

person4 = Person("Santiago", 5)
bus.add_passengers(person4)


bus.remove_passengers(person1)
bus.remove_passengers(person2)
bus.remove_passengers(person3)
bus.remove_passengers(person4)
