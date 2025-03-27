from Lab7.Clase.validation import ValidatorException
from Lab7.Random_Generator import random_gen, random_name, random_list_id, random_cnp
from Lab7.services.Services import FilmeService, ClientService, InchirieriService
from Lab7.repository.Inchirieri_repo import InchirieriRepository
from Lab7.repository.Client_repo import ClientRepository
from Lab7.repository.Film_repo import FilmRepository
from Lab7.Clase.validation import Validator
import random

class UI:
    def __init__(self, fcontroler, ccontroler, icontroler):
        self.__fcontroler = fcontroler
        self.__ccontroler = ccontroler
        self.__icontroler = icontroler

    def __readUserCommand(self):
        print("""
        1. adaugă film
        2. sterge film
        3. modifica film
        4. adauga client
        5. sterge client
        6. modifica client
        7. creeaza un film random
        8. creeaza un client random
        9. creeaza o lista random de filme
        10. creeaza o lista random de clienti
        11. cauta film
        12. cauta client
        13. inchiriaza
        14. returneaza
        15. clienți cu filme închiriate ordonat dupa: nume
        16. clienți cu filme închiriate ordonat dupa: numărul de filme închiriate
        17. cele mai inchiriate filme
        18. primi 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
        19. filmele inchiriate ordonate dupa: numarul de clienti
        20. primele 30% filme cu cele mai multe inchiriari
        """)
        return input("Give command:")

    def __createFilm(self):
        idf = input("Film id:")
        titlu = input("Titlu:")
        descriere = input("Descriere:")
        gen = input("Gen:")
        try:
            self.__fcontroler.create(idf, titlu, descriere, gen)
            print("Creat si adaugat cu succces")
        except ValidatorException as ex:
            print(ex)

    def create_random_film(self, l, x):
        f = self.__fcontroler.create(l[x], random_name(), random_name(), random_gen())
        return f

    def create_list_of_random_films(self):
        x = random.randint(0, 5)
        l= random_list_id()
        while x >= 0:
            self.create_random_film(l, x)
            x -= 1
            
    def afiseaza_filme(self):
        print(self.__fcontroler.af())

    def __removeFilm(self):
        id = int(input("Film id:"))
        try:
            f = self.__fcontroler.remove(id)
            print("Film sters")
        except ValueError as msg:
            print(msg)

    def __updateFilm(self):
        idf = int(input("Film id:"))
        titlu = input("Titlu:")
        descriere = input("Descriere:")
        gen = input("Gen:")
        try:
            old = self.__fcontroler.update(idf, titlu, descriere, gen)
            print("Film updated")
        except ValueError as msg:
            print(msg)

    def __searchFilm(self):
        idf = int(input("Film id:"))
        try:
            print(self.__fcontroler.search(idf))
            print("Film gasit")
        except ValueError as msg:
            print(msg)
    def __createClient(self):
        idc = input("Client id:")
        nume = input("Nume: ")
        cnp = input("Cnp: ")
        try:
            self.__ccontroler.create(idc, nume, cnp)
            print("Creat si adaugat cu succces")
        except ValidatorException as ex:
            print(ex)

    def create_random_client(self, l, x):
        c = self.__ccontroler.create(l[x], random_name(), random_cnp())
        return c

    def create_list_of_random_clients(self):
        x = random.randint(0, 5)
        l= random_list_id()
        while x >= 0:
            self.create_random_client(l,x)
            x -= 1
    def __stergeClient(self):
        id = int(input("Client id:"))
        try:
            c = self.__ccontroler.remove(id)
            print("Client sters")
        except ValueError as msg:
            print(msg)

    def __modificaClient(self):
        idc = int(input("Client id:"))
        nume = input("Nume: ")
        cnp = input("Cnp: ")
        try:
            old = self.__ccontroler.create(idc, nume, cnp)
            print("Film updated")
        except ValueError as msg:
            print(msg)

    def __afiseaza_clienti(self):
        print(self.__ccontroler.af())

    def __searchClient(self):
        idc = int(input("Client id:"))
        try:
            print(self.__ccontroler.search(idc))
            print("Client gasit")
        except ValueError as msg:
            print(msg)
    def __inchiriaza(self):
        idc = input("Client id:")
        idf = input("Film id:")
        try:
            self.__icontroler.create(idc, idf)
        except ValueError as msg:
            print(msg)

    def __returneaza(self):
        idc = input("Client id:")
        idf = input("Film id:")
        try:
            self.__icontroler.remove(idc, idf)
        except ValueError as msg:
            print(msg)

    def __ordonare_dupa_nume(self):
        print(self.__icontroler.clienti_ord_nume())

    def __ordonare_nr_filme(self):
        print(self.__icontroler.clienti_ord_nr_filme())

    def __cele_mai_inchiriate_filme(self):
        print(self.__icontroler.cele_mai_inchiriate_filme())

    def __primii_30(self):
        print(self.__icontroler.primii_30())

    def __primele_30(self):
        print(self.__icontroler.primele_30())

    def afiseaza_inchirieri(self):
        print(self.__icontroler.af_inchirieri())


    def startUI(self):
        while True:
            option = self.__readUserCommand()
            if option == "0":
                print("By By")
                return
            if option == "1":
                'Citeste si adauga'
                self.__createFilm()
                self.afiseaza_filme()
            if option == "2":
                'Sterge film'
                self.__removeFilm()
                self.afiseaza_filme()
            if option == "3":
                'modifica film'
                self.__updateFilm()
                self.afiseaza_filme()
            if option == "4":
                'Citeste si adauga client'
                self.__createClient()
                self.__afiseaza_clienti()
            if option == "5":
                'Sterge client'
                self.__stergeClient()
                self.__afiseaza_clienti()
            if option == "6":
                'Modifica client'
                self.__modificaClient()
                self.__afiseaza_clienti()
            elif option == "7":
                'Flim random'
                l = random_list_id()
                x= random.randint(0,5)
                self.create_random_film(l,x)
                self.afiseaza_filme()
            elif option == "8":
                'Client random'
                l = random_list_id()
                x = random.randint(0, 5)
                self.create_random_client(l,x)
                self.__afiseaza_clienti()
            elif option == "9":
                'Lista filme random'
                self.create_list_of_random_films()
                print(self.__fcontroler.af())
            elif option == "10":
                'Lista clienti random'
                self.create_list_of_random_clients()
                self.__afiseaza_clienti()
            elif option == "11":
                'Cauta film'
                self.__searchFilm()
            elif option == "12":
                'Cauta client'
                self.__searchClient()
            elif option == "13":
                'Inchiriere'
                self.__inchiriaza()
                self.afiseaza_inchirieri()
            elif option == "14":
                'Returnare'
                self.__returneaza()
                self.afiseaza_inchirieri()
            elif option == "15":
                'Ordonate dupa nume'
                self.__ordonare_dupa_nume()
            elif option == "16":
                'Ordonate dupa nr'
                self.__ordonare_nr_filme()
            elif option == "17":
                'Cele mai inchiriate filme'
                self.__cele_mai_inchiriate_filme()
            elif option == "18":
                'Primii 30%'
                self.__primii_30()
            elif option == "19":
                'Filmele ordonate dupa nr de clienti'
                self.__cele_mai_inchiriate_filme()
            elif option == "20":
                'Primii 30%'
                self.__primele_30()
            elif option =="!":
                self.__afiseaza_clienti()
                self.afiseaza_filme()
                self.afiseaza_inchirieri()

""""
def test_create_random_film():
    u = UI(FilmeService(), ClientService(), InchirieriService())
    l = random_list_id()
    x = random.randint(0, 5)
    random.seed(1)
    filme = u.create_random_film(l,x)
    assert filme.get_idf()==14
    assert filme.get_titlu() == "Szyci"
    assert filme.get_descriere() == "Pyop"
    assert filme.get_gen() == "Drama"
    
test_create_random_film()

"""