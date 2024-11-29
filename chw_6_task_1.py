from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        # print(value)

    def __str__(self):
        # print(str(self.value))
        return str(self.value)

class Name(Field):
    pass
    
class Phone(Field): 
    def __init__(self, value):
        super().__init__(value)
        if len(self.value) != 10:
            raise ValueError
        else:
            self.value = value

    def __str__(self):
        return str(self.value)

class Record:
    # contact = {}
    

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        # Record.contact.update({self.name.value: self})
        # Record.contact[self.name.value] = f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
        # print(Record.contact)
        # print(Name(name))
        

    
    def add_phone(self, value):
        self.phones.append(Phone(value))
        # print(self.phones)

    def remove_phone(self, value):
        self.phones = [p for p in self.phones if p.value != value]

    def edit_phone(self, old_value, new_value):
        self.phones = [p if p.value != old_value else Phone(new_value) for p in self.phones]
        
        


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
  
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        
        return self.data.get(name)

    """"Треба знайти об'єкт Record"""

    # def __str__(self):
    #     return str(self.data)

        

        
# Створення нової адресної книги
book = AddressBook()

#     # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# john_record.add_phone("+381234567890")


# #     # Додавання запису John до адресної книги
book.add_record(john_record)

print(book)

# # #     # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")

# # print(Record("John"))
# # print(Phone.phone_list)

# print(john_record)
# book.add_record(jane_record)

# #     # Виведення всіх записів у книзі
# # print(book)
# #     # Знаходження та редагування телефону для John
john = book.find("John")
print(john)
# john_record.remove_phone("5555555555")
# jane = book.find("Jane")
# # bob = book.find("Bob")
# # print(bob)

# print(john)
john.edit_phone("1234567890", "1112223333")
print(john)
# # print(john_record)
# print(book)
# # x = Record.contact["John"]
# # print(x)

# #     john.edit_phone("1234567890", "1112223333")

# # print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# #     # Пошук конкретного телефону у записі John
# #     found_phone = john.find_phone("5555555555")
# #     print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# #     # Видалення запису Jane
# #     book.delete("Jane")

