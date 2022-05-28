import re

def test_phones_on_home_page(app):
    first_contact_from_home_page = app.contact.get_list()[0]
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(first_contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    first_contact_from_view_page = app.contact.get_contact_from_view_page(0)
    first_contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert first_contact_from_edit_page.mobile == first_contact_from_view_page.mobile
    assert first_contact_from_edit_page.workphone == first_contact_from_view_page.workphone
    assert first_contact_from_edit_page.secondaryphone == first_contact_from_view_page.secondaryphone
    assert first_contact_from_edit_page.homephone == first_contact_from_view_page.homephone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                        [contact.homephone, contact.workphone, contact.mobile, contact.secondaryphone]))))