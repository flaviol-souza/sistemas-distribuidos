from threading import Thread
from time import sleep

counter = 0

def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')

t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'The final counter is {counter}')