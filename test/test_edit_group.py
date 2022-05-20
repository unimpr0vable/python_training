from model.group import Group
from random import randrange

def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    group = Group(name="1", header="1", footer="1")
    group.id = old_groups[index].id
    app.group.edit_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name"))
    old_groups = app.group.get_list()
    app.group.edit_first(Group(name="new_group_name"))
    #new_groups = app.group.get_list()
    assert len(old_groups) == app.group.count()

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_name", header="test_header"))
    old_groups = app.group.get_list()
    app.group.edit_first(Group(header="new_group_header"))
    #new_groups = app.group.get_list()
    assert len(old_groups)  == app.group.count()
