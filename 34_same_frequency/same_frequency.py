def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    nums1 = tuple(str(num1))
    nums2 = tuple(str(num2))

    return {num: nums1.count(num) for num in nums1} == {num: nums2.count(num) for num in nums2}