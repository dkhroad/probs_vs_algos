The problem can be solved by partitioning the input list into 4 parts using 3
pointers low, mid, high. 

We assume any thing below index 'low' and above index 'high' is at its correct
place. And any value between mid and high indexes is unknown. By setting mid =
low, we can scan the entire list in a single pass, and move each element to its
right place as the following: 

- if input_list[mid] is 0, we swap it with input_list[low] and increments both
    low and mid pointers.
- if input_list[mid] is 2, we swap it with input_list[high] and decrement the
    high pointers
- if input_list[mid] is 1, we just increment the mid pointer. 

Using this algorithm, we can sort the array in one pass, achieving the worst case
time complexity of O(N), where N is the size of the input list.
