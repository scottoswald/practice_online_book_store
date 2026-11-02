class Book:
    # books don't have an id until they are saved to the database
    # so we need a default value for id
    # and parameters with a default must come last
    # this change, means the `BookRepository` will no longer work as expected
    def __init__(self, title, author, id = None):
        self.id = id
        self.title = title
        self.author = author

    # This tells Python how to compare two Books 
    # Without this, Python only checks if they are the same object in memory. 
    # With this, it checks if their data (like name and genre) matches.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a Book
    # Instead of seeing a confusing code like <Artist object at 0x102...>, 
    # you'll see the actual ID, Name, and Genre, which is much more useful to us humans
    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author})"