from multiprocessing import Pool, cpu_count
import time

def double(x):
    """heavy function"""
    time.sleep(0.01)
    return x * 2

def multiprocess():
    worker = cpu_count() - 1
    start = time.perf_counter()
    with Pool(worker) as p:
        p.map(double, range(10*10))
    end = time.perf_counter()

    print(f"Multiprocess: {end - start}")

def singleprocess():
    start = time.perf_counter()
    for i in range(10*10):
        double(i)

    end = time.perf_counter()

    print(f"Singleprocess: {end - start}")

if __name__ == "__main__":
    multiprocess()
    singleprocess()