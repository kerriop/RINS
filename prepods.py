#Библиотека для работы со списком преподавателей
from bs4 import BeautifulSoup

prepodsList = []

#Класс - структура преподавателя
class Prepod (object):
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def trace(self):
        print("[Prepod name='" + self.name + "']")

#Добавить преподавателя
def addPrepod(name):
    prepodsList.append(Prepod(name))

#Вывод содержимого базы
def trace():
    for p in prepodsList:
        p.trace()

#Загрузить базу с файла input.txt
def loadInput():
    with open("input.txt") as f: authors = f.readlines()
    authors = [x.strip() for x in authors]
    for author in authors:
        addPrepod(author)

#Разбор преподавателей из общей страницы поиска
def parsePrepods(r, prepod):
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find("table", {"id": "restab"})
    if table is None:
        print("Автор не найден (" + prepod + ")")
        return
    print("Авторы найдены!")