import random

from utils.constants import MAX_VALUE


def get_random_x(init=0, limit=MAX_VALUE):
    return random.randint(init, limit - 1)


def get_random_in_list(input_list, condition=(lambda x: True)):
    index = get_random_x(limit=len(input_list))
    while not condition(input_list[index]):
        index = get_random_x(limit=len(input_list))
    return input_list[index]


def get_wighted_attribute(weighted_list):
    sorted_attributes = sorted(weighted_list, key=lambda x: x["weight"], reverse=True)
    total_weight = sum(attribute["weight"] for attribute in sorted_attributes)
    random_number = random.uniform(0, total_weight)

    cumulative_weight = 0
    for attribute in sorted_attributes:
        cumulative_weight += attribute["weight"]
        if random_number < cumulative_weight:
            return attribute["value"]
