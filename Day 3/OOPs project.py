class Library:
    def __init__(self, books):
        self.books = books[:]  # copy list to avoid mutation
        self.issued = {}       # {book_name: borrower_name}

    def display_books(self):
        if not self.books:
            print("\nNo books are currently available.\n")
        else:
            print(f"\n📚 {len(self.books)} Available Book(s):")
            for book in self.books:
                print(f"   ♦ {book}")
            print()

    def borrow_book(self, user, book):
        if book not in self.books:
            if book in self.issued:
                print(f"\n❌ '{book}' is already issued to {self.issued[book]}.\n")
            else:
                print(f"\n❌ '{book}' is not available in the library.\n")
            return
        self.books.remove(book)
        self.issued[book] = user
        print(f"\n✅ '{book}' has been issued to {user}. Please return it on time!\n")

    def return_book(self, user, book):
        if book in self.issued and self.issued[book] == user:
            self.books.append(book)
            del self.issued[book]
            print(f"\n✅ '{book}' has been returned. Thank you, {user}!\n")
        else:
            print(f"\n❌ Return failed: Either '{book}' was not issued or it was not issued to {user}.\n")

    def donate_book(self, book):
        self.books.append(book)
        print(f"\n🎁 Thank you for donating '{book}' to the library!\n")

    def track_books(self):
        if not self.issued:
            print("\n📖 No books are currently issued.\n")
        else:
            print("\n📖 Issued Books:")
            for book, user in self.issued.items():
                print(f"   ♦ '{book}' → issued to {user}")
            print()


class LibrarySystem:
    def __init__(self, library):
        self.library = library

    def menu(self):
        print("""
================= 📚 DELHI LIBRARY MENU 📚 =================
1. List all available books
2. Borrow a book
3. Return a book
4. Donate a book
5. Track issued books
6. Exit
============================================================
""")

    def run(self):
        print("\n🌟 Welcome to the the Library! 🌟\n")
        while True:
            self.menu()
            try:
                choice = int(input("👉 Enter your choice (1-6): "))
            except ValueError:
                print("\n❌ Invalid input! Please enter a number (1-6).\n")
                continue

            if choice == 1:
                self.library.display_books()

            elif choice == 2:
                user = input("Enter your name: ").strip()
                book = input("Enter book name to borrow: ").strip()
                self.library.borrow_book(user, book)

            elif choice == 3:
                user = input("Enter your name: ").strip()
                book = input("Enter book name to return: ").strip()
                self.library.return_book(user, book)

            elif choice == 4:
                book = input("Enter book name to donate: ").strip()
                self.library.donate_book(book)

            elif choice == 5:
                self.library.track_books()

            elif choice == 6:
                print("\n👋 Thank you for visiting the the Library. Goodbye!\n")
                break

            else:
                print("\n❌ Invalid choice! Please select between 1 and 6.\n")


if __name__ == "__main__":
    initial_books = ["Vistas", "Invention", "Rich & Poor", "Indian",
                     "Macroeconomics", "Microeconomics"]

    library = Library(initial_books)
    system = LibrarySystem(library)
    system.run()
