from model.group import Group
from model.contact import Contact
import random

def test_del_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="test", nickname="test", company="test",
                               mobile="12345", email="test@mail.ru", workphone="12345", secondaryphone="12345",
                                homephone="12345", address="city street house", email2="test2@mail.ru",
                                email3="test3@mail.ru"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))

    group = random.choice(orm.get_group_list())
    contact = random.choice(orm.get_contact_list())

    if contact not in orm.get_contacts_in_group(group):
        app.contact.add_to_group(contact.id, group.id)
    #if assert not work then precondition not work
    assert contact in orm.get_contacts_in_group(group)

    app.contact.del_from_group(contact.id, group.id)

    assert contact not in orm.get_contacts_in_group(group)