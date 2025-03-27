class Film():
    nrf=0
    def __init__(self, idf, titlu: str, descriere: str, gen: str):
        self.__Idf=idf
        self.__Titlu=titlu
        self.__Descriere=descriere
        self.__Gen=gen
        Film.nrf+=1

    def get_numar(self):
        return Film.nrf

    def get_idf(self):
        return self.__Idf

    def get_titlu(self):
        return self.__Titlu

    def get_descriere(self):
        return self.__Descriere

    def get_gen(self):
        return self.__Gen

    def set_idf(self, idf):
        self.__Idf=idf

    def set_titlu(self, titlu):
        self.__Titlu=titlu

    def set_descriere(self, descriere):
        self.__Descriere=descriere

    def set_gen(self, gen):
        self.__Gen=gen

    def __str__(self):
        return f'Film(idf={self.__Idf}, titlu={self.__Titlu}, descriere={self.__Descriere}, gen={self.__Gen})'

    def __eq__(self, other):
        if not isinstance(other, Film):
            return  False
        return self.get_idf() == other.get_idf()

def test_creare_client():
    f = Film(1,"Jumanji", "Dupa un joc", "Actiune")
    assert f.get_idf() == 1
    assert f.get_titlu() == "Jumanji"
    assert f.get_descriere() == "Dupa un joc"
    assert f.get_gen()=="Actiune"

test_creare_client()

def test_eq():
    f=Film(1,"Jumanji", "Dupa un joc", "Actiune")
    f1 =Film(1,"Jumanji", "Dupa un joc", "Actiune")
    assert f==f1

test_eq()