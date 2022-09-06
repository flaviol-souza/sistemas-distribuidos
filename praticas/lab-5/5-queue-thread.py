import time
from queue import Empty, Queue
from threading import Thread
from time import perf_counter

def producer(queue):
    for i in range(1, 6):
        print(f'Inserting item {i} into the queue')
        time.sleep(1)
        queue.put(i)

def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Processing item {item}')
            time.sleep(2)
            queue.task_done()

def main():
    start_time = perf_counter()

    queue = Queue()

    # create a producer thread and start it
    producer_thread = Thread(
        target=producer,
        args=(queue,)
    )
    producer_thread.start()

    # create a consumer thread and start it
    consumer_thread = Thread(
        target=consumer,
        args=(queue,),
        daemon=True
    )
    consumer_thread.start()

    producer_thread.join()

    queue.join()
    
    end_time = perf_counter()
    print(f'\nIt took {end_time- start_time :0.2f} second(s) to complete.')


if __name__ == '__main__':
    main()