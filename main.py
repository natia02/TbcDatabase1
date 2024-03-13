import json
import sqlite3

from Book import Book


def books_to_list():
    books = []
    with open("Books.json", 'r') as file:
        data = json.load(file)
        for book_data in data:
            book = Book(book_data['title'], book_data['number_of_pages'],
                        book_data['cover_type'], book_data['category'])
            books.append(book)

    return books


def create_and_fill_database():
    books = books_to_list()
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS book (
                        title text,
                        number_of_pages integer,
                        cover_type text,
                        category text
                        )""")

    for book in books:
        c.execute("INSERT INTO book VALUES (?,?,?,?)",
                  (book.title, book.number_of_pages, book.cover_type, book.category))

    conn.commit()
    conn.close()


def print_avg_of_books():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()

    c.execute("SELECT avg(number_of_pages) FROM book")
    avg_pages = c.fetchone()[0]

    print(f"Average number of pages across all books: {avg_pages}")

    conn.close()


def print_the_title_of_largest_book():
    conn = sqlite3.connect('Library.db')
    c = conn.cursor()

    c.execute("SELECT title FROM book WHERE number_of_pages = (SELECT MAX(number_of_pages) FROM book)")
    largest_book = c.fetchone()[0]

    print(f"The largest Book is: {largest_book}")

    conn.close()


if __name__ == "__main__":
    create_and_fill_database()
    print_avg_of_books()
    print_the_title_of_largest_book()
