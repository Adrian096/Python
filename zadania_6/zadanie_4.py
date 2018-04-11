import urllib2

response = urllib2.urlopen("https://www.python.org/")
html = response.read()

plik = open("tekst.txt" -w)
plik.write(html)

