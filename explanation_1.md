In order to find the square root of an integer in O(log n) time complexity, we
use binary search. The basic algorithm is as the following:

We set the lower value of the search space to 0 and the upper value
to the given number. We repeated divide this search space by 2. If the result
multiplied by itself is equal to the number then we have the correct square
root. Otherwise if the multiplication of the division result is greater than
the number, we reduce the search space by half by setting the upper bound to the mid point
(division result), else we set the lower bound to the mid point.

We continue these steps mentioned above till be exhaust the search space.
If the whole search space is exhausted without finding the integer square root,
then we  return the last lower value of the search space as it will be the
floor value of the actual square root.

Since we are using binary search to find the square root. The time complexity
of this solution is: O(log N), where N is the integer for which we need
to find the square root. 

Space Complexity: O(log N)
The biggest term contributing to space complexity is the stack usage by the
recursive function _sqrt. Which is directly proportional to number times _sqrt
is called. Which is: O(log N)
