from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, company=None, mobile=None, workphone = None,
                 secondaryphone = None, homephone = None, email=None, email2=None, email3=None, address=None, id = None,
                  all_phones_from_home_page = None, all_emails_from_home_page = None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.homephone = homephone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.address = address
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and \
               self.firstname == other.firstname