'''make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True'''


def make_bricks(small, big, goal):
    if goal >= 5 and big > 0:
        goal = goal - 5
        big = big - 1
    elif small > 0:
        goal = goal - 1
        small = small - 1
    if goal > 0:
        if big == 0 and small == 0:
            return False
        else:
            return make_bricks(small, big, goal)
    elif goal == 0:
        return True
        # return make_bricks(small, big, goal)


def non_rec_make_bricks(small, big, goal):
    while((small > 0 or big > 0) and goal > 0):
        if goal >= 5 and big > 0:
            goal = goal - 5
            big = big - 1
        elif small > 0:
            goal = goal - 1
            small = small - 1
        if goal == 0:
            return True
    return False


def no_iteration(small, big, goal):
    bg_needed = goal//5
    sm_needed = goal % 5
    if(bg_needed <= big and sm_needed <= small):
        return True
    if(bg_needed > big):
        sm_needed += (bg_needed-big)*5
        if(sm_needed <= small):
            return True
        else:
            return False
    return False


print(non_rec_make_bricks(3, 1, 9))
