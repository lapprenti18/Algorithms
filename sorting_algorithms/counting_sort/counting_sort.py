def find_bigest_number(array):
  best_num = array[0]

  for i in array:
    if i > best_num:
      best_num = i
  return best_num

def counting_sort(array):
  bigest_num = find_bigest_number(array)
  count_array = []

  for i in range(bigest_num + 1):
    count_array.append(array.count(i))
  
  index = 0
  for i in range(len(count_array)):
    for j in range(count_array[i]):
      array[index] = i
      index += 1
