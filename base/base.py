import time

from base import data_generator
from utils import constants


class BaseSortingTimeGather(object):
    def __init__(self, algorithms):
        self.algorithms = algorithms

    def take_execution_time(self, minimum_size, maximum_size, step, samples_by_size):
        return_table = []

        for size in range(minimum_size, maximum_size + 1, step):
            table_row = [size]
            times = self.take_times(size, samples_by_size)
            return_table.append(table_row + times)

        return return_table

    """
        It will return three values, one for each algorithm: The execution time for that size on each algorithm
    """

    def take_times(self, size, samples_by_size):
        samples = []
        for _ in range(samples_by_size):
            samples.append((sorted(data_generator.get_random_list(size)), data_generator.get_random_x()))

        return [self.take_time_for_algorithm(samples, x) for x in self.algorithms]

    """
        Returns the median of the execution time measures for a sorting approach given in 
    """

    def take_time_for_algorithm(self, samples_array, sorting_approach):
        times = []

        for sample in samples_array:
            start_time = time.time()
            sorting_approach(sample[0], sample[1])
            times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

        times.sort()
        return times[len(times) // 2]
