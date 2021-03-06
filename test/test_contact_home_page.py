import re
from random import randrange
from model.contact import Contact


def test_contacts_on_home_page(app, db):
    contacts_ui = sorted(app.contact.get_list(), key=Contact.id_or_max)
    contacts_bd = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for ui, bd in zip(contacts_ui, contacts_bd):
        assert [ui.firstname, ui.lastname, ui.address] == [
            bd.firstname.strip(), bd.lastname.strip(), bd.address.strip()]
        assert ui.all_emails_from_home_page == merge_emails_like_on_home_page(bd)
        assert ui.all_phones_from_home_page == merge_phones_like_on_home_page(bd)


def test_some_contact_on_home_page(app):
    old_contacts = app.contact.get_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert [contact_from_home_page.firstname, contact_from_home_page.lastname, contact_from_home_page.address] == [
        contact_from_edit_page.firstname, contact_from_edit_page.lastname, contact_from_edit_page.address]
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3])))