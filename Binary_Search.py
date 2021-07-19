# Here a list is given with integer numbers and we are going to implement BINARY SEARCH ALGO
# to find a value from that list.

# The given list.
given_list= [5,7,3,6,4,9,8,1]

# The given value that wil be searched in the list
given_value= 5

# First thing we need to do is we need to sort the list. Cause Binary Search doesn't work for an unsorted list.
given_list.sort() # sort the list
print('The sorted given list is ',given_list)
print('The given value is ', given_value)





def binary_search(list,value):
    # Initialization
    starting_index_for_searching = 0
    end_index_for_searching = len(list) - 1  # -1 as index starts from 0.
    value_found=False
    while (starting_index_for_searching<=end_index_for_searching and value_found==False):
        mid_point = int((starting_index_for_searching+end_index_for_searching)/2) # Here floor value wil be picked.
        if(value==list[mid_point]):
            value_found=True
            print('Given value found in index number ', mid_point, 'using binary search')
        elif(value>list[mid_point]):
            starting_index_for_searching=mid_point+1
            # As value belongs to the right of mid_point so gonna search from
            # the very next index of mid_point to end of the list
        else:
            end_index_for_searching=mid_point-1
            # As value belongs to the left of mid_point so gonna search from
            # starting index to previous index of mid_point


binary_search(given_list,given_value)

# Rifat




