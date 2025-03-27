from Lab7.Clase.validation import Validator, ValidatorException
from Lab7.repository.Film_repo import FilmRepository
from Lab7.repository.Client_repo import ClientRepository
from Lab7.repository.Inchirieri_repo import InchirieriRepository
from Lab7.services.Services import FilmeService, ClientService, InchirieriService
from Lab7.repository.File_repo import ClientsFileRepository, clearFileContent
from Lab7.Clase.client import Clietnt
from Lab7.Clase.film import Film

def test_create_film():
    fs= FilmeService(Validator(), FilmRepository())
    f = fs.create(1,"Fatherhood", "Emotional", "Drama")
    assert f.get_idf()==1
    assert f.get_titlu()=="Fatherhood"
    assert f.get_descriere()=="Emotional"
    assert f.get_gen()=="Drama"
    try:
        fs.create("","","","")
        assert False
    except ValidatorException:
        assert True

def test_remove_film():
    fs = FilmeService(Validator(), FilmRepository())
    f = fs.create(1,"Fatherhood", "Emotional", "Drama")
    try:
        fs.remove(2)
        assert False
    except ValueError:
        assert True
    f = fs.remove(1)
    assert fs.get_size()==0

def test_update_film():
    fs = FilmeService(Validator(), FilmRepository())
    f = fs.create(1, "Fatherhood", "Emotional", "Drama")
    f1 = fs.update(1, "Trolls", "Muzica", "Comedie")
    assert fs.get_size()==1
    assert fs.search(1)==f1
    try:
        f = fs.update(2, "Trolls", "Muzica", "Comedie")
        assert False
    except ValueError:
        assert True


def test_serch_film():
    fs = FilmeService(Validator(), FilmRepository())
    f = fs.create(1, "Fatherhood", "Emotional", "Drama")
    assert fs.search(1) == f

def test_create_client():
    cs = ClientService(Validator(), ClientRepository())
    c = cs.create(1, "Ion", "1233333333333")
    assert c.get_idc()==1
    assert c.get_nume()=="Ion"
    assert c.get_cnp() == "1233333333333"
    try:
        cs.create("","","")
    except ValidatorException:
        assert True

def test_remove_client():
    cs = ClientService(Validator(), ClientRepository())
    cs.create(1, "Ion", "1233333333333")
    try:
        cs.remove(2)
    except ValueError:
        assert True
    cs.remove(1)
    assert cs.get_size()==0

def test_update_client():
    cs = ClientService(Validator(), ClientRepository())
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.update(1,"Ana", "2345678765")
    assert cs.get_size()==1
    assert cs.search(1)==c1
    try:
        cs.update(2, "Ana", "2345678765")
        assert False
    except ValueError:
        assert True


def test_serch_client():
    cs = ClientService(Validator(), ClientRepository())
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.create(2, "Ana", "2345678765")
    assert cs.search(1)==c
    assert cs.search(2)==c1


def test_create_inchiriere():
    cr= ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.create(2, "Ana", "2345678765")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    iserv= InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1,2)
    assert i.get_idc()==1
    assert i.get_idf()==2
    try:
        iserv.create("","")
    except ValueError:
        assert True


def test_remove_inchiriere():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.create(2, "Ana", "2345678765")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    assert iserv.get_size() ==1
    iserv.remove(1,2)
    assert iserv.get_size()== 0

test_remove_inchiriere()

