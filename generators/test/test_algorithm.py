import unittest

from generators.random_generator import RandomGenerator


class RandomGeneratorTest(unittest.TestCase):
    def test_random_gen(self):
        options = [1, 10, 100, 1000]
        for i in options:
            generator = RandomGenerator("random_configuration.json")
            data = generator.generate(rows_count=i)
            self.assertEqual(i, len(data))

    def test_print_empty_data(self):
        generator = RandomGenerator("random_configuration.json")
        generator.print_data(format="csv")
        self.assertEqual(True, True)

    def test_print_data_json(self):
        options = [1, 10, 100, 1000]
        for i in options:
            generator = RandomGenerator("random_configuration.json")
            generator.generate(rows_count=i)
            generator.print_data(format="json")
            self.assertEqual(True, True)

    def test_print_data_csv(self):
        options = [1, 10, 100, 1000]
        for i in options:
            generator = RandomGenerator("random_configuration.json")
            generator.generate(rows_count=i)
            generator.print_data(format="csv")
            self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
