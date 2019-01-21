from random import randint

def make_map(field_width):
    map_ = [[2] * field_width]
    for i in range(field_width - 2):
        if i == field_width // 2 - 2:
            r = randint(1, field_width - 20)
            R = randint(1, field_width - r - 20)
            map_.append([2] + [-1] * r + [1.1] * (field_width - r - R - 2) + [-1] * R + [2])
        elif i < field_width // 2 - 2 or i > field_width // 2 + 2:
            map_.append([2] + [1.1] * (field_width - 2) + [2])
        elif i == field_width // 2 + 2:
            r = randint(1, field_width - 20)
            R = randint(1, field_width - r - 20)
            map_.append([2] + [1.1] * r + [-1] * (field_width - r - R - 2) + [1.1] * R + [2])
        else:
            map_.append([2] + [-1] * (field_width - 2) + [2])
    map_.append([2] * field_width)
    return map_
