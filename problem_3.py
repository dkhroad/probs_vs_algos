
def merge(left,right):
    left_index = 0
    right_index = 0
    merged = []

    while left_index < len(left)  and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else: 
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged
                  

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)



def sort(arr):
    return mergesort(arr)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    num1 = [] 
    num2 = [] 
    sorted = sort(input_list) # sorted via merge sort
    idx = 0

    while idx < len(sorted):
        num1.append(str(sorted[idx]))
        idx += 1
        if idx < len(sorted):
            num2.append(str(sorted[idx]))
            idx += 1 

    return int(("".join(num1))),int(("".join(num2)))

    


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
