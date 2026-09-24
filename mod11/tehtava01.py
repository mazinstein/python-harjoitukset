class Publication:
    def __init__(self, title):
        self.title = title

class Book(Publication):
    def __init__(self, title, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(title)

    def print_information(self):
        print(self.title ,self.author, self.pages)

class Magazine(Publication):
    def __init__(self, title, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(title)

    def print_information(self):
        print(self.title ,self.chief_editor)

magazine = Magazine("Donald Duck", "Aki Hyyppä")
book = Book("Ward No. 6", "Rosa Liksom", 192)

magazine.print_information()
book.print_information()