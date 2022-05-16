from model.contact import Contact
import time

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    old_contacts = app.contact.get_list()
    app.contact.delete_first()
    time.sleep(1)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts