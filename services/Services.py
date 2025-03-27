from Lab7.Clase.validation import Validator, ValidatorException
from Lab7.Clase.film import Film
from Lab7.Clase.client import Clietnt
from Lab7.repository.File_repo import ClientsFileRepository, FilmeFileRepository, InchirieriFileRepository
from Lab7.repository.Inchirieri_repo import InchirieriRepository
from Lab7.Clase.inchirieri import Inchiriere
from math import ceil

def cmp_filme(elem):
    """
    Functie de comparare cand aceasta se realizeaza dupa nr filme
    :param elem: list
    :return: al doilea element, nr de filme inchiriate
    """
    return elem[2]
class FilmeService:
    def __init__(self, val, f_repo):
        self.__val = val
        self.__repo = f_repo
        #self.__c_repo = ClientsFileRepository("repository\clienti")


    def create(self, idf, titlu, descriere, gen):
        """
        Creaza film, il verifica si adauga in rpository
        :param idf: id-ul filmului
        :param titlu: titlul filmului
        :param descriere:
        :param gen:
        :return: filmul
        """
        f = Film(idf, titlu, descriere, gen)
        self.__val.validate_film(f)
        self.__repo.store(f)
        return f


    def remove(self, idf):
        """
        Sterge film din repository
        :param idf: id-ul filmului
        :return:
        """
        return self.__repo.remove(idf)

    def search(self, ceva):
        """
        Gaseste un film in repository
        :param ceva: id-ul filmului cautat
        :return: filmul
        """
        l = self.__repo.getAllFilme()
        if ceva=="":
            return l
        for f in l:
            if f.get_idf() == ceva:
                return f

    def update(self, idf, titlu, descriere, gen):
        """
        Modifica film in repository
        :param idf: id-ul filmului
        :param titlu:
        :param descriere:
        :param gen:
        :return: filmul de dinaite de a fi modificat
        """
        newf = Film(idf, titlu, descriere, gen)
        self.__val.validate_film(newf)
        oldf = self.__repo.find(idf)
        self.__repo.update(idf, newf)
        return oldf

    def af(self):
        rez=[]
        filme = self.__repo.getAllFilme()
        for i in filme:
            rez.append(str(i))
        return rez

    def get_size(self):
        """
          Return the number of films
        """
        return self.__repo.size()
class ClientService:
    def __init__(self, val, c_repo):
        self.__c_val = val
        self.__c_repo = c_repo


    def create(self, idc, nume, cnp):
        c = Clietnt(idc, nume, cnp)
        self.__c_val.validate_client(c)
        self.__c_repo.store(c)
        return c

    def remove(self, idc):
        """
        Sterge client din repository
        :param idc: id-ul clientului
        :return:
        """
        return self.__c_repo.remove(idc)

    def search(self, ceva):
        """
        Gaseste un client in repository
        :param ceva: id-ul clientului cautat
        :return: clientul
        """
        l = self.__c_repo.getAllClienti()
        if ceva=="":
            return l
        for c in l:
            if c.get_idc() == ceva:
                return c

    def update(self, idc, nume, cnp):
        """
        Modifica client in repository
        :param idc: id-ul clientului
        :param nume:
        :param cnp:
        :return: clientul de dinaite de a fi modificat
        """
        newc = Clietnt(idc, nume, cnp)
        self.__c_val.validate_client(newc)
        oldf = self.__c_repo.find(idc)
        self.__c_repo.update(idc, newc)
        return oldf


    def get_size(self):
        """
          Return the number of clients
        """
        return self.__c_repo.size()

    def af(self):
        rez = []
        clienti = self.__c_repo.getAllClienti()
        for i in clienti:
            rez.append(str(i))
        return rez

