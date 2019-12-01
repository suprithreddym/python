import time
#from time import perf_counter as my_timer
#from time import monotonic as my_timer
from time import process_time as my_timer
import random

input("please enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("ended at " + time.strftime("%X", time.localtime(end_time)))
print("your reaction time is {} seconds".format(end_time - start_time))