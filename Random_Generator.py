import random
from string import ascii_lowercase, ascii_uppercase
from Lab7.Clase.film import Film
from Lab7.repository.Film_repo import FilmRepository
from Lab7.repository.Client_repo import ClientRepository
from Lab7.Clase.validation import Validator, ValidatorException
from Lab7.services.Services import FilmeService, ClientService

def random_list_id():
    randomlist = []
    for i in range(0, 8):
        n = random.randint(1, 30)
        if n not in randomlist:
            randomlist.append(n)
    return randomlist

def random_name():
    a= random.randint(1,22)
    film_nume = ""
    prima_litera=random.choice(ascii_uppercase)
    film_nume+=prima_litera
    for i in range(1,a):
        litera=random.choice(ascii_lowercase)
        film_nume+=litera
    return film_nume

def random_gen():
    x = random.randint(0, 3)
    list_of_genras= ["Actiune", "Comedie", "Horror", "Drama"]
    return list_of_genras[x]

def random_cnp():
    x = random.randint(100000,10000000)
    return str(x)

def test_random_id_list():
    random.seed(0)
    l = random_list_id()
    assert l == [28, 13, 25, 29, 14, 2, 9, 17]

test_random_id_list()

def test_random_name():
    random.seed(0)
    name = random_name()
    assert name == "Ynbiqpmzjplsg"


test_random_name()

def test_random_gen():
    random.seed(0)
    gen = random_gen()
    assert gen == "Drama"

test_random_gen()

def test_random_cnp():
    random.seed(0)
    cnp = random_cnp()
    assert cnp == "6563343"

test_random_cnp()