class InchirieriService():
    def __init__(self, val, f_repo, c_repo, i_repo):
        self.__f_repo = f_repo
        self.__c_val = val
        self.__c_repo = c_repo
        self.__i_repo = i_repo

    def create(self, idc, idf):
        clienti = self.__c_repo.getAllClienti()
        filme = self.__f_repo.getAllFilme()
        for c in clienti:
            for f in filme:
                if int(idc) == int(c.get_idc()) and int(idf) == int(f.get_idf()):
                    r = Inchiriere(idc, idf)
                    self.__c_val.validate_inchiriere(r)
                    self.__i_repo.store(r)
                    return r

    def remove(self, idc, idf):
        """
        Sterge inchiriere din repository
        :param idc:
        :param idf:
        :return:
        """
        return self.__i_repo.remove(idc, idf)

    def clienti_ord_nume(self):
        """
        Ordoneaza clientii cu inchirieri dupa nume
        :return: lista cu numele clientilor
        """
        inchirieri = self.__i_repo.getAllInchirieri()
        clienti=self.__c_repo.getAllClienti()
        c_i = []
        for i in inchirieri:
            for c in clienti:
                if int(i.get_idc())== int(c.get_idc()) and c.get_nume() not in c_i:
                    c_i.append(c.get_nume())
        #s = sorted(set(c_i), key=str)
        s = self.quicksort(c_i, 0, len(c_i)-1)
        return s

    def gnome_sort(self, lista, keye):
        """
        Sorteaza lista
        :param lista:
        :param keye: cheia/ conditia
        :return: lista
        Complexitate:
        n- lungime lista
        Best case:
        n=1
        T(x)=1+1 apartine O(1)
        lista e deja sortata
        T(x)=1+(1+1+1+1)+(1+1)+..(1+1)=1 + 4 +2(n-2) apartine O(n)
        Caz mediu:
        lista e invers sortata/While poate fi executat 1,2,..n ori (același probabilitate).
        T(x)=1+2+(1+4)+2+2+(1+4)+(1+4)..=7+(1+4)(1+2+3+..n-1)=7+5n(n-1)/2
        apartine O(n^2)
        => T apartine O(n^2), theta(n^2)
        """
        index = 0
        while index <= len(lista)-1:
            if index == 0:
                index+=1
            if keye(lista[index]) <= keye(lista[index - 1]):
                index+=1
            else:
                aux = lista[index]
                lista[index]= lista[index-1]
                lista[index-1]=aux
                index-=1
        return lista

    def partition(self, lista, low, high):
        pivot = lista[high]
        i = low - 1
        for j in range(low, high):
            if lista[j] <= pivot:
                i = i + 1
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
        aux = lista[high]
        lista[high]= lista[i+1]
        lista[i+1]=aux
        return i + 1

    def quicksort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quicksort(array, low, pi - 1)
            self.quicksort(array, pi + 1, high)
        return array

    def clienti_ord_nr_filme(self):
        """
        Ordoneaza clientii cu inchirieri dupa nr de filme inchiriate
        :return: lista clienti
        """
        clienti = self.__c_repo.getAllClienti()
        inchirieri = self.__i_repo.getAllInchirieri()
        #print(inchirieri)
        lista = []
        for c in clienti:
            #print(c.get_idc())
            lista_filme_client = self.__i_repo.find(c.get_idc())
            #print(lista_filme_client)
            rez = []
            for i in lista_filme_client:
                rez.append(str(i))
            d = [c.get_nume(), rez, len(rez)]
            lista.append(d)
        #print(lista)
        lista.sort(key=cmp_filme, reverse=True)
        return lista

    def cele_mai_inchiriate_filme(self):
        """
        Ordoneaza filmele dupa nr de inchirieri
        :return:
        """
        filme = self.__f_repo.getAllFilme()
        lista =[]
        for f in filme:
            lista_filme_inchiriate = self.__i_repo.find2(f.get_idf())
            rez = []
            for i in lista_filme_inchiriate:
                rez.append(str(i))
            d = [f.get_titlu(), rez, len(rez)]
            lista.append(d)
        #lista_ordonata = sorted(lista, key=cmp_filme, reverse=True)
        lista_ordonata = self.gnome_sort(lista, cmp_filme)
        return lista_ordonata

    def primii_30(self):
        """
        Returneaza primii 30% clienti cu cele mai multe filme inchiriate
        :return:
        """
        lista_ordonata = self.clienti_ord_nr_filme()
        # Calculăm indexul până la care vrem să selectăm elementele
        index_limita = int(len(lista_ordonata) * 0.3)
        primele_30 = lista_ordonata[:index_limita]
        return primele_30

    def primele_30(self):
        """
        Returneaza primele 30% din filme din lista cu filme inchiriate
        :return:
        """
        lista_ordonata = self.cele_mai_inchiriate_filme()
        # Calculăm indexul până la care vrem să selectăm elementele
        index_limita = ceil(len(lista_ordonata) * 0.3)
        primele_30 = lista_ordonata[:index_limita]
        return primele_30
    def get_size(self):
        """
          Return the number of inchirieri
        """
        return self.__i_repo.size()


    def af_inchirieri(self):
        rez = []
        inchirieri = self.__i_repo.getAllInchirieri()
        for i in inchirieri:
            rez.append(str(i))
        return rez

def test_gnome_sort():
    arr=[2,34,6,4]
    InchirieriService(Validator(), FilmeFileRepository("filme"), ClientsFileRepository("clienti"),InchirieriRepository()).clienti_ord_nr_filme()
    assert InchirieriService(Validator(), ClientsFileRepository("clienti"), FilmeFileRepository("filme"), InchirieriFileRepository("inchirieri")).quicksort(arr,0,len(arr)-1) == [2, 4, 6, 34]

if __name__=="__main__":
    test_gnome_sort()

