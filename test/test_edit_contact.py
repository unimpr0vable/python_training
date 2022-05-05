from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="1", lastname="1", nickname="1", company="1",
                               mobile="1", email="1"))
    app.session.logout()