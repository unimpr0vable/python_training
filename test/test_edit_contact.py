from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test", nickname="test", company="test",
                               mobile="12345", email="test@mail.ru", workphone="12345", secondaryphone="12345",
                                homephone="12345", address="city street house", email2="test2@mail.ru",
                                email3="test3@mail.ru"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact_vars = Contact(firstname="1", lastname="1", nickname="1", company="1", mobile="1", email="1", workphone="1",
                         secondaryphone="1", homephone="1", address="1", email2="1", email3="1")
    contact_vars.id = contact.id
    app.contact.edit_by_index(index, contact_vars)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact_vars
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_list(), key=Contact.id_or_max)

#def test_edit_first_contact_firstname(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test"))
    #old_contacts = app.contact.get_list()
    #app.contact.edit_first(Contact(firstname="new_firstname"))
    #new_contacts = app.contact.get_list()
    #assert len(old_contacts) == app.contact.count()

#def test_edit_first_contact_lastname(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", lastname="test"))
    #old_contacts = app.contact.get_list()
    #app.contact.edit_first(Contact(lastname="new_lastname"))
    #new_contacts = app.contact.get_list()
    #assert len(old_contacts) == app.contact.count()