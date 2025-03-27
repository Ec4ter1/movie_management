from Lab7.Clase.client import Clietnt
from Lab7.Clase.film import Film
from Lab7.Clase.inchirieri import Inchiriere

class ValidatorException(Exception):
    def __init__(self, errors):
        self.__Errors = errors
    def getErrors(self):
        return self.__Errors

class Validator:
    def __init__(self):
        self.__accepted_gen=["Actiune", "Comedie", "Horror", "Drama"]
        self.__accepted_cnp_len = 6
    def validate_film(self, f: Film):
        errors = []
        if (f.get_idf() == ""): errors.append("Id can not be empty!")
        if (f.get_titlu() == ""): errors.append("Name can not be empty!")
        if (f.get_descriere() == ""): errors.append("Descriere can not be empty!")
        if (f.get_gen() == ""): errors.append("Gen can not be empty!")
        if f.get_gen() not in self.__accepted_gen:
            errors.append(f"Genre must be one of {self.__accepted_gen}")
        if len(errors) > 0:
            raise ValidatorException(errors)

    def validate_client(self, c: Clietnt):
        errors = []
        if (c.get_idc() == ""): errors.append("Id can not be empty!")
        if (c.get_nume() == ""): errors.append("Name can not be empty!")
        if (c.get_cnp() == ""): errors.append("Cnp can not be empty!")
        if len(c.get_cnp())<self.__accepted_cnp_len:
            errors.append(f"Cnp must be at least {self.__accepted_cnp_len} digits")
        if len(errors) > 0:
            raise ValidatorException(errors)

    def validate_inchiriere(self, i: Inchiriere):
        errors = []
        if (i.get_idc() == ""): errors.append("Id client can not be empty!")
        if (i.get_idf() == ""): errors.append("Id film can not be empty!")


def testFilmValidator():
    validator = Validator()
    f1 = Film("", "", "", "")
    try:
        validator.validate_film(f1)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 5

    f2 = Film(1234, "Fight Club", "misto", "Actiune")
    try:
        validator.validate_film(f2)
        assert True
    except ValidatorException as ex:
        assert False

def testClientValidator():
    validator = Validator()
    c1 = Clietnt("", "", "")
    try:
        validator.validate_client(c1)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 4

testFilmValidator()
testClientValidator()