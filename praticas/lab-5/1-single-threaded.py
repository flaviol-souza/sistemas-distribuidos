from time import sleep, perf_counter

def task():
    print('Starting a task...')
    sleep(1)
    print('done')

if __name__ == '__main__':
    start_time = perf_counter()
    task()
    task()
    end_time = perf_counter()

    print(f'It took {end_time - start_time: 0.2f} second(s) to complete.')