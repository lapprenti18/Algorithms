def bubble_sort(array):
  if len(array) == 1:
    return
  while 1:
    swapped = False
    for i in range(1, len(array), 1):
      if array[i - 1] > array[i]:
        array[i - 1], array[i] =  array[i], array[i - 1]
        swapped = True

      if swapped == False:
        return
