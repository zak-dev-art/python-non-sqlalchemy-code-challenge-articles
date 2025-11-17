class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # immutable: if already set, ignore new values
        if self._title is not None:
            return

        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            return

        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if isinstance(value, Magazine):
            self._magazine = value
