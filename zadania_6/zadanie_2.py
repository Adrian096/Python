import re


class check(Exception):
    emails = []

    def __init__(self, email):

        if not re.match('[^@]+@[^@]+\.[^@]+', email):
            raise Exception("Niepoprawny adres email!")
        else:
            self.emails.append(email)
            
klasa = check("KtosTamo2.pl")

        
