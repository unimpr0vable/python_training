from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    app.group.edit_first(Group(name="1", header="1", footer="1"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    app.group.edit_first(Group(name="new_group_name"))

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header"))
    app.group.edit_first(Group(header="new_group_header"))
