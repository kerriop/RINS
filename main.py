import urllib.parse, requests
import prepods, enet

enet.initSession()
enet.setOrgId(open("org.txt").readline())
prepods.loadInput()

r = enet.loadPrepod(prepods.prepodsList[0])
print(r.text)