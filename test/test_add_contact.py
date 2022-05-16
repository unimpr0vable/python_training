# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_list()
    contact = Contact(firstname="Albina", lastname="Gurova", nickname="unimpr0vable", company="Liga",
                               mobile="89638958605", email="albina.gurova@gmail.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", nickname="", company="", mobile="", email=""))
