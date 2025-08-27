from map import (
    get_ground, set_ground, get_object, set_object,
    G_GRASS, G_DIRT, G_DIRT_WET,
    O_NONE, O_SEED, O_PLANT_S3, O_LOG, O_ROCK
)

def use_tool(tool_id, tx, ty):
    if tool_id == 1:
        if get_object(tx, ty) == O_PLANT_S3:
            set_object(tx, ty, O_NONE)
    elif tool_id == 2:
        if get_ground(tx, ty) == G_GRASS:
            set_ground(tx, ty, G_DIRT)
        if get_object(tx, ty) == O_SEED:
            set_object(tx, ty, O_NONE)
    elif tool_id == 3:
        if get_ground(tx, ty) == G_DIRT:
            set_ground(tx, ty, G_DIRT_WET)
    elif tool_id == 4:
        if get_object(tx, ty) == O_LOG:
            set_object(tx, ty, O_NONE)
    elif tool_id == 5:
        if get_object(tx, ty) == O_ROCK:
            set_object(tx, ty, O_NONE)