def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    min = ints[0] if len(ints) > 0 else None 
    max = ints[0] if len(ints) > 0 else None

    for i in range(len(ints)):
        if ints[i] < min:
            min = ints[i]
        if ints[i] > max:
            max = ints[i]

    return (min,max)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None,None) == get_min_max([])) else "Fail")
print ("Pass" if ((1,1) == get_min_max([1,1])) else "Fail")
print ("Pass" if ((1,1) == get_min_max([1])) else "Fail")
