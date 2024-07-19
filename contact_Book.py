import json

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

#Create a contact book to store data
class ContactBook:
    def __init__(self):
        self.contacts = []

#To add contacts 
    def add_contacts(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print("Contact added successfully.")

#To view contacts
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")

#To search contacts
    def search_contacts(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                self.display_contact(contact)

#To update contacts
    def update_contact(self, name, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

#To delete contacts
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

#To displays contacts details
    def display_contact(self, contact):
        print(f"Name: {contact.name}")
        print(f"Phone: {contact.phone}")
        print(f"Email: {contact.email}")
        print(f"Address: {contact.address}")

def save_contacts_to_file(contact_manager, filename='contacts.json'):
    with open(filename, 'w') as file:
        json_contacts = [{'name': c.name, 'phone': c.phone, 'email': c.email, 'address': c.address} for c in contact_manager.contacts]
        json.dump(json_contacts, file)

def load_contacts_file(contact_manager, filename='contacts.json'):
    try:
        with open(filename, 'r') as file:
            json_contacts = json.load(file)
            for c in json_contacts:
                contact_manager.add_contact(c['name'], c['phone'], c['email'], c['address'])
    except FileNotFoundError:
        print("No contacts file found.")

def main():
    contact_manager = ContactBook()
    load_contacts_file(contact_manager)
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_manager.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            contact_manager.search_contact(search_term)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            new_name = input("Enter new name (): ")
            new_phone = input("Enter new phone (): ")
            new_email = input("Enter new email (): ")
            new_address = input("Enter new address (): ")
            contact_manager.update_contact(name, new_name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '6':
            save_contacts_to_file(contact_manager)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
