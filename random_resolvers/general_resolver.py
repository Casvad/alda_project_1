import random
from datetime import datetime, timedelta

from utils.file_manager import open_csv_file
from utils.random_util import get_random_in_list, get_wighted_attribute, get_random_x

distinct_random_map = {}


def conditional_weighted_random(row_data, resolver_configuration):
    weighted_attributes = resolver_configuration["weighted_attributes"]
    conditional_column = resolver_configuration["conditional_column"]

    for weighted_attribute in weighted_attributes:
        if weighted_attribute["value"] == row_data[conditional_column]:
            return get_wighted_attribute(weighted_attribute["options"])

    return ""


def sum_random_integer(row_data, resolver_configuration):
    min_value = resolver_configuration["min_value"]
    max_value = resolver_configuration["max_value"]
    random_value = get_random_x(min_value, max_value)

    return row_data[resolver_configuration["column_name"]] + random_value


def random_integer(row_data, resolver_configuration):
    min_value = resolver_configuration["min_value"]
    max_value = resolver_configuration["max_value"]
    random_value = get_random_x(min_value, max_value)

    return random_value


def distinct_sequence_integer(row_data, resolver_configuration):
    distinct_id = resolver_configuration["distinct_id"]
    if distinct_id not in distinct_random_map:
        distinct_random_map[distinct_id] = -1
    distinct_random_map[distinct_id] += 1

    return distinct_random_map[distinct_id]

def distinct_random_integer(row_data, resolver_configuration):
    distinct_id = resolver_configuration["distinct_id"]
    min_value = resolver_configuration["min_value"]
    max_value = resolver_configuration["max_value"]
    if distinct_id not in distinct_random_map:
        distinct_random_map[distinct_id] = {}

    random_value = get_random_x(min_value, max_value)
    while random_value in distinct_random_map[distinct_id]:
        random_value = get_random_x(min_value, max_value)
    distinct_random_map[distinct_id][random_value] = random_value

    return random_value


def weighted_random(row_data, resolver_configuration):
    weighted_attributes = resolver_configuration["weighted_attributes"]
    other_attributes = resolver_configuration["other_attributes"] or []
    add_other_attributes = resolver_configuration.get("add_other_attributes", True)

    if add_other_attributes:
        resolver_configuration["add_other_attributes"] = False
        random.shuffle(other_attributes)
        for other_attribute in other_attributes:
            weighted_attributes.append({
                "value": other_attribute,
                "weight": 1,
            })

    return get_wighted_attribute(weighted_attributes)


def name_resolver(row_data, resolver_configuration):
    primary_name = open_csv_file(resolver_configuration["primary_name"])

    random_name, gender = get_random_in_list(primary_name)
    if resolver_configuration["second_name"]:
        second_name = open_csv_file(resolver_configuration["second_name"])
        random_second_name, gender = get_random_in_list(second_name, condition=(lambda x: x[1] == gender))

        random_name += " " + random_second_name
    if resolver_configuration["first_last_name"]:
        first_last_name = open_csv_file(resolver_configuration["first_last_name"])
        random_name += " " + get_random_in_list(first_last_name)[0]
    if resolver_configuration["second_last_name"]:
        second_last_name = open_csv_file(resolver_configuration["second_last_name"])
        random_name += " " + get_random_in_list(second_last_name)[0]

    return random_name


def random_string_from_files(row_data, resolver_configuration):
    file_names = resolver_configuration["files"]
    separator = resolver_configuration["separator"]
    ans = ""
    for file in file_names:
        file_content = open_csv_file(file)
        ans += separator + get_random_in_list(file_content)[0]

    return ans


def subtract_random_date(row_data, resolver_configuration):
    current_date = datetime.now()
    min_value = resolver_configuration["min_value"]
    max_value = resolver_configuration["max_value"]
    result_date = current_date - timedelta(days=get_random_x(min_value, max_value))

    return result_date.strftime("%Y-%m-%d")  #To add hours use this %H:%M:%S
