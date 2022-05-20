from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.open_page_add_new()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_page_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and
                len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()

    def delete_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_contact_page()
        self.contact_cache = None

    def delete_first(self):
        self.delete_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_some_contact_for_edit(index)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first(self, contact):
        self.edit_by_index(0, contact)

    def select_first_contact_for_edit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()

    def select_some_contact_for_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("company", contact.company)
        self.change_field("mobile", contact.mobile)
        self.change_field("email", contact.email)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tbody/tr[@name='entry']"):
                firstname = element.find_element_by_xpath(".//td[3]").text
                lastname = element.find_element_by_xpath(".//td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname = firstname, lastname = lastname, id = id))
        return list(self.contact_cache)

