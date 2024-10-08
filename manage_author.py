from menu import author_operations


def manage_authors(library_system):

    while True:
        author_operations()
        author_choice = input("Select an option: ")
        if author_choice == '1':
            author_name = input("Enter author name: ")
            biography = input("Enter author biography: ")
            library_system.add_author(author_name, biography)
            print("Author added.")
        elif author_choice == '2':
            author_name = input("Enter author name to view details: ")
            author = library_system.find_author(author_name)
            if author:
                print(author.details())
            else:
                print("Author not found.")
        elif author_choice == '3':
            print("\nList of all authors: ")
            library_system.display_authors()
        elif author_choice == '4':
            break