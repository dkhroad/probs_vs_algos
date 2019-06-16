Since the problem mentions it is a sorted array, we can use binary search and
keep the worst case time complexity of O(log N), where N is the size of the
input list. 

However, since the array could be rotated around a pivot point. We can't apply
the binary search directly to the input list. We will first need to find the
pivot point around which the input list is rotate. Since the element next to 
the pivot point would be smaller than the pivot point, we can apply a modified 
binary search to find the pivot point.

Once we have found the pivot point. We can logically divide the input list into 
two sub lists divided by the pivot point. By checking if the number to be searched
is smaller than first element of the input list, we can easily determine if the number to be
searched is in the left (of the pivot) sub array or in the right sub array. 

After we have determine the correct sub list in which the number resides,
we apply another binary search in the correct sub list to find the number if it
exists in that input list.

Space Complexity: O(1)
Time Complexity:  O(log n), where n is the size of the input list.
Note that even though we do 2 binary searches (one to find the pivot index and
another to find the number) of time complexity of O(log n). The overall time
complexity is still O(log n) since 2 is just a constant that can be dropped. 
