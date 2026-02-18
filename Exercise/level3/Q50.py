'''Build a contact manager that stores contacts (name, phone, email) in a CSV file. Support
add, search by name, delete, and list-all via a simple numbered menu. Persist data between
runs.'''



import csv
import os

CSV_FILE = "contacts.csv"

def load_contacts():
    contacts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            contacts = list(reader)
    return contacts

def save_contacts(contacts):
    with open(CSV_FILE, mode="w", newline="") as f:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    results = [c for c in contacts if name in c["name"].lower()]
    if results:
        for c in results:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("No contact found with that name.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()
    new_contacts = [c for c in contacts if name not in c["name"].lower()]
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print(f"Deleted contact(s) with name containing '{name}'")
        return new_contacts
    else:
        print("No matching contact to delete.")
        return contacts

def list_contacts(contacts):
    if contacts:
        for c in contacts:
            print(f"Name: {c['name']}, Phone: {c['phone']}, Email: {c['email']}")
    else:
        print("No contacts available.")

def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            contacts = delete_contact(contacts)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Manager")
            break
        else:
            print("Invalid choice. Please select 1-5")


if __name__ == "__main__":
    main()
