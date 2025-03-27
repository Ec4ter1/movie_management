from Lab7.Clase.film import Film
class FilmRepository:

    def __init__(self):
        self.__Filme = {}

    def store(self, f):
        """
        Adauga un film in lista
        :param f: filmul
        """
        if f.get_idf() in self.__Filme:
            print("Repetare")
        self.__Filme[int(f.get_idf())] = f

    def remove(self, idf):
        """
        Sterge film din lista
        :param idf: id-ul filmului
        :return: filmul sters
        """
        if not idf in self.__Filme:
            raise ValueError("No film for the id given")
        f = self.__Filme[idf]
        del self.__Filme[idf]
        return f

    def update(self, idf, f):
        """
        Modifica lista cu filme
        :param idf: id-ul filmului
        :param f: noul film
        """
        self.remove(idf)
        self.store(f)

    def find(self, idf):
        """
        Gaseste un film in lista
        :param idf: id-ul filmului
        :return: filmul
        """
        if not idf in self.__Filme:
            return None
        return self.__Filme[idf]

    def getAllFilme(self):
        """
        Returns the list of films
        :return: lista
        """
        return self.__Filme.values()

    def size(self):
        """
          return the number of film s in the repository
        """
        return len(self.__Filme)


def test_store_film():
    f= Film(1, "Trolls", "Muzica", "Comedie")
    repo = FilmRepository()
    assert repo.size()==0
    repo.store(f)
    assert repo.size()==1

test_store_film()

def test_remove_film():
    repo = FilmRepository()
    f = Film(1, "Trolls", "Muzica", "Comedie")
    f1= Film(2, "Beauty Shop", "Hair salon", "Drama")
    repo.store(f)
    repo.store(f1)
    assert repo.size()==2
    repo.remove(1)
    assert repo.size()==1

test_remove_film()

def test_update_film():
    repo = FilmRepository()
    f = Film(1, "Trolls", "Muzica", "Comedie")
    repo.store(f)
    f1 = Film(1, "Beauty Shop", "Hair salon", "Drama")
    repo.update(1, f1)
    assert repo.find(1)== f1

test_update_film()

def test_find_film():
    repo = FilmRepository()
    f = Film(1, "Trolls", "Muzica", "Comedie")
    repo.store(f)
    assert repo.find(1)==f

test_find_film()

def test_getAllFilme():
    repo = FilmRepository()
    f = Film(1, "Trolls", "Muzica", "Comedie")
    repo.store(f)
    f1 = Film(2, "Beauty Shop", "Hair salon", "Drama")
    repo.store(f1)
    l = repo.getAllFilme()
    assert len(l)==2
    f2 = repo.find(1)
    assert f2.get_idf()==1
    assert f2.get_titlu()=="Trolls"
    assert f2.get_descriere()=="Muzica"
    assert f2.get_gen()=="Comedie"

test_getAllFilme()