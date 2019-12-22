def highest_even(li):
    sorted_li = sorted(li)
    for number in range(len(sorted_li), 0, -1):
        if number % 2 == 0:
            return sorted_li[number - 1]


print(highest_even([10, 1, 2, 3, 4, 8]))

# Andrei way

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))