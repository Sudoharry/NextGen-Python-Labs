# Contact book program

contacts = {}

def add_contacts():
    name = input ("Enter contact name: ")
    phone = input ("Enter phone number: ")
    contacts[name] = phone
    print (f"Contact for {name} added.")


def view_contacts():
    if contacts:
       print ("\nContacts:")
       for name, phone in contacts.items():
           print(f"{name}:{phone}")
    else:
        print ("No contacts available!")

def search_contacts():
     name = input ("Enter the name to search: ")
     if name in contacts:
         print(f"{name}:{contacts[name]}")
     else:
          print(f"No contact found for {name}.")


while True:
   print ("\n1. Add contacts")
   print ("2. View contacts")
   print ("3. Search contacts")
   print ("4. Exit")


   choice = input ("Search an option (1/2/3/4): ")


   if choice == '1':
      add_contacts()

   elif choice == '2':
       view_contacts()

   elif choice == '3':
       search_contact()

   elif choice == '4':
       print ("Tata bye bye!!")
       break

   else:
       print ("Invalud choice.")
