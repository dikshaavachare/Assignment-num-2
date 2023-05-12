def sort_tuple_last(tuples):
    return sorted(tuples, key=lambda x: x[-1])

# Sample List
list_of_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sorted List
sorted_list = sort_tuple_last(list_of_tuples)

print(sorted_list)
