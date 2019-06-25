def find_pivot_index(input_list,lower=0,upper=-1):
    # pdb.set_trace()
    if upper == -1:
        upper = len(input_list) - 1
    if upper < 0:
        return -1

    if upper == lower:
        return lower

    mid = (lower + upper) // 2

    if upper - lower == 1: 
        if input_list[lower] > input_list[upper]:
            return lower
        else:
            return upper
    # pdb.set_trace()
    if input_list[lower] > input_list[mid]: # pivot is in the lower half
        upper = mid - 1
    else:
        lower = mid + 1  # pivot is in the upper half
    return find_pivot_index(input_list,lower,upper)


def binary_search(input_list,number,lower,upper):
    if len(input_list) < 1:
        return -1
    if lower > len(input_list) -1 or upper > len(input_list) - 1:
        return -1
    if lower > upper:
        return -1

    if lower == upper and lower > -1:
        if input_list[lower] == number:
            return lower
        else:
            return -1

    mid = (lower + upper) // 2
    if number == input_list[mid]:
        return mid
    if number < input_list[mid]:
        upper = mid - 1
    else: 
        lower = mid + 1

    return binary_search(input_list,number,lower,upper)

            

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot_index = find_pivot_index(input_list)
    if pivot_index == 1:
        return pivot_index

    if number == input_list[pivot_index]:
        return pivot_index

    if pivot_index == len(input_list) - 1: # array is not rotated
       return binary_search(input_list,number,0,pivot_index)

    if number < input_list[0]: # the number is in the right sub array
        return binary_search(input_list,number,pivot_index + 1,len(input_list) -1 )
    else: # the number is in the left sub array
        return binary_search(input_list,number,0,pivot_index -1)



   


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 5])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
