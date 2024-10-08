from menu import book_operations


def manage_books(library_system):

    while True:
        book_operations()
        book_choice = input("Select an option: ")
        if book_choice == '1':
            title = input("Enter a book title: ")
            author = input("Enter the author: ")
            genre = input("Enter the genre: ")
            pub_date = input("Enter publication date: ")
            library_system.add_book(title, author, genre, pub_date)
            print("Book added.")
        elif book_choice == '2':
            library_id = input("Enter user library ID: ")
            book_title = input("Enter book title to return: ")
            print(library_system.return_book(library_id, book_title))
        elif book_choice == '4':
            search_title = input("Enter a book title to search: ")
            book = library_system.find_book(search_title)
            if book:
                print(f"Book found: {book.details()}")
            else:
                print("Book not found.")
        elif book_choice == '5':
            print("\nList of all books: ")
            library_system.display_books()
        elif book_choice == '6':
            break