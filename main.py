from ins_sort import *
from merge_sort import *
import random
import timeit
import matplotlib.pyplot as plt

def make_array(n, seed=5757):
    random.seed(seed)
    return [random.randint(0,15000) for i in range(n)]

def main():
    sizes = [1, 5, 25, 50]
    for i in range(100, 5001, 100):
        sizes.append(i)
    m_sort_times = []
    i_sort_times = []
    for n in sizes:
        data = make_array(n)

        m_sort_data = data.copy()
        start_time = timeit.default_timer()
        mergeSort(m_sort_data)
        end_time = timeit.default_timer()-start_time

        m_sort_times.append(end_time)

        i_sort_data = data.copy()
        start_time = timeit.default_timer()
        insertionSort(i_sort_data)
        end_time = timeit.default_timer() - start_time

        i_sort_times.append(end_time)

    plt.figure(figsize=(14,6))
    plt.plot(sizes, m_sort_times, label='Merge Sort')
    plt.plot(sizes, i_sort_times, label='Insertion Sort')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Timings')
    plt.legend()
    # plt.xticks(sizes[4:], rotation=45, ha='right')
    plt.grid(True)
    plt.savefig('./time_graph.png')

    plt.figure(figsize=(14,6))
    plt.plot(sizes[:8], m_sort_times[:8], label='Merge Sort')
    plt.plot(sizes[:8], i_sort_times[:8], label='Insertion Sort')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Timings, Small Values')
    plt.legend()
    # plt.xticks(sizes[4:], rotation=45, ha='right')
    plt.grid(True)
    plt.savefig('./time_graph_small.png')

    plt.show()
    return

if __name__ == '__main__':
    main()

