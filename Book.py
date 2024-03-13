class Book:
    def __init__(self, title, number_of_pages, cover_type, category):
        self.title = title
        self.number_of_pages = number_of_pages
        self.cover_type = cover_type
        self.category = category

    def __str__(self):
        return (f"Title: {self.title}, Number of Pages: {self.number_of_pages}, "
                f"Cover Type: {self.cover_type}, Category: {self.category}")
