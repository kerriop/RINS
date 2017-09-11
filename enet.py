#Библиотека для загрузки страниц без авторизации
import requests, prepods
cookie = None
orgid = 0
session = None

#Установить id организации
def setOrgId(oid):
    global orgid
    orgid = oid

#Инициализировать cookie для доступа к сайту
def initSession():
    global session, cookie
    session = requests.Session()
    r = session.post('http://elibrary.ru/')
    cookie = session.cookies.get_dict()

#Произвести поиск по имени
def loadPrepod(prepod):
    return session.post('https://elibrary.ru/authors.asp?surname=' + prepod.getName() + '&sortorder=0&order=0&orgid=' + str(orgid), cookies=cookie)