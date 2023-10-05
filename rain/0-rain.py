#!/usr/bin/python3
""" possible interview question """


def rain(walls):
    """calculate how much water can be trapped in the walls"""
    if not walls:
        return 0
    water = 0
    left = 0  # left wall
    right = len(walls) - 1  # right wall
    left_max = walls[left]  # max height of left wall
    right_max = walls[right]  # max height of right wall
    while left < right:  # while the walls haven't met
        if left_max < right_max:  # if left wall is shorter
            left += 1        # move left wall to the right  1
            if walls[left] > left_max:  # if the new left wall is taller  2
                left_max = walls[left]  # update the max height of left wall  3
            else:
                water += left_max - walls[left]
        else:  # if right wall is shorter
            right -= 1  # move right wall to the left  4
            if walls[right] > right_max:  # if the new right wall is taller  5
                # update the max height of right wall  6
                right_max = walls[right]
            else:
                water += right_max - walls[right]
    return water  # return the total amount of water trapped
