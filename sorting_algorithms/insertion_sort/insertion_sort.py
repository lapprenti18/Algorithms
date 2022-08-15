def insert(array, index):
  current = array[index]
  i = index

  while (i > 0 and array[i - 1] > current):
    array[i] = array[i - 1]
    i = i - 1
  array[i] = current
  return

def insertion_sort(array):
  for i in range(2, len(array) + 1):
    insert(array, i - 1)
