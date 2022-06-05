# -*- coding: utf-8 -*-
from model.group import Group
import pytest
#from data.groups import testdata


#@pytest.mark.parametrize("group", testdata, ids =[repr(x) for x in testdata])
def test_add_group(app, json_groups):
    #group = data_groups
    group = json_groups
    old_groups = app.group.get_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups.append(group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)