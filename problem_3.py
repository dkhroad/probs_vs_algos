
def minmax(arr):
    min,max = 0,0
    if len(arr) > 0:
        min,max = arr[0],arr[0]

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    return (min,max)

def countsort(arr):
    min,max = minmax(arr) 
    count = [0 for _ in range(max-min+1)]
    for i in range(len(arr)):
        count[arr[i]-min] += 1


    for i in range(1,len(count)):
        count[i] += count[i-1]
        

    output = [0] * len(arr)
    for i in range(len(arr)-1,-1,-1):
        output[count[arr[i]-min]-1] = arr[i]
        count[arr[i]-min] -= 1
    

    return output[::-1]

def sort(arr):
    return countsort(arr)

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
    sum1 = 0
    sum2 = 0
    sorted = sort(input_list) # sorted via count sort with time complexity of O(n)
    idx = 0

    while idx < len(sorted):
        num1.append(str(sorted[idx]))
        idx += 1
        if idx < len(sorted):
            num2.append(str(sorted[idx]))
            idx += 1 

    if len(num1) > 0:
        sum1 = int("".join(num1))

    if len(num2) > 0:
        sum2 = int("".join(num2))

    return (sum1,sum2)

    


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
    test_function([[], [0,0]])
    test_function([[1],[1,0]])
    test_function([[1,2],[2,1]])
