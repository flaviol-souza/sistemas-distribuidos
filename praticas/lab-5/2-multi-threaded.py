from time import sleep, perf_counter
from threading import Thread

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

if __name__ == '__main__':
    start_time = perf_counter()

    # create two new threads
    t1 = Thread(target=task)
    t2 = Thread(target=task)

    # fork
    t1.start()
    t2.start()

    # join
    t1.join()
    t2.join()

    end_time = perf_counter()

    #print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')
    print('It took {:0.2f} second(s) to complete.'.format(end_time - start_time))