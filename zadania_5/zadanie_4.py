import re
regex_pesel = re.compile(
    r'''(?P<PESEL>\d{11}
        (?P<rok_urodzenia)\)
    ''',
    re.IGNORECASE | re.VERBOSE
)

f = open("tekst.txt")
dane =  f.read()
f.close()

for match_object in regex_pesel.finditer(dane):
    print(match_object.groupdict())