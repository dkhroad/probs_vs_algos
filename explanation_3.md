To solve this problem in time complexity of O(n log n), where n is the size of
the input list, first we sort the input list using count sort, then we iterate
through the sorted list by picking a digit at an alternate index to compute
digits for the two numbers. 

Time complexity: 
    time complexity to sort + time complexity to compute two numbers.
    O(n+k) + O(n), where n is the number of elements in the input and k is the
    range of the input.
    Dropping the lower order term O(n), and assuming k to significantly smaller then n, we 
    get overall complexity of O(n)

Space complexity: 
    We need 1) original array of size n, count array of size k, where k is the
    range of elements in the array. And an output array of size n. 
    Therefore the space complexity is expected to be O(n+k)

