# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

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
            for i in range(7)]

@ pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
