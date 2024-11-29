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

    def edit_phone(self, old_phone, new_phone):
        self.phones = [p if p.value != old_phone else Phone(new_phone) for p in self.phones]

    def find_phone(self, phone):
        return Phone(phone) if phone in (p.value for p in self.phones) else None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
  
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name) -> Record:
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]


    def str(self):
        pass
        # return f"Record {} {}" 

        

        
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# john_record.add_phone("+381234567890")
book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)
john = book.find("John")
# print(john)

john.edit_phone("1234567890", "1112223333")
# print(john)

found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
print(book)

