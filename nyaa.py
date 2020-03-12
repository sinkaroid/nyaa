import pycurl
import certifi

ext = '.php'

nekopoi = 'https://raw.githubusercontent.com/sinkaroid/poifeed/master/feed.php'
anitoki = 'https://raw.githubusercontent.com/sinkaroid/anti/master/page/feed/index.php'
samehada = 'https://raw.githubusercontent.com/sinkaroid/Smhdk/master/src/feed.php'
oplovers = 'https://raw.githubusercontent.com/sinkaroid/erza/master/page/feed.php'
hentaimama = 'https://gist.githubusercontent.com/sinkaroid/29f669dc986dcc39edfd064b69982cbd/raw/1e1c07cf1fa58d8d5569a210e6adae414ee37672/gistfile1.txt'
def main():
    
    c = pycurl.Curl()
    c.setopt(c.URL,FILE_SRC)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
    return

FILE_DEST = './feeds/nekopoi'+ext
FILE_SRC = nekopoi
with open(FILE_DEST, 'wb') as f:
    main()

FILE_DEST = './feeds/anitoki'+ext
FILE_SRC = anitoki
with open(FILE_DEST, 'wb') as f:
    main()

FILE_DEST = './feeds/samehada'+ext
FILE_SRC = samehada
with open(FILE_DEST, 'wb') as f:
    main()

FILE_DEST = './feeds/oplovers'+ext
FILE_SRC = oplovers
with open(FILE_DEST, 'wb') as f:
    main()

FILE_DEST = './feeds/hentaimama'+ext
FILE_SRC = hentaimama
with open(FILE_DEST, 'wb') as f:
    main()    