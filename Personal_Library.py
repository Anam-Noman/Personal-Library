import json

class PersonalLibraryManager:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(self.library, file, indent=4)

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        publication_year = input("Enter publication year: ")
        genre = input("Enter genre: ")
        read_status = input("Have you read it? (yes/no): ").strip().lower() == "yes"

        book = {
            "Title": title,
            "Author": author,
            "Publication Year": publication_year,
            "Genre": genre,
            "Read Status": read_status
        }

        self.library.append(book)
        self.save_library()
        print("Book added successfully!\n")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.library = [book for book in self.library if book["Title"].lower() != title.lower()]
        self.save_library()
        print("Book removed successfully (if it existed).\n")

    def search_book(self):
        query = input("Enter title or author to search: ").lower()
        results = [book for book in self.library if query in book["Title"].lower() or query in book["Author"].lower()]

        if results:
            for book in results:
                print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Publication Year']}, Genre: {book['Genre']}, Read: {'Yes' if book['Read Status'] else 'No'}")
        else:
            print("No matching books found.")
        print()

    def display_books(self):
        if not self.library:
            print("Library is empty.\n")
        else:
            for book in self.library:
                print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Publication Year']}, Genre: {book['Genre']}, Read: {'Yes' if book['Read Status'] else 'No'}")
            print()

    def display_statistics(self):
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["Read Status"])
        read_percentage = (read_books / total_books * 100) if total_books > 0 else 0

        print(f"Total Books: {total_books}")
        print(f"Books Read: {read_books} ({read_percentage:.2f}%)\n")

    def menu(self):
        while True:
            print("Personal Library Manager")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Exiting...\n")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = PersonalLibraryManager()
    manager.menu()
