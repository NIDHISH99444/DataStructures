def jump( nums):
    size = len(nums)

    # destination is last index
    destination = size - 1

    # record of current coverage, record of last jump index
    cur_coverage, last_jump_index = 0, 0

    # counter for jump
    times_of_jump = 0

    # Quick response if start index == destination index == 0
    if size == 1:
        return 0

    # Greedy strategy: extend coverage as long as possible with lazy jump
    for i in range(0, size):

        # extend current coverage as further as possible
        cur_coverage = max(cur_coverage, i + nums[i])

        # forced to jump (by lazy jump) to extend coverage
        if i == last_jump_index:

            # update last jump index
            last_jump_index = cur_coverage

            # update counter of jump by +1
            times_of_jump += 1

            # check if reached destination already
            if cur_coverage >= destination:
                return times_of_jump

    return times_of_jump


print(jump([ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]))

