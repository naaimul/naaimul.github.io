class Book:
    
    def __init__(self, title, author, category, price, quantity):
        self.title = title
        self.author = author
        self.category = category
        self.price = price
        self.quantity = quantity

    def display_info(self):
        return f"Title: {self.title.title()}, Author: {self.author}, Category: {self.category}, Price: ${self.price:.2f}, Quantity: {self.quantity}"

    def purchase(self):
        
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False


class IslamicBook(Book):
    
    def __init__(self, title, author, category, price, quantity, translation_language):
        super().__init__(title, author, category, price, quantity)
        self.translation_language = translation_language

    def display_info(self):
        
        return super().display_info() + f", Translation Language: {self.translation_language}"


class ScienceBook(Book):
    
    def __init__(self, title, author, category, price, quantity, field_of_study):
        super().__init__(title, author, category, price, quantity)
        self.field_of_study = field_of_study

    def display_info(self):
        
        return super().display_info() + f", Field of Study: {self.field_of_study}"



users = {}
books = []  
reviews = {}


categories = ["Islamic", "Children's", "Science", "Novels"]



def normalize_title(title):
    
    return title.strip().lower()


def register():
    print("\n=== Registration ===")
    username = input("Enter username: ").strip()
    if username in users:
        print("Username already exists! Try logging in.")
        return
    password = input("Enter password: ").strip()
    users[username] = password
    print("Registration successful!")


def login():
    print("\n=== Login ===")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    if users.get(username) == password:
        print("Login successful!")
        return username
    print("Invalid credentials!")
    return None


def add_book():
    print("\n=== Add Book ===")
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        category = input(f"Enter category ({', '.join(categories)}): ").strip()
        if category not in categories:
            raise ValueError("Invalid category!")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        
        if category.lower() == "islamic":
            translation_language = input("Enter translation language: ").strip()
            book = IslamicBook(title, author, category, price, quantity, translation_language)
        elif category.lower() == "science":
            field_of_study = input("Enter field of study: ").strip()
            book = ScienceBook(title, author, category, price, quantity, field_of_study)
        else:
            book = Book(title, author, category, price, quantity)
        
        books.append(book)
        print(f"Book '{title.title()}' added successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def view_books():
    print("\n=== View All Books ===")
    if not books:
        print("No books available.")
        return

    for book in books:
        print(book.display_info())


def search_books():
    print("\n=== Search Books ===")
    query = normalize_title(input("Enter book title or author: "))
    found = False
    for book in books:
        if query in book.title.lower() or query in book.author.lower():
            print(book.display_info())
            found = True
    if not found:
        print("No books found!")


def update_book():
    print("\n=== Update Book ===")
    try:
        title = normalize_title(input("Enter book title to update: "))
        for book in books:
            if book.title.lower() == title:
                print(f"Editing '{book.title.title()}' by {book.author}")
                book.title = input("Enter new title (or press Enter to keep current): ").strip() or book.title
                book.author = input("Enter new author (or press Enter to keep current): ").strip() or book.author
                category = input(f"Enter new category ({', '.join(categories)}) (or press Enter to keep current): ").strip()
                if category:
                    book.category = category if category in categories else book.category
                book.price = float(input("Enter new price (or press Enter to keep current): ").strip() or book.price)
                book.quantity = int(input("Enter new quantity (or press Enter to keep current): ").strip() or book.quantity)
                print("Book updated successfully!")
                return
        print("Book not found!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def delete_book():
    print("\n=== Delete Book ===")
    title = normalize_title(input("Enter book title to delete: "))
    for book in books:
        if book.title.lower() == title:
            books.remove(book)
            print(f"Book '{title.title()}' deleted successfully!")
            return
    print("Book not found!")


def add_review():
    print("\n=== Add Review ===")
    title = normalize_title(input("Enter book title to review: "))
    for book in books:
        if book.title.lower() == title:
            print(f"=== Reviews for '{book.title.title()}' ===")
            if title in reviews:
                for idx, review in enumerate(reviews[title], 1):
                    print(f"{idx}. {review}")
            else:
                print("No reviews yet for this book.")

            add_new = input("Would you like to add a review? (yes/no): ").strip().lower()
            if add_new == "yes":
                review = input(f"Write your review for '{book.title.title()}': ").strip()
                if title not in reviews:
                    reviews[title] = []
                reviews[title].append(review)
                print("Review added successfully!")
            return
    print("Book not found!")

def purchase_book():
    print("\n=== Purchase Book ===")
    title = normalize_title(input("Enter book title to purchase: "))
    for book in books:
        if book.title.lower() == title:
            if book.purchase():
                print(f"Purchase successful! Remaining copies: {book.quantity}")
                delivery_location = input("Enter your delivery location: ").strip()
                print(f"Your book will be delivered to: {delivery_location}")

                # Payment Methods
                print("\n=== Payment Method ===")
                print("1. Credit Card")
                print("2. Debit Card")
                payment_choice = input("Choose your payment method (1-2): ")

                if payment_choice in ["1", "2"]:
                    card_number = input("Enter your card number: ").strip()
                    card_name = input("Enter the name on your card: ").strip()
                    expiry_date = input("Enter the expiry date (MM/YY): ").strip()
                    cvv = input("Enter CVV: ").strip()
                    print(f"Payment processed successfully using {'Credit Card' if payment_choice == '1' else 'Debit Card'}!")
                else:
                    print("Invalid payment choice. Transaction failed.")
                return
            else:
                print("Sorry, this book is out of stock.")
                return
    print("Book not found!")


def main_menu():
    user = None
    while True:
        print("\n=== Online Bookstore Management ===")
        print("1. Register/Sign Up")
        print("2. Log In")
        print("3. Add Book")
        print("4. View All Books")
        print("5. Search Books")
        print("6. Update Book")
        print("7. Delete Book")
        print("8. Add Review")
        print("9. Purchase Book")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")
        try:
            if choice == "1":
                register()
            elif choice == "2":
                user = login()
            elif choice == "3":
                if user:
                    add_book()
                else:
                    print("Please log in first!")
            elif choice == "4":
                view_books()
            elif choice == "5":
                search_books()
            elif choice == "6":
                if user:
                    update_book()
                else:
                    print("Please log in first!")
            elif choice == "7":
                if user:
                    delete_book()
                else:
                    print("Please log in first!")
            elif choice == "8":
                add_review()
            elif choice == "9":
                purchase_book()
            elif choice == "10":
                print("Thank you for using the Online Bookstore Management System!")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}")


 
main_menu()

