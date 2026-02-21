def rectangle_area(a, b=None):
    if a < 1:
        return 0
    if b != None:
        if b < 1:
            return 0
        else:
            return a * b
    else:
        return a * a
