from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group_vars = Group(name="1", header="1", footer="1")
    group_vars.id = group.id
    app.group.edit_by_id(group.id, group_vars)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_vars
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)


#def test_edit_first_group_name(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test_name"))
    #old_groups = app.group.get_list()
    #app.group.edit_first(Group(name="new_group_name"))
    #new_groups = app.group.get_list()
    #assert len(old_groups) == app.group.count()

#def test_edit_first_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test_name", header="test_header"))
    # old_groups = app.group.get_list()
    #app.group.edit_first(Group(header="new_group_header"))
    #new_groups = app.group.get_list()
    #assert len(old_groups)  == app.group.count()
