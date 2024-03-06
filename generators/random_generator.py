from random_resolvers.general_resolver import (
    name_resolver,
    weighted_random,
    distinct_random_integer,
    conditional_weighted_random,
    random_integer,
    sum_random_integer,
    random_string_from_files,
    subtract_random_date,
    distinct_sequence_integer,
)
from utils.file_manager import open_json_file


class RandomGenerator(object):
    def __init__(self, config_file_name):
        self.random_data = []
        self.config_file_name = config_file_name
        self.config = open_json_file(config_file_name)

    def generate(self, rows_count):
        random_data = []
        for i in range(rows_count):
            row_data = {}
            for column_name in self.config:
                column_data = self.config[column_name]
                if column_data["enabled"]:
                    row_value = self.__resolve_by_name(
                        column_name, column_data["resolver"], column_data["configuration"], row_data
                    )
                    row_data[column_name] = row_value

            random_data.append(row_data)

        self.random_data = random_data

        return random_data

    def print_data(self, format="json", file_name=None):
        ans = ""
        if format == "json":
            ans += str(self.random_data)
        elif format == "csv":
            if len(self.random_data) > 0:
                column = ""
                for k in self.random_data[0]:
                    column += k + ","
                ans += str(column[:-1]) + "\n"

            for i in self.random_data:
                row = ""
                for k in i:
                    row += str(i[k]) + ","
                ans += str(row[:-1]) + "\n"
        if file_name:
            with open(file_name, "w") as file:
                # Write the content to the file
                file.write(ans)
        else:
            print(ans)

    def __resolve_by_name(self, column_name, resolver_name, configuration, row_data):
        resolvers_map = {
            "random_name": name_resolver,
            "weighted_random": weighted_random,
            "distinct_random_integer": distinct_random_integer,
            "distinct_sequence_integer": distinct_sequence_integer,
            "conditional_weighted_random": conditional_weighted_random,
            "random_integer": random_integer,
            "sum_random_integer": sum_random_integer,
            "random_string_from_files": random_string_from_files,
            "subtract_random_date": subtract_random_date,
        }

        if resolver_name not in resolvers_map:
            raise Exception("Resolver with name {0} not found for column {1}".format(resolver_name, column_name))

        return resolvers_map[resolver_name](row_data, configuration)
