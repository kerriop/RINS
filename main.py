import urllib.parse, requests
import prepods, enet

print('Инициализация...')
enet.initSession()
enet.setOrgId(open("org.txt").readline())
prepods.loadInput()

for prepod in prepods.prepodsList:
    print('Посылаю запрос на поиск автора: ' + prepod.getName())
    r = enet.loadPrepod(prepod)
    prepods.parsePrepods(r, prepod.getName())

