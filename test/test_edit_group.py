from model.group import Group

def test_edit_first_group(app):
    app.group.edit_first(Group(name="1", header="1", footer="1"))

def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="new_group_name"))

def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="new_group_header"))
