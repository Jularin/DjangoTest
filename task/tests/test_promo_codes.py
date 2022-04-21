import json

from task.management.commands._utils import add_new_promo, search_code


def test_create():
    add_new_promo("10", "group")

    add_new_promo("10", "group2")
    add_new_promo("100", "group")


def test_searching():
    add_new_promo("10", "new group")
    search_code("123")
    search_code("123_dlas")
    with open("groups.json") as f:
        first_group: dict = json.load(f)[0]
        search_code(list(first_group.values())[0][0])
