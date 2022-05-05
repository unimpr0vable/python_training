# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Albina", lastname="Gurova", nickname="unimpr0vable", company="Liga",
                               mobile="89638958605", email="albina.gurova@gmail.com"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", nickname="", company="", mobile="", email=""))
    app.session.logout()
