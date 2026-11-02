class Film:
    def __init__(self, title, genre, release_year, rating, id = None):
        self.id = id
        self.title = title
        self.genre = genre
        self.release_year = release_year
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Film({self.id}, {self.title}, {self.genre}, {self.release_year}, {self.rating})"