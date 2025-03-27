class Inchiriere():
    def __init__(self, idc, idf):
        self.__idc = idc
        self.__idf = idf

    def get_idf(self):
        return self.__idf

    def get_idc(self):
        return self.__idc

    def __str__(self):
        return f'Inchiriere(id client ={self.__idc}, id film={self.__idf})'

"""
1. fa ca o inchiriere sa mearga daca si numai daca exista id-ul in lista de cilenti si filme
2. returneaza == remove

"""