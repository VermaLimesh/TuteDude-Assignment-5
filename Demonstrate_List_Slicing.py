# Task 2: Demonstrate List Slicing

list_of_no = [i for i in range(11) if i >= 1]                  # Creates a list of numbers from 1 to 10.

exct_list_of_no = list_of_no[0:5]                              # Extracts the first five elements from the list.

revs_list_of_no = exct_list_of_no[::-1]                        # Reverses these extracted elements.

print('Original list: ',list_of_no)
print('Extracted first five elements: ',exct_list_of_no)
print('Reversed extracted elements: ',revs_list_of_no)