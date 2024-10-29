class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f" Name: {self.name}, Author:{self.author}, {self.page_count} pages")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f" Name: {self.name}, Chief Editor: {self.chief_editor}")


if __name__ == "__main__":
    publication1 = Magazine("Donald Duck","Aki Hyyppä")
    publication1.print_information()
    publication2 = Book("Compartment No.6", "Rosa Liksom", 192)
    publication2.print_information()

