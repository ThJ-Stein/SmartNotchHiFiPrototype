import urllib2
def IP():
    IP=urllib2.urlopen('http://ip.42.pl/raw').read()
    return IP

if __name__ == "__main__":
    print IP()