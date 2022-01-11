def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    greater_nums = []
    for num in nums:
        x = nums.index(num) + 1
        next_nums = nums[x::]
        for next_num in next_nums:
            if next_num > num:
                greater_nums.append(next_num)
    return len(greater_nums)

