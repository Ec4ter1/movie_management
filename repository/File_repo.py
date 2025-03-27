from Lab7.repository.Client_repo import ClientRepository
from Lab7.repository.Film_repo import FilmRepository
from Lab7.Clase.client import Clietnt
from Lab7.Clase.film import Film
from Lab7.Clase.inchirieri import Inchiriere
from Lab7.repository.Inchirieri_repo import InchirieriRepository


def clearFileContent(fileName):
    """
      Clear the content of the file
    """
    f = open(fileName, "w")
    f.close()


class ClientsFileRepository(ClientRepository):
    """
      Responsible with the load/store of clients from/into a text file
    """

    def __init__(self, file_name):
        ClientRepository.__init__(self)
        #self.__Clienti = {}
        self.repo = ClientRepository()
        self.__fileName = file_name
        self.__loadFromFile()

    def __createClientFromLine(self, line):
        """
        Citeste o linie din fisier si creeaza un client
        :param line: linia citita
        :return: client
        """
        fields = line.split(",")
        c = Clietnt(fields[0], fields[1].strip(), fields[2].strip())
        return c

    def __loadFromFile(self):
        """
         Load client from file
        """
        fh = open(self.__fileName)
        content = fh.read()
        fh.close()
        lines = content.split('\n')
        for line in lines:
            if line.strip() == "":
                continue  # we have an empty line, just skip
            c = self.__createClientFromLine(line)
            self.repo.store(c)


    def store(self, c):
        self.repo.store(c)
        self.__storeToFile()

    def __appendToFile(self, c):
        """
          Append a new line in the file representing the client
        """
        fh = open(self.__fileName, "a")
        line = f"{c.get_idc()}, {c.get_nume()}, {c.get_cnp()}"
        fh.write(line)
        fh.write("\n")
        fh.close()

    def update(self, idc, c):
        self.repo.update(idc, c)
        self.__storeToFile()

    def remove(self, idc):
        """
          remove a client from the repository
          id - string, the id of the client to be removed
          return client
        """
        self.repo.remove(idc)
        self.__storeToFile()

    def __storeToFile(self):
        fh = open(self.__fileName, "w")
        clienti = self.getAllClienti()
        for c in clienti:
            str_client = f"{c.get_idc()}, {c.get_nume()}, {c.get_cnp()}"
            fh.write(str_client)
            fh.write("\n")
        fh.close()

    def getAllClienti(self):
        return self.repo.getAllClienti()

    def size(self):
        return len(self.repo.getAllClienti())

class FilmeFileRepository(FilmRepository):
    """
      Responsible with the load/store of clients from/into a text file
    """

    def __init__(self, file_name):
        FilmRepository.__init__(self)
        self.repo = FilmRepository()
        self.__fileName = file_name
        self.__loadFromFile()

    def __createFilmFromLine(self, line):
        """
        Citeste o linie din fisier si creeaza un client
        :param line: linia citita
        :return: client
        """
        fields = line.split(",")
        f = Film(int(fields[0]), fields[1].strip(), fields[2].strip(), fields[3].strip())
        return f

    def __loadFromFile(self):
        """
         Load client from file
        """
        fh = open(self.__fileName)
        content = fh.read()
        fh.close()
        lines = content.split('\n')
        for line in lines:
            if line.strip() == "":
                continue  # we have an empty line, just skip
            f = self.__createFilmFromLine(line)
            self.repo.store(f)

    def store(self, c):
        self.repo.store(c)
        self.__storeToFile()

    def __appendToFile(self, f):
        """
          Append a new line in the file representing the client
        """
        fh = open(self.__fileName, "a")
        line = f"{f.get_idf()}, {f.get_titlu()}, {f.get_descriere()}, {f.get_gen()}"
        fh.write(line)
        fh.write("\n")
        fh.close()

    def update(self, idf, f):
        self.repo.update(idf, f)
        self.__storeToFile()

    def remove(self, idf):
        """
          remove a client from the repository
          id - string, the id of the client to be removed
          return client
        """
        self.repo.remove(idf)
        self.__storeToFile()

    def __storeToFile(self):
        fh = open(self.__fileName, "w")
        filme = self.getAllFilme()
        for f in filme:
            str_client = f"{f.get_idf()}, {f.get_titlu()}, {f.get_descriere()}, {f.get_gen()}"
            fh.write(str_client)
            fh.write("\n")
        fh.close()

    def getAllFilme(self):
        return self.repo.getAllFilme()

    def size(self):
        return len(self.repo.getAllFilme())

class InchirieriFileRepository(InchirieriRepository):
    """
      Responsible with the load/store of clients from/into a text file
    """

    def __init__(self, file_name):
        InchirieriRepository.__init__(self)
        self.repo = InchirieriRepository()
        self.__fileName = file_name
        self.__loadFromFile()

    def __createFilmFromLine(self, line):
        """
        Citeste o linie din fisier si creeaza un client
        :param line: linia citita
        :return: client
        """
        fields = line.split(",")
        i = Inchiriere(int(fields[0]), int(fields[1]))
        return i

    def __loadFromFile(self):
        """
         Load client from file
        """
        fh = open(self.__fileName)
        content = fh.read()
        fh.close()
        lines = content.split('\n')
        for line in lines:
            if line.strip() == "":
                continue  # we have an empty line, just skip
            f = self.__createFilmFromLine(line)
            self.repo.store(f)

    def store(self, c):
        self.repo.store(c)
        self.__storeToFile()

    def __appendToFile(self, f):
        """
          Append a new line in the file representing the client
        """
        fh = open(self.__fileName, "a")
        line = f"{f.get_idf()}, {f.get_idc()}"
        fh.write(line)
        fh.write("\n")
        fh.close()

    def remove(self, idc, idf):
        """
          remove a client from the repository
          id - string, the id of the client to be removed
          return client
        """
        self.repo.remove(idc, idf)
        self.__storeToFile()

    def __storeToFile(self):
        fh = open(self.__fileName, "w")
        filme = self.getAllInchirieri()
        for f in filme:
            str_client = f"{f.get_idf()}, {f.get_idc()}"
            fh.write(str_client)
            fh.write("\n")
        fh.close()

    def find(self, idc):
        return self.repo.find(idc)

    def find2(self, idf):
        return self.repo.find2(idf)
    def getAllInchirieri(self):
        return self.repo.getAllInchirieri()

    def size(self):
        return len(self.repo.getAllInchirieri())
