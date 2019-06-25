def _sqrt(number,lower,upper):
    if number == 0 or number == 1:
        return number
    if (upper - lower)  == 1:
        return lower
    mid = (lower + upper) // 2 
    sqr  = mid * mid
    if sqr > number:
        upper = mid
        return _sqrt(number,lower,upper)
    if sqr < number:
        lower = mid
        return _sqrt(number,lower,upper)
    if sqr == number:
        return mid


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    return _sqrt(number,0,number)
    




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(29)) else "Fail")
