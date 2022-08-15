def merge(array, left, right):
  index = 0

  while len(left) and len(right):
    if left[0] < right[0]:
      array[index] = left.pop(0)
    else:
      array[index] = right.pop(0)
    index += 1
  while len(left):
    array[index] = left.pop(0)
    index += 1
  while len(right):
    array[index] = right.pop(0)
    index += 1
  return

def merge_sort(array):
  if (len(array)<=1):
    return

  mid = len(array)//2
  left = array[:mid]
  right = array[mid:]

  merge_sort(left)
  merge_sort(right)
  merge(array, left, right)
  return array
