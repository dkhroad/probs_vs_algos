To solve this problem in time complexity of O(n log n), where n is the size of
the input list, first we sort the input list using merge sort, then we iterate
through the sorted list by picking a digit at an alternate index to compute
digits for the two numbers. 

Total time complexity: 
    time complexity to sort + time complexity to compute two numbers.
    O(n (log n)) + O(n)
    Dropping the lower order term O(n), we get overall complexity of O(n log(n))

