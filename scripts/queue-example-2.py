import threading
import Queue

import time, random

WORKERS = 2

class Worker(threading.Thread):

    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            item = self.__queue.get()
            if item is None:
                break # reached end of queue

            # pretend we're doing something that takes 10-100 ms
            time.sleep(random.randint(10, 100) / 1000.0)

            print "task", item, "finished"

#
# run with limited queue

queue = Queue.Queue(3)

for i in range(WORKERS):
    Worker(queue).start() # start a worker

for item in range(10):
    print "push", item
    queue.put(item)

for i in range(WORKERS):
    queue.put(None) # add end-of-queue markers

## push 0
## push 1
## push 2
## push 3
## push 4
## push 5
## task 0 finished
## push 6
## task 1 finished
## push 7
## task 2 finished
## push 8
## task 3 finished
## push 9
## task 4 finished
## task 6 finished
## task 5 finished
## task 7 finished
## task 9 finished
## task 8 finished
