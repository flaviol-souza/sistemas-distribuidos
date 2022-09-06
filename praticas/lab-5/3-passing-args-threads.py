from time import sleep, perf_counter
from threading import Thread


def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')

if __name__ == '__main__':
    start_time = perf_counter()

    # create and start 10 threads
    threads = []
    for n in range(1, 11):
        t = Thread(target=task, args=(n,))
        threads.append(t)
        t.start()

    # wait for the threads to complete
    for t in threads:
        t.join()

    end_time = perf_counter()

    print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')