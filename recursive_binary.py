import copy
import random


def recursive_binary(list, element, first_element_no, last_element_no):

    mid = int((first_element_no + last_element_no)/2)
    print(mid)
    if element == list[mid]:
        print("the mid is", mid)
        result = mid
        return result
    elif element < list[mid]:
        result = recursive_binary(list, element, first_element_no, mid-1)
        return result
    elif element > list[mid]:
        result = recursive_binary(list, element, mid+1, last_element_no)
        return result

        #testcasebelow

ordered_list = list(random.sample(range(100), 10))
ordered_list.sort()  #ordered list as input
search_number = recursive_binary(ordered_list, ordered_list[9], 0, 9)
print("the search number is", search_number)
