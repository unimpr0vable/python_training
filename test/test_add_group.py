# -*- coding: utf-8 -*-
from model.group import Group
import allure
#from data.groups import testdata


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, db, json_groups, check_ui):
    #group = data_groups
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)
    with allure.step('Then yhe new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Contact.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)