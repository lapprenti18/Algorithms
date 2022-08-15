import time
import threading
from sorting_algorithms import *
import copy

number = "intermediate-tests/intermediate_09_unsorted_list_positive_and_negative_numbers_7"

def getFunctionTime(functionName, function, param):
  st = time.time()
  function(param)
  et = time.time()
  elapsed_time = et - st
  print('Execution time for ' + functionName +':', elapsed_time, 'seconds')


if __name__ == "__main__":
  array = list(map(int, open(number, "r").read().split(' ')))
  thread_pool = []

  thread_pool.append(threading.Thread(target=getFunctionTime('merge_sort', merge_sort, copy.deepcopy(array))))
  thread_pool.append(threading.Thread(target=getFunctionTime('heap_sort', heap_sort, copy.deepcopy(array))))
  thread_pool.append(threading.Thread(target=getFunctionTime('selection_sort', selection_sort, copy.deepcopy(array))))
  thread_pool.append(threading.Thread(target=getFunctionTime('insertion_sort', insertion_sort, copy.deepcopy(array))))
  thread_pool.append(threading.Thread(target=getFunctionTime('counting_sort', counting_sort, copy.deepcopy(array))))
  
  map(lambda thread: thread.start(), thread_pool)
  map(lambda thread: thread.join(), thread_pool)