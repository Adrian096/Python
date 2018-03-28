import re
regex_ip = re.compile(
    r'''(?P<IP>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
        ''',
    re.IGNORECASE | re.VERBOSE
)

f = open("tekst.txt")
dane =  f.read()
f.close()

for match_object in regex_ip.finditer(dane):
    print(match_object.groupdict())