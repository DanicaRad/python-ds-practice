def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    nums.reverse()
    pairs = []
    print(nums)

    # for num in list(range(0, len(nums) - 1)):
    #     remainder = goal - int(new_nums[num])
    #     if remainder in new_nums[num:]:
    #         pairs.append((remainder, new_nums[num]))
    
    # return pairs[-1]

    for num1 in nums:
        num1, *rest = nums
        for num2 in rest:
            if num1 + num2 == goal:
                pairs.append((num1, num2))
    return pairs[0]

    # for num in list(range(len(nums))):
    #     for re_num in nums[num:]:
    #         if re_num + num == goal:
    #             print(f"this {re_num} can probably fuck off it + {num} dont't = {goal} and aren't the first pairs")




    # pairs = tuple((num, goal - num) for num in nums if (goal - num) in nums) 

    # sort_pairs = {nums.index(pair[1]): pair for pair in pairs}
    # print(list(sort_pairs.keys()))
    # print(sort_pairs)




