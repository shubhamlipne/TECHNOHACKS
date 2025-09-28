import os
import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from a JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    """Add a new contact to the contact book."""
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("⚠️ Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()
    if not phone:
        print("⚠️ Phone number cannot be empty.")
        return

    contacts[name] = phone
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added.")


def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"🔍 {name}: {contacts[name]}")
    else:
        print("❌ Contact not found.")


def delete_contact(contacts):
    """Delete a contact by name."""
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted.")
    else:
        print("❌ Contact not found.")


def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("📭 No contacts available.")
    else:
        print("\n📒 Contact List:")
        for name, phone in contacts.items():
            print(f"- {name}: {phone}")


def main():
    """Main application loop."""
    contacts = load_contacts()

    while True:
        print("\n📌 Contact Book Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1–5.")


if __name__ == "__main__":
    main()
