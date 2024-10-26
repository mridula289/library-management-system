import os

# Define file paths
BOOKS_FILE = 'books.txt'
STAFF_FILE = 'staff.txt'
INCOME_FILE = 'income.txt'

# Define delimiter to separate details in the files
DELIMITER = '|'

# Function to add a book to the collection
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    year = input("Enter the year of publication: ")
    price = float(input("Enter the book price: "))
    quantity = int(input("Enter the quantity available: "))

    # Create a string with book details separated by the delimiter
    book_details = title + DELIMITER + author + DELIMITER + isbn + DELIMITER + year + DELIMITER + str(price) + DELIMITER + str(quantity) + '\n'



    # Open the file in append mode and write the book details
    with open(BOOKS_FILE, 'a') as file:
        file.write(book_details)

    print("Book added successfully!")

# Function to sell a book and update total income
def sell_book():
    sell_title = input("Enter the title of the book you want to sell: ").strip()
    quantity_to_sell = int(input("Enter the quantity to sell: "))

    # Read all books from the file
    books = []
    with open(BOOKS_FILE, 'r') as file:
        for line in file:
            books.append(line.strip())

    # Find the book to sell
    book_found = False
    total_sale = 0  # Track the total sale for this transaction
    for i, book in enumerate(books):
        try:
            title, author, isbn, year, price, quantity = book.split(DELIMITER)
            price = float(price)
            quantity = int(quantity)
            
            if sell_title.lower() == title.lower():
                if quantity >= quantity_to_sell:
                    # Update quantity and calculate the sale amount
                    quantity -= quantity_to_sell
                    total_sale = price * quantity_to_sell
                    
                    # Update book details in the list
                    books[i] = title + DELIMITER + author + DELIMITER + isbn + DELIMITER + year + DELIMITER + price + DELIMITER + quantity

                    
                    book_found = True
                    print("Sold {} copies of '{}'. Remaining quantity: {}".format(quantity_to_sell, title, quantity))
                    print("Total sale amount: ${}".format(total_sale))

                    
                    # Update total income
                    update_total_income(total_sale)
                    
                    break
                else:
                    print("Insufficient quantity available to sell. Only {} copies available.".format(quantity))

                    return
        except ValueError:
           print("Skipping line due to incorrect format: {}".format(book))

        continue
    
    if not book_found:
        print("No book found with title '{}'.".format(sell_title))


    # Write the updated books back to the file
    with open(BOOKS_FILE, 'w') as file:
        file.write('\n'.join(books) + '\n')

# Function to update total income from sales
def update_total_income(sale_amount):
    total_income = 0.0
    
    # Read existing total income from file
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, 'r') as file:
            total_income = float(file.read().strip())
    
    # Update the total income
    total_income += sale_amount
    
    # Write the new total income back to the file
    with open(INCOME_FILE, 'w') as file:
        file.write(str(total_income))

    
    print("Updated total income: $" + "{:.f}".format(total_income))


# Function to search for a book in the collection
def search_book():
    search_query = input("Enter the title, author, or ISBN of the book you want to search for: ").strip().lower()

    found_books = []
    with open(BOOKS_FILE, 'r') as file:
        for line in file:
            book_details = line.strip()
            try:
                title, author, isbn, year, price, quantity = book_details.split(DELIMITER)
                
                # Check if search query matches any book details
                if (search_query in title.lower() or
                    search_query in author.lower() or
                    search_query in isbn)
                    found_books.append(book_details)

            except ValueError:
                print("Skipping line due to incorrect format: " + line.strip())

                continue

    # Print the results
    if found_books:
        print("\nBooks found:")
        for book in found_books:
            title, author, isbn, year, price, quantity = book.split(DELIMITER)
            print("Title: {}, Author: {}, ISBN: {}, Year: {}, Price: ${}, Quantity: {}".format(title, author, isbn, year, price, quantity))

    else:
        print("No books found.")

# Function to delete a book from the collection
def delete_book():
    delete_title = input("Enter the title of the book you want to delete: ").strip().lower()

    # Read all books from the file
    books = []
    with open(BOOKS_FILE, 'r') as file:
        for line in file:
            books.append(line.strip())

    # Find the book to delete
    book_found = False
    for i, book in enumerate(books):
        try:
            title, author, isbn, year, price, quantity = book.split(DELIMITER)
            if delete_title in title.lower():
                books.pop(i)
                book_found = True
                print("Book titled '" + title + "' deleted successfully!")

                break
        except ValueError:
            print("Skipping line due to incorrect format: " + line.strip())

            continue
    
    if not book_found:
        print("No book found with title '" + delete_title + "'.")


    # Write the remaining books back to the file
    with open(BOOKS_FILE, 'w') as file:
        file.write('\n'.join(books) + '\n')

# Function to view all available books
def view_books():
    if not os.path.exists(BOOKS_FILE):
        print("No books found.")
        return

    # Open the file in read mode
    with open(BOOKS_FILE, 'r') as file:
        print("\nAvailable Books:")
        for line in file:
            try:
                title, author, isbn, year, price, quantity = line.strip().split(DELIMITER)
                print("Title: " + title + ", Author: " + author + ", ISBN: " + isbn + ", Year: " + year + ", Price: $" + str(price) + ", Quantity: " + str(quantity))

            except ValueError:
                print("Skipping line due to incorrect format: " + line.strip())

                continue

# Function to add a staff member
def add_staff():
    staff_id = input("Enter the staff ID: ")
    name = input("Enter the staff name: ")
    position = input("Enter the staff position: ")

    # Create a string with staff details separated by the delimiter
    staff_details = staff_id + DELIMITER + name + DELIMITER + position + '\n'


    # Open the file in append mode and write the staff details
    with open(STAFF_FILE, 'a') as file:
        file.write(staff_details)

    print("Staff member added successfully!")

# Function to view staff details
def view_staff():
    if not os.path.exists(STAFF_FILE):
        print("No staff members found.")
        return

    # Open the file in read mode
    with open(STAFF_FILE, 'r') as file:
        print("\nStaff Members:")
        for line in file:
            try:
                staff_id, name, position = line.strip().split(DELIMITER)
                print("Staff ID: " + str(staff_id) + ", Name: " + name + ", Position: " + position)

            except ValueError:
                print("Skipping line due to incorrect format: " + line.strip())

                continue

# Function to view total income
def view_total_income():
    total_income = 0.0
    
    if os.path.exists(INCOME_FILE):
        with open(INCOME_FILE, 'r') as file:
            total_income = float(file.read().strip())
    
    print("\nTotal Income: $" + "{:.f}".format(total_income))


# Main function to handle user interaction
def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. Sell Book")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. View Available Books")
        print("6. Add Staff")
        print("7. View Staff")
        print("8. View Total Income")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            sell_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            view_books()
        elif choice == '6':
            add_staff()
        elif choice == '7':
            view_staff()
        elif choice == '8':
            view_total_income()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
main()
