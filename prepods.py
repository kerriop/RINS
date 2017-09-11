#Библиотека для работы со списком преподавателей

prepodsList = []

class Prepod (object):
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def trace(self):
        print("[Prepod name='" + self.name + "']")

def addPrepod(name):
    prepodsList.append(Prepod(name))

def trace():
    for p in prepodsList:
        p.trace()

def loadInput():
    with open("input.txt") as f: authors = f.readlines()
    authors = [x.strip() for x in authors]
    for author in authors:
        addPrepod(author)