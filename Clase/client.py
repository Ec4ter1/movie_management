class Clietnt():
    """
    Represents a client
    """
    nrc=1
    def __init__(self, idc, nume, cnp):
        self.__Idc=idc
        self.__Nume= nume
        self.__Cnp= cnp
        Clietnt.nrc+=1

    def get_idc(self):
        return self.__Idc

    def get_nume(self):
        return self.__Nume

    def get_cnp(self):
        return self.__Cnp

    def set_idc(self, idc):
        self.__Idc=idc

    def set_nume(self, nume):
        self.__Nume= nume

    def set_cnp(self, cnp):
        self.__Cnp= cnp

    def __str__(self):
        return f'Client(idc={self.__Idc}, nume={self.__Nume}, cnp={self.__Cnp})'

    def __eq__(self, other):
        if not isinstance(other, Clietnt):
            return False
        return self.get_idc() == other.get_idc()

def test_creare_client():
    c = Clietnt(12,"Ana", 123)
    assert c.get_idc() == 12
    assert c.get_nume() == "Ana"
    assert c.get_cnp() == 123

test_creare_client()

def test_eq():
    c = Clietnt(1, "Ion", 123)
    c1 = Clietnt(1, "Ion", 123)
    assert c==c1

test_eq()