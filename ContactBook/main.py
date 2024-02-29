class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number
        print(f"Contact '{name}' added successfully.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact found: {name}: {self.contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("Contact list is empty.")

    def update_contact(self, name, new_number):
        if name in self.contacts:
            self.contacts[name] = new_number
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")


def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View Contact List")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            number = input("Enter contact number: ")
            contact_book.add_contact(name, number)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            contact_book.view_contacts()
        elif choice == "5":
            name = input("Enter contact name to update: ")
            new_number = input("Enter new contact number: ")
            contact_book.update_contact(name, new_number)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
