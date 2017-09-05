#все операции с преподавателями

prepods_list = []

class Prepod (object):
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def trace(self):
        print("[Prepod name='" + self.name + "']")

def add_prepod(name):
    prepods_list.append(Prepod(name))

def trace():
    for p in prepods_list:
        p.trace()