from .article import Article


class Magazine:
    all = []

    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if not (2 <= len(value) <= 16):
            return
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        arts = self.articles()
        if not arts:
            return None
        return list({a.author for a in arts})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None

        count = {}
        for a in arts:
            count[a.author] = count.get(a.author, 0) + 1

        result = [author for author, c in count.items() if c > 2]
        return result if result else None
