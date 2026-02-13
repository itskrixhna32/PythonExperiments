#6.	Create a contact book where users can store, search, update, and delete contacts. Use dictionary for storing contacts.
contacts = {}
def add_contact(name, phone):
    contacts[name] = phone
def search_contact(name):
    return contacts.get(name, "Contact not found")
def update_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "Contact not found"
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        return "Contact deleted"
    else:
        return "Contact not found"
while True:
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
        print("Contact added successfully.")
    elif choice == '2':
        name = input("Enter contact name to search: ")
        print(search_contact(name))
    elif choice == '3':
        name = input("Enter contact name to update: ")
        phone = input("Enter new phone number: ")
        print(update_contact(name, phone))
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        print(delete_contact(name))
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
        