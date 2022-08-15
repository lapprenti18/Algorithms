def find_lowest_number_index(array):
  min = 0

  for i in range(len(array)):
    if array[min] > array[i]:
      min = i
  return min


def selection_sort(array):
  for i in range(len(array)):
    lowest_number_index = find_lowest_number_index(array[i:]) 
    if lowest_number_index != 0:
      array[i] = array[lowest_number_index]
      array[lowest_number_index] = array[i]
