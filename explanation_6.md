To solve this problem in a single pass with O(n) worst case time complexity, 
we keep track of the minimum and maximum values in two separate variables - min and max.
As we traverse the list, we compare each element with min and max, and swap it with min if it is
smaller than min or with max if it is larger than max. 
