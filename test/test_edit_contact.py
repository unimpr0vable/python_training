from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="1", lastname="1", nickname="1", company="1",
                               mobile="1", email="1"))
    app.session.logout()

def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="new_firstname"))
    app.session.logout()

def test_edit_first_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(lastname="new_lastname"))
    app.session.logout()