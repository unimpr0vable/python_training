from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.edit_first(Contact(firstname="1", lastname="1", nickname="1", company="1",
                               mobile="1", email="1"))

def test_edit_first_contact_firstname(app):
    app.contact.edit_first(Contact(firstname="new_firstname"))

def test_edit_first_contact_lastname(app):
    app.contact.edit_first(Contact(lastname="new_lastname"))