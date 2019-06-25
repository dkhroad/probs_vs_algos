Time Complexity: 
As our primary data structure to store tries nodes is a hash table (python
dictionary) with a path component as a key. The worst case time complexity of inserting
and/or looking for a handler for a given route will be O(np), when np is the
maximum number of path components in the longest route. Since it is highly
unusual for the path component to exceed a small number (say 50), even the
worst case time complexity could be assumed to be close to the average time
complexity. Which is, O(1)

Space complexity: 
Since we are using Python dictionary as our underlying data structure, that has
space complexity of O(n), when n is the number of keys (path components). 

