from generators.random_generator import RandomGenerator


def run_random_generator():
    generator = RandomGenerator("random_configuration.json")
    generator.generate(rows_count=100)
    generator.print_data(format="csv", file_name="out.csv")


if __name__ == '__main__':
    run_random_generator()
