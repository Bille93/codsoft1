import json

# Define the file path for the JSON data
DATA_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_contacts(contacts):
    """Save contacts to a JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    """Add a new contact"""
    contact = {}
    contact['name'] = input("Enter name: ")
    contact['phone'] = input("Enter phone number: ")
    contact['email'] = input("Enter email: ")
    contact['address'] = input("Enter address: ")
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts(contacts):
    """View all contacts"""
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    """Search contacts by name or phone number"""
    query = input("Enter name or phone number to search: ")
    results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            results.append(contact)
    if not results:
        print("No matching contacts found.")
    else:
        print("Search Results:")
        for index, contact in enumerate(results, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def update_contact(contacts):
    """Update an existing contact"""
    view_contacts(contacts)
    index = int(input("Enter the index of the contact to update: ")) - 1
    if 0 <= index < len(contacts):
        contact = contacts[index]
        contact['name'] = input(f"Enter new name (current: {contact['name']}): ")
        contact['phone'] = input(f"Enter new phone number (current: {contact['phone']}): ")
        contact['email'] = input(f"Enter new email (current: {contact['email']}): ")
        contact['address'] = input(f"Enter new address (current: {contact['address']}): ")
        save_contacts(contacts)
        print("Contact updated successfully.")
    else:
        print("Invalid index.")

def delete_contact(contacts):
    """Delete an existing contact"""
    view_contacts(contacts)
    index = int(input("Enter the index of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        del contacts[index]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Invalid index.")

def show_menu():
    """Display the menu options"""
    print("\nContact Book Application")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    """Main function"""
    contacts = load_contacts()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
