from Lab7.Clase.client import Clietnt
class ClientRepository:
    def __init__(self):
        self.__Clienti= {}

    def store(self, c):
        """
        Adauga la lista un client
        :param c: clientul
        :return:
        """
        if c.get_idc() in self.__Clienti:
            print("Repetare")
        self.__Clienti[int(c.get_idc())] = c

    def remove(self, idc):

        if idc not in self.__Clienti:
            raise ValueError("No client for the id")
        c = self.__Clienti[idc]
        del self.__Clienti[idc]
        return c

    def update(self, idc, c):
        """
        Modifica lista cu clienti
        :param idc: id-ul clientului modificat
        :param c: clientul nou
        :return:
        """
        self.remove(idc)
        self.store(c)

    def find(self, idc):
        """
        Gsaeste un client in lista
        :param idc: id-ul clientului
        :return: clientul
        """
        if not idc in self.__Clienti:
            return None
        return self.__Clienti[idc]

    def getAllClienti(self):
        """
        lista de clienti
        :return: lista
        """
        return self.__Clienti.values()

    def size(self):
        """
          return the number of clients in the repository
        """
        return len(self.__Clienti)


def test_store_client():
    c = Clietnt(1, "Ana", 1234567789)
    repo = ClientRepository()
    assert repo.size()==0
    repo.store(c)
    assert repo.size()==1

test_store_client()

def test_remove_client():
    repo = ClientRepository()
    c = Clietnt(1, "Ana", 1234567789)
    c1 = Clietnt(2, "Andreea", 12222567789)
    repo.store(c)
    repo.store(c1)
    assert repo.size()==2
    repo.remove(1)
    assert repo.size()==1

test_remove_client()

def test_update_client():
    repo = ClientRepository()
    c = Clietnt(1, "Ana", 1234567789)
    repo.store(c)
    c1 = Clietnt(1, "Andreea", 12222567789)
    repo.update(1, c1)
    assert repo.find(1)== c1

test_update_client()

def test_find_client():
    repo = ClientRepository()
    c = Clietnt(2, "Andreea", 12222567789)
    repo.store(c)
    assert repo.find(2)==c

test_find_client()

def test_getAllClienti():
    repo = ClientRepository()
    c = Clietnt(2, "Andreea", 12222567789)
    repo.store(c)
    c1 = Clietnt(1, "Ana", 1234567789)
    repo.store(c1)
    l = repo.getAllClienti()
    assert len(l)==2
    f2 = repo.find(1)
    assert f2.get_idc()==1
    assert f2.get_nume()=="Ana"
    assert f2.get_cnp()== 1234567789

test_getAllClienti()