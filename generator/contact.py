from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 7
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", company="", mobile="", email="")] + [
            Contact(firstname="Albina", lastname="Gurova", nickname="unimpr0vable", company="Liga", mobile="89428958606",
            email="albina.gurova@gmail.com", workphone= "89428958607", secondaryphone = "89428958608",
            homephone = "89428958609", address= "Kazan, Sibgata Hakima, 70", email2 = "albina.gurova2@gmail.com",
            email3 = "albina.gurova2@gmail.com")] + [
            Contact(firstname=random_string("name", 10), lastname=random_string("lastn", 15), nickname=random_string("nick", 15),
            company=random_string("comp", 15), mobile=random_string("", 10), email=random_string("@", 15),
            workphone= random_string("+7", 10), secondaryphone = random_string("8", 9), homephone = random_string("(8)", 7),
            address= random_string("address", 30), email2 = random_string("@", 15),  email3 = random_string("@", 15))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__ , indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))