import random
import time
import queue_time


from matplotlib import pyplot as plt

import ctypes

# Load the shared library
libqueue = ctypes.CDLL('./libqueue.so')  # Replace with the path to your library

# Define the argument and return types
libqueue.queue_time.restype = ctypes.c_int
libqueue.queue_time.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
libqueue.queue_time_optimized.restype = ctypes.c_int
libqueue.queue_time_optimized.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]

def main():

    test_1(queue_time.queue_time_optimized)
    test_2(queue_time.queue_time_optimized)
    test_3(queue_time.queue_time_optimized)
    test_4(queue_time.queue_time_optimized)
    test_5(queue_time.queue_time_optimized)
    test_6(queue_time.queue_time_optimized)

    times_1 = test_random_c([libqueue.queue_time, libqueue.queue_time_optimized])
    times_2 = test_random([queue_time.queue_time, queue_time.queue_time_optimized])

    display_results(times_2, ["queue_time", "queue_time_optimized"], "python implementations")
    display_results(times_1, ["queue_time", "queue_time_optimized"], "C implementations")

    print("All tests passed")


def test_1( solver):
    customers = [5, 3, 4]
    n = 1
    assert solver(customers, n) == 12

def test_2(solver):
    customers = [10, 2, 3, 3]
    n = 2
    assert solver(customers, n) == 10

def test_3(solver):
    customers = [2, 3, 10]
    n = 2
    assert solver(customers, n) == 12

def test_4(solver):
    customers = [1, 2, 3, 4, 5]
    n = 1
    assert solver(customers, n) == 15

def test_5(solver):
    customers = [1, 2, 3, 4, 5]
    n = 2
    assert solver(customers, n) == 9

def test_6(solver):
    customers = [5, 2, 7, 2, 5, 1, 7]
    n = 3
    assert solver(customers, n) == 13

def test_random(solvers):
    times = [[] for _ in range(len(solvers))]
    for i in range(2, 1000):
        customers = [random.randint(1, 10) for _ in range(i)]
        n = random.randint(1, 10)
        solution = solvers[0](customers, n)
        for j, solver in enumerate(solvers):
            start = time.time()
            assert solution == solver(customers, n)
            times[j].append(time.time() - start)
    return times

def display_results(time, solvers_names, title):

        for i, t in enumerate(time):
            new_array = []
            for j in range(0, len(t)-1, 10):
                average = sum(t[j:j+10]) / 10
                new_array.append(average)
            time[i] = new_array


        for i, t in enumerate(time):
            plt.plot(t, label=solvers_names[i])
        
        plt.xlabel("Test Case")
        plt.ylabel("Time")
        plt.title(title)
        plt.legend()
        plt.show()

def test_random_c(solvers):
    times = [[] for _ in range(len(solvers))]
    for i in range(1000, 10000, 10):
        customers = [random.randint(1, 10) for _ in range(i)]
        num_customers = len(customers)
        customers_c = (ctypes.c_int * num_customers)(*customers)
        n = random.randint(1, 10)
        solution = solvers[0](customers_c, num_customers,  n)
        for j, solver in enumerate(solvers):
            start = time.time()
            solver(customers_c, num_customers, n)
            times[j].append(time.time() - start)
    return times

if __name__ == "__main__":
    main()
