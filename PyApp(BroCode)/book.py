class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return f'{self.pages + other.pages} pages'
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title' or key == 0:
            return self.title
        elif key == 'author' or key == 1:
            return self.author
        elif key == 'pages' or key == 2:
            return self.pages
        else:
            return 'Nothing'
    
