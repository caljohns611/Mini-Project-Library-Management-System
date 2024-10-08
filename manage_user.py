from menu import user_operations


def manage_users(library_ststem):
    
    while True:
        user_operations()
        user_choice = input("Select an option: ")
        if user_choice == '1':
            name = input("Enter user name: ")
            library_id = input("Enter user library ID: ")
            library_ststem.add_user(name, library_id)
            print("User added.")
        elif user_choice == '2':
            library_id = input("Enter user library ID to view details: ")
            user = library_ststem.find_user(library_id)
            if user:
                print(user.details())
            else:
                print("User not found.")
        elif user_choice == '3':
            print("\nList of all users: ")
            library_ststem.display_users()
        elif user_choice == '4':
            break