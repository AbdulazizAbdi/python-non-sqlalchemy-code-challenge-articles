class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            raise AttributeError("Title is immutable")
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise Exception("Title must be between 5 and 50 characters")
        self._title = title
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Must be an instance of Author class")
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise Exception("Must be an instance of Magazine class")
        self._magazine = magazine
        
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise AttributeError("Name is immutable")
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not len(name) > 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine_list = [article.magazine for article in Article.all if article.author == self]
        return list(set(magazine_list))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories_list = [article.magazine.category for article in Article.all if article.author == self]
        if len(categories_list) == 0:
            return None
        else:
            return list(set(categories_list))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception('Name must be a string')
        if not 2 <= len(name) <= 16:
            raise Exception('Name must be between 2 and 16 characters')
        self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise Exception("Category must be a string")
        if not len(category) > 0:
            raise Exception("Category must be a more than 0 characters")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors_list = [article.author for article in Article.all if article.magazine == self]
        return list(set(contributors_list))

    def article_titles(self):
        title_list = [article.title for article in Article.all if article.magazine == self]
        if len(title_list) == 0:
            return None
        else:
            return title_list

    def contributing_authors(self):
        author_list = {}
        for article in Article.all:
            author_article_count =0
            if article.magazine == self:
                author = article.author
                if author in author_list:
                    author_list[author] += 1
                else:
                    author_list[author] = 1

        contributing_author_list = [author for author, article_count in author_list.items() if article_count > 2]
        if len(contributing_author_list) == 0:
            return None
        else:
            return contributing_author_list
