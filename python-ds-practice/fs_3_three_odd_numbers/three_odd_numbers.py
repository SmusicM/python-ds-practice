def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    three_sequentials = []
    for i in range(len(nums)-2):
        three = (nums[i],nums[i+1],nums[i+2]) #gets three at indexs
        three_sequentials = three_sequentials + [three]
    return any(sum(triplet) % 2 != 0 for triplet in three_sequentials)