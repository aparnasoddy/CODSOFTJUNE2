contacts = []

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

def add_contact():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contact = Contact(name, phone_number, email, address)
    contacts.append(contact)
    print("Contact added successfully.")

def view_contact_list():
    print("\nName\t\t\tPhone Number\t\t\tEmail\t\t\tAddress\n")
    for contact in contacts:
        print(f"{contact.name}\t\t\t{contact.phone_number}\t\t\t{contact.email}\t\t\t{contact.address}")

def search_contact():
    search_term = input("\nEnter search term (name or phone number): ")
    found_contacts = []
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
            found_contacts.append(contact)
    if found_contacts:
        print("\nSearch results:")
        for contact in found_contacts:
            print(f"Name: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}\n")
    else:
        print("No matching contacts found.")

def update_contact():
    search_term = input("\nEnter search term (name or phone number) for the contact to update: ")
    found_contact = None
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
            found_contact = contact
            break
    if found_contact:
        print(f"\nFound contact:\nName: {found_contact.name}\nPhone Number: {found_contact.phone_number}\nEmail: {found_contact.email}\nAddress: {found_contact.address}\n")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        found_contact.phone_number = new_phone_number
        found_contact.email = new_email
        found_contact.address = new_address
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    search_term = input("\nEnter search term (name or phone number) for the contact to delete: ")
    found_contact = None
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
            found_contact = contact
            break
    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\nOptions:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact_list()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a valid option.")
