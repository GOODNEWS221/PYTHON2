

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


    def __repr__(self):
        return f"{self.name}, {self.phone}, {self.email}"

class ContactBook:
    def __init__(self):
        self.book = []
    
    def add_contact(self):
        print("do you want to add a new contact")
        name = input("Your name: ")
        phone = input("Your phone: ")
        email = input("Your email: ")
        
        if name != "":
            contact = Contact(name, phone, email)
            self.book.append(contact)
            
            print(f"✅ Contact added: {contact}")
    
    def delete_contact(self):
        print("do you want to delete a contact")
        delete = input("Contact to be deleted: ")

        for contact in self.book:
            if contact.name.lower() == delete.lower():
                self.book.remove(contact)
                print(f"Contact list: {contact}")
                break
        else:
            print("not found: 404")

        

    def view_contact(self):
        if not self.book:
            print("no contact available")
        else:
            for idx, contact in enumerate (self.book, start=1):
                print(f"{idx}. {contact}")

        


   

def click():
    A = ContactBook()
    while True:
        print("Welcome to my contact list")
        print("1. add contact")
        print("2. delete contact")
        print("3. view contact")
        print("4 exit")

        user_option = input("kindly select an option: ")
        if user_option == "1":
            A.add_contact()
        elif user_option == "2":
            A.delete_contact()
        elif user_option == "3":
            A.view_contact()
        elif user_option == "4":
            print("Goodbye, see you next time")
            break
        else:
            print("invalid choice")


        

    


click()



