import re # Imports regex.

contacts = {"1234567890": {"Name": "John Smith", "Email": "johnsmith@gmail.com"}} # Our dictionary containing our contacts.

def main():
    while True:
        select = input('''
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Quit 
''')
        if select == '1':
            add_new_contact()
        elif select == '2':
            edit_contact()
        elif select == '3':
            delete_contact()
        elif select == '4':
            search_for_contact()
        elif select == '5':
            print(contacts)
        elif select == '6':
            print("Thank you, have a good day.")
            break
        else:
            print("Please select a valid option")
            continue

def add_new_contact():
    new_contact = {}
    while True:
        try:
            number = input("What is your new contact's phone number? ")
            new_contact_number = re.search(r"\(?\d{3}\)?(\s|-)?\d{3}(\s|-)?\d{4}", number) # Using regex to confirm the user is entering the correct input for a phone number (contains 10 digits, the first 3 digits may or may not be surrounded by parenthesis, and there may or may not be dashes between the first 3 digits and the second 3 digits). The re.search() method is used to search for any matches in the user input to the metacharacters used inside our raw string.
            number = new_contact_number.group().replace('(', '').replace('-', '').replace(')', '').replace(' ', '') # using .replace() to take whatever format the user enters the phone number and converts it to our universal format that we've created (1234567890). The number is assigned to the variable using the .group() method so it appears readable.
            print(number)
            new_contact_name = input("What is your new contact's name? ")
            email = input("What is your new contact's email address? ")
            new_contact_email = re.search(r"[\w.-]+@[\w-]+.[a-z]{2,3}", email) # Checks to make sure the user enters the email in the proper format (includes a username, an @ symbol and ends with .com, .org, etc.)
            new_contact.update({number: {"Name": new_contact_name, "Email": new_contact_email.group()}}) # Updates new_contact with the new number. It also adds the new name and new email address (using .group()) to their indicated keys in our contacts dicitonary.
            contacts.update(new_contact) # Updates our main dicitonary contacts with the new contact.
            print(f"Congratulations! Your new contact {number} {new_contact_name} {new_contact_email.group()} has been added successfully!")
            break
        except:
            continue # Repeating the loop if the user enters an invalid input.

def edit_contact():
    while True:
        try:
            print(contacts)
            change = input("Please select the contact you would like to edit (Q for quit) ").lower()
            if change == 'q':
                break
            elif change in contacts:
                print("Please make the necessary changes to your contact ")
            else:
                print("contact not found")
                continue
            updated_info = input("Would you like to change the number, name, or email? ").lower()
            if updated_info == "number":
                new_number = input("Please enter the new number here ")
                contacts[new_number] = contacts[change] # Adding the new phone number to the outer key in our contacts dicitonary by setting it equal to the change input.  
                del contacts[change] # Deletes the change input keeping our new_number at the outer key inside our contacts dictionary.
                print("Number successfully changed.")
            elif updated_info == "name":
                new_name = input("Please enter the new name here ")
                contacts[change]["Name"] = new_name # Selects the inner key "Name" inside the nested dicitonary of contacts and sets it equal to the value of the new_name input.
                print("Name successfully changed.")
            elif updated_info == 'email':
                new_email = input("Please enter the new email here ")
                contacts[change]["Email"] = new_email # Selects the inner key "Email" inside the nested dicitonary of contacts and sets it equal to the value of the new_email input.
                if contacts[change]["Email"] == new_email:
                    print("Email successfully changed.")
            else:
                print("Invalid entry")
        except:
            continue
    
def delete_contact():
    while True:
        delete = input("Please select the contact you would like to delete ")
        if delete in contacts:
            print(delete)
        else:
            print("Contact not found")
            return
        confirm = input("Are you sure you would like to delete this contact? ")
        if confirm == 'yes':
            del contacts[delete] # Using the del method to delete what is entered in the delete input from the contacts dictionary.
            print(f"Your contact {delete} has been deleted successfully.")
            break
        elif confirm == 'no':
            continue
        else:
            print("Invalid entry")
            continue

def search_for_contact(): # need help with this
    while True:
        try:
            contact_search = input("Search for a phone number here ")
            search_results = re.match(r"\(?\d{3}\)?(\s|-)?\d{3}(\s|-)?\d{4}", contact_search) # Using regex to confirm the user is entering the correct input for a phone number (contains 10 digits, the first 3 digits may or may not be surrounded by parenthesis, and there may or may not be dashes between the first 3 digits and the second 3 digits). The re.match() method is used to confirm if there is match in our contacts dictionary for the user input.
            search_results = search_results.group().replace('(', '').replace('-', '').replace(')', '').replace(' ', '') # using .replace() to take whatever format the user enters the phone number they are searching for and converts it to our universal format that we've created (1234567890). The .group() method is used on to convert the user input to a readable format.
            print(search_results)
            if search_results in contacts:
                print(contacts[search_results]) # Accessing our dicitonary to print out the phone number the user searches for if it is in there.
                break
            else:
                print("Contact not found")
                continue
        except:
            continue
main()