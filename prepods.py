#все операции с преподавателями
class Prepod (object):
    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name

    def trace(self):
        print("[Prepod name='" + self.name + "']")

prepods_list = []
prepods_list.append(Prepod("Фамилия И.О."))

prepods_list[0].trace()