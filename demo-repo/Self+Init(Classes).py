class Person:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age

    def show_details(self):
        print("Person: ", self.name, self.lastname, self.age)

person1=Person("Juan","Perez",10)
person1.show_details()
person1.phone="59888773"
print(person1.phone)

person2=Person("Karla","Gomez",99)
person2.show_details()