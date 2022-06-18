# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#from data.groups import testdata


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, json_groups, check_ui):
    #group = data_groups
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Contact.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)