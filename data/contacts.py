from model.contact import Contact
import random
import string

testdata = [
    Contact(firstname="firstname1", lastname="lastname1", nickname="nickname1", company="company1", mobile="mobile1",
            email="email1", workphone="workphone1", secondaryphone="secondaryphone1",
            homephone="homephone1", address="address1", email2="email12", email3="email13"),
    Contact(firstname="firstname2", lastname="lastname2", nickname="nickname2", company="company2", mobile="mobile2",
            email="email2", workphone="workphone2", secondaryphone="secondaryphone2",
            homephone="homephone2", address="address2", email2="email22", email3="email23")
]


#def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + " "*10
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Contact(firstname="", lastname="", nickname="", company="", mobile="", email="")] + [
            #Contact(firstname="Albina", lastname="Gurova", nickname="unimpr0vable", company="Liga", mobile="89428958606",
            #email="albina.gurova@gmail.com", workphone= "89428958607", secondaryphone = "89428958608",
            #homephone = "89428958609", address= "Kazan, Sibgata Hakima, 70", email2 = "albina.gurova2@gmail.com",
            #email3 = "albina.gurova2@gmail.com")] + [
            #Contact(firstname=random_string("name", 10), lastname=random_string("lastn", 15), nickname=random_string("nick", 15),
            #company=random_string("comp", 15), mobile=random_string("", 10), email=random_string("@", 15),
            #workphone= random_string("+7", 10), secondaryphone = random_string("8", 9), homephone = random_string("(8)", 7),
            #address= random_string("address", 30), email2 = random_string("@", 15),  email3 = random_string("@", 15))
            #for i in range(7)]