import json
from uuid import uuid4
from typing import List, Dict


def read_data() -> List[Dict]:
    try:
        with open("groups.json") as f:
            try:
                groups = json.load(f)
            except json.decoder.JSONDecodeError:
                return []
        return groups
    except FileNotFoundError:
        return []


def write_data(out_dict: List[Dict]):
    with open("groups.json", 'w') as f:
        json.dump(out_dict, f, indent=4)


def add_new_promo(amount: str, group_name: str):
    groups = read_data()
    new_codes = [group_name + "__" + str(uuid4()) for i in range(int(amount))]

    for group in groups:
        if group.get(group_name) is not None:
            group[group_name] += new_codes

            write_data(groups)
            return

    groups += [{group_name: new_codes}]
    write_data(groups)


def search_code(code: str) -> bool:
    groups = read_data()
    group_name = code.split("__")[0]

    for group in groups:
        if group.get(group_name) is not None:
            for promo in group.get(group_name):
                if promo == code:
                    return True
            return False
    return False