def test_clienti_ord_nr_filme():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ana", "1233333333333")
    c1 = cs.create(2, "Ion", "2345678765")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    f1 = fs.create(3, "Moxie", "Feminist", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    i1 = iserv.create(2, 2)
    i2 = iserv.create(2, 3)
    lista = iserv.clienti_ord_nr_filme()
    assert lista[0]==['Ion', ['Inchiriere(id client =2, id film=2)', 'Inchiriere(id client =2, id film=3)'], 2]


def test_clienti_ord_nume():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.create(2, "Ana", "2345678765")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    f1 = fs.create(3, "Moxie", "Feminist", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    i1 = iserv.create(2, 2)
    i2 = iserv.create(1, 3)
    lista = iserv.clienti_ord_nume()
    assert lista[0]=="Ana"


def test_cele_mai_inchiriate_filme():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ion", "1233333333333")
    c1 = cs.create(2, "Ana", "2345678765")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    f1 = fs.create(3, "Moxie", "Feminist", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    i1 = iserv.create(2, 2)
    i2 = iserv.create(1, 3)
    lista = iserv.cele_mai_inchiriate_filme()
    assert lista[0]==['Fatherhood', ['Inchiriere(id client =1, id film=2)', 'Inchiriere(id client =2, id film=2)'], 2]


def test_primii_30():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ana", "1233333333333")
    c1 = cs.create(2, "Ion", "2345678765")
    c2 = cs.create(5, "Marcel", "123454323")
    c3 = cs.create(7, "Mada", "7576767676")
    c4 = cs.create(9, "Lorena", "123454323")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    f1 = fs.create(3, "Moxie", "Feminist", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    i1 = iserv.create(2, 2)
    i2 = iserv.create(1, 3)
    i3 = iserv.create(5,2)
    i4 = iserv.create(7,2)
    i5 = iserv.create(9,3)
    i6 = iserv.create(9,2)
    lista = iserv.primii_30()
    assert lista[0]==['Ana', ['Inchiriere(id client =1, id film=2)', 'Inchiriere(id client =1, id film=3)'], 2]


def test_primele_30():
    cr = ClientRepository()
    fr = FilmRepository()
    cs = ClientService(Validator(), cr)
    c = cs.create(1, "Ana", "1233333333333")
    c1 = cs.create(2, "Ion", "2345678765")
    c2 = cs.create(5, "Marcel", "123454323")
    c3 = cs.create(7, "Mada", "7576767676")
    c4 = cs.create(9, "Lorena", "123454323")
    fs = FilmeService(Validator(), fr)
    f = fs.create(2, "Fatherhood", "Emotional", "Drama")
    f1 = fs.create(3, "Moxie", "Feminist", "Drama")
    iserv = InchirieriService(Validator(), fr, cr, InchirieriRepository())
    i = iserv.create(1, 2)
    i1 = iserv.create(2, 2)
    i2 = iserv.create(1, 3)
    i3 = iserv.create(5, 2)
    i4 = iserv.create(7, 2)
    i5 = iserv.create(9, 3)
    i6 = iserv.create(9, 2)
    lista = iserv.primele_30()
    assert lista==[['Fatherhood', ['Inchiriere(id client =1, id film=2)', 'Inchiriere(id client =2, id film=2)', 'Inchiriere(id client =5, id film=2)', 'Inchiriere(id client =7, id film=2)', 'Inchiriere(id client =9, id film=2)'], 5]]

def test_repo():
    file_neme = "clienti_test"
    clearFileContent(file_neme)
    repo = ClientsFileRepository(file_neme)
    assert repo.size() == 0
    c = Clietnt("1", "Ana", 123211232)
    repo.store(c)
    #assert repo.c_repo.size()==1
    clearFileContent(file_neme)
    

def test_read():
    file_name = "clienti_test"
    clearFileContent(file_name)
    repo = ClientsFileRepository(file_name)
    c = Clietnt("1", "Ana", 123211232)
    repo.store(c)
    repo.store(Clietnt("4", "Geo", 123211232))
    assert repo.repo.find(1) == c
    clearFileContent(file_name)


def test_remove():
    file_name = "clienti_test"
    repo = ClientsFileRepository(file_name)
    c = Clietnt("1", "Ana", 123211232)
    repo.store(c)
    repo.store(Clietnt("4", "Geo", 123211232))
    assert repo.repo.find(1)==c
    repo.remove(1)
    assert repo.repo.size()==1
    clearFileContent(file_name)


def test_update():
    file_name = "clienti_test"
    repo = ClientsFileRepository(file_name)
    c = Clietnt("1", "Ana", 123211232)
    repo.store(c)
    c2 = Clietnt("1", "Geo", 123211232)
    assert repo.repo.find(1) == c
    repo.update(1, c2)
    assert repo.repo.find(1)==c2
