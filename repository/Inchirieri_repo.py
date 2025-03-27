from Lab7.Clase.inchirieri import Inchiriere
from Lab7.Clase.client import Clietnt
from Lab7.Clase.film import Film
class InchirieriRepository:
    nr = 0
    def __init__(self):
        self.__Inchirieri = {}
        self.nr= 0

    def store(self, i):
        """
        Adauga o inchiriere in lista
        :param i: inchirierea
        """
        self.__Inchirieri[self.nr]=i
        self.nr+=1

    def remove(self, idc, idf):
        """
        Sterge o inchiriere din lista
        :param idc:
        :param idf:
        :return:
        """
        l = len(self.__Inchirieri)
        i=0
        while i<l:
            if idf == self.__Inchirieri[i].get_idf() and idc == self.__Inchirieri[i].get_idc():
                del self.__Inchirieri[i]
            i+=1

    def find(self, idc):
        """
        Gsaeste toate inchirierile unui client
        :param idc: id-ul clientului
        :return: inchirierea
        """
        rez=[]
        for i in self.__Inchirieri:
            if self.__Inchirieri[i].get_idc() == idc:
                rez.append(self.__Inchirieri[i])
        return rez

    def find2(self, idf):
        """
        Gaseste toti clientii care au inchiriat un film
        :return:
        """
        rez = []
        for i in self.__Inchirieri:
            if self.__Inchirieri[i].get_idf() == idf:
                rez.append(self.__Inchirieri[i])
        return rez

    def getAllInchirieri(self):
        return self.__Inchirieri.values()

    def size(self):
        """
          return the number of inchirieri in the repository
        """
        return len(self.__Inchirieri)


def test_store_inchiriere():
    i = Inchiriere(12, 13)
    repo = InchirieriRepository()
    assert repo.size()==0
    repo.store(i)
    assert repo.size()==1

test_store_inchiriere()

def test_sterge_inchiriere():
    i=Inchiriere(12, 13)
    i1=Inchiriere(1,2)
    repo = InchirieriRepository()
    repo.store(i)
    repo.store(i1)
    assert repo.size()==2
    repo.remove(1,2)
    assert repo.size()==1

test_sterge_inchiriere()

def test_find_inchiriere():
    i = Inchiriere(12, 13)
    i1 = Inchiriere(1, 2)
    repo = InchirieriRepository()
    repo.store(i)
    repo.store(i1)
    assert len(repo.find(1))==1

test_find_inchiriere()

