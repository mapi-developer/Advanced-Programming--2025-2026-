import time
import matplotlib.pyplot as plt
from os import linesep
import random


def progress_bar(current, total, bar_length=50):
    """
    Given a value for CURRENT step out of TOTAL steps, this function will draw a progress bar reflecting the ratio between the two.
    When CURRENT == TOTAL, the progress bar will reach 100% and will terminate with a newline.
    """
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '#' + '>'
    padding = (bar_length - len(arrow)) * ' '
    end_char = linesep if current == total else '\r'
    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=end_char)


def measure_and_plot(algo, inputs, input_sizes, n_runs=100):
    """
    Performs multiple runs of an algorithm, measures the time it takes to complete it and plots the results. The plot will contain:
    - the average running time per input size
    - the minimum and maximum running time per input size
    Inputs to this function:
    - algo: an algorithm with some number of inputs
    - inputs: a list of iterables that each serve as a different input to the algo
    - input_sizes: a list of integer values, each corresponding to a different input in inputs and characterizing the 'size' of that input.
    These sizes will be used as coordinates along the horizontal axis in the plot.
    Ideally, several inputs will have the same sizes, since e.g. the running time of a sort algorithm might depend heavily on the initial ordering of
    the items. This is why we will display a minimum and maximum running time as well...
    - n_runs: the number of times the algorithm is run for each of the inputs
    """
    avg_times_per_size = dict()
    min_max_avg_times_per_size = dict()
    num_inputs = len(inputs)

    for inputt_ix, inputt in enumerate(inputs):
        progress_bar(inputt_ix+1, num_inputs)
        inputt_sz = input_sizes[inputt_ix]
        
        start_time = time.process_time()
        for time_ix in range(n_runs):
            algo(inputt)
        end_time = time.process_time()
        
        total_time = (end_time - start_time)
        average_time = total_time / n_runs
        
        if avg_times_per_size.get(inputt_sz) is not None:
            ## yes, it's possible that the same input size will have multiple average times
            ## associated with it in the dictionary, since we don't know how many inputs will be contained
            ## in the inputs parameter that have the same sizes
            avg_times_per_size[inputt_sz].append(average_time)
        else:
            avg_times_per_size[inputt_sz] = [average_time]

    for (sz, avg_times) in avg_times_per_size.items():
        if min_max_avg_times_per_size.get(sz) is None:
            min_max_avg_times_per_size[sz] = dict()
        min_max_avg_times_per_size[sz]['min'] = min(avg_times)
        min_max_avg_times_per_size[sz]['max'] = max(avg_times)
        min_max_avg_times_per_size[sz]['avg'] = sum(avg_times) / len(avg_times)

    all_items = list(min_max_avg_times_per_size.items())
    all_items.sort(key=lambda x: x[0])

    plt.figure(figsize=(6,6)) ## use square aspect ratio
    plt.scatter([kv[0] for kv in all_items], [kv[1]['avg'] for kv in all_items], marker='o', color='blue')
    plt.scatter([kv[0] for kv in all_items], [kv[1]['min'] for kv in all_items], marker='^', color='green')
    plt.scatter([kv[0] for kv in all_items], [kv[1]['max'] for kv in all_items], marker='x', color='red')
    plt.xlabel('Input Size')
    plt.ylabel('Average Running Time (seconds)')
    plt.title('Algorithm Running Time Analysis')
    plt.show()


def test_sort_algo(algo, n_sizes=1500, jumps_in_size=10, n_inputs_per_size=10, value_bound=100):
    inputs = []
    sizes = []

    for size in range(1,n_sizes+1,jumps_in_size):
        for _ in range(n_inputs_per_size):
            inputs.append([random.randint(1,value_bound) for _ in range(size)])
            sizes.append(size)

    measure_and_plot(algo, inputs, sizes)