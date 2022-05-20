from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test", nickname="test", company="test",
                               mobile="12345", email="test@mail.ru"))
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="1", lastname="1", nickname="1", company="1",
                               mobile="1", email="1")
    contact.id = old_contacts[index].id
    app.contact.edit_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_list()
    app.contact.edit_first(Contact(firstname="new_firstname"))
    #new_contacts = app.contact.get_list()
    assert len(old_contacts) == app.contact.count()

def test_edit_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    old_contacts = app.contact.get_list()
    app.contact.edit_first(Contact(lastname="new_lastname"))
    #new_contacts = app.contact.get_list()
    assert len(old_contacts) == app.contact.count()