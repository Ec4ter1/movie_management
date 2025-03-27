from L4.Functii import read_valid_number
from Lab7.Clase.film import Film
from Lab7.Clase.client import Clietnt
"""
Scrieți o aplicație pentru o firmă de închiriere de filme.
Aplicația stochează:
 filme: <id>,<titlu>,<descriere>,<gen>,etc
 clienți: <id>, <nume>, <CNP>,etc
"""
from Lab7.tests import *
from Lab7.Clase.validation import Validator
from Lab7.repository.Film_repo import FilmRepository
from Lab7.repository.Client_repo import ClientRepository
from Lab7.repository.Inchirieri_repo import InchirieriRepository
from Lab7.services.Services import FilmeService, ClientService, InchirieriService
from Lab7.ui.consola import UI
from Lab7.repository.File_repo import ClientsFileRepository, FilmeFileRepository, InchirieriFileRepository

if __name__ == "__main__":
    test_create_film()
    test_remove_film()
    test_update_film()
    test_create_client()
    test_remove_client()
    test_update_client()
    test_create_inchiriere()
    test_remove_inchiriere()
    test_primele_30()
    test_primii_30()
    test_cele_mai_inchiriate_filme()
    test_clienti_ord_nume()
    test_clienti_ord_nr_filme()
    test_serch_client()
    test_serch_film()
    test_update()
    test_remove()
    test_read()
    test_repo()

val = Validator()

c_repo = ClientRepository()
c_file = ClientsFileRepository("clienti")

f_file = FilmeFileRepository("filme")
f_repo = FilmRepository()

i_repo = InchirieriRepository()
i_file = InchirieriFileRepository("inchirieri")

fcontroler = FilmeService(val, f_file)
ccontroler = ClientService(val, c_file)
icontroler = InchirieriService(val, f_file, c_file, i_file)

ui = UI(fcontroler, ccontroler, icontroler)
ui.startUI()


