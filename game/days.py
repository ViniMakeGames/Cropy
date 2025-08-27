from data import CROPS, G_DIRT_WET, G_DIRT
from map import MAP_GROUND, get_ground, set_ground, get_object, set_object

def advance_day():
    h = len(MAP_GROUND)
    w = len(MAP_GROUND[0]) if h else 0
    for y in range(h):
        for x in range(w):
            if get_ground(x, y) == G_DIRT_WET:
                oid = get_object(x, y)
                for seq in CROPS:
                    if oid in seq:
                        i = seq.index(oid)
                        if i < len(seq) - 2:
                            set_object(x, y, seq[i + 1])
                        break
    for y in range(h):
        for x in range(w):
            if get_ground(x, y) == G_DIRT_WET:
                set_ground(x, y, G_DIRT)