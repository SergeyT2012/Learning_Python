
class Human:
    def __init__(self, name, age, pin):
        self.__age = age
        self.__name = name
        self.pin = pin
        with open("name_age.txt", "w") as file:
            file.write(
                f"Old Name: {self.__name}, Old Age: {self.__age}\n")
    def check_pin(self,):
        input_pin = int(input("Enter Pin: "))
        if input_pin == person.pin:
            person.__age = int(input("Enter new age: "))
            person.__name = input("Enter new name: ")
            with open("skibidi.txt", "a") as file:
                file.write(f"New Name: {person.__name}, New Age: {person.__age}")
        else:
            print("nuh uh")
person = Human('John', 89, 1111)
person.check_pin()