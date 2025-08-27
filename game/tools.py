from map import (
    get_ground, set_ground, get_object, set_object,
)
from data import (
    G_GRASS, G_DIRT, G_DIRT_WET,
    O_NONE, O_FENCE, O_LOG, O_ROCK,
    O_CORN_SEED, O_CORN_S1, O_CORN_S2, O_CORN_S3, O_CORN_S4, O_CORN,
    O_CARROT_SEED, O_CARROT_S1, O_CARROT_S2, O_CARROT_S3, O_CARROT_S4, O_CARROT,
    O_TOMATO_SEED, O_TOMATO_S1, O_TOMATO_S2, O_TOMATO_S3, O_TOMATO_S4, O_TOMATO,
    BLOCK_OBJECTS, GROUND_SPRITES, OBJECT_SPRITES, CROPS,
    is_seed, is_ready_to_harvest, get_crop_result,
)

def use_tool(tool_id, tx, ty):
    object = get_object(tx, ty)
    ground = get_ground(tx, ty)

    if tool_id == 1:
        if is_ready_to_harvest(object):
            set_object(tx, ty, get_crop_result(object))
    elif tool_id == 2:
        if ground == G_GRASS:
            set_ground(tx, ty, G_DIRT)
        if is_seed(object):
            set_object(tx, ty, O_NONE)
    elif tool_id == 3:
        if ground == G_DIRT:
            set_ground(tx, ty, G_DIRT_WET)
    elif tool_id == 4:
        if object == O_LOG:
            set_object(tx, ty, O_NONE)
    elif tool_id == 5:
        if object == O_ROCK:
            set_object(tx, ty, O_NONE)
    elif tool_id == 6:
        if object == O_NONE and ground != G_GRASS:
            set_object(tx, ty, O_CORN_SEED)
    elif tool_id == 7:
        if object == O_NONE and ground != G_GRASS:
            set_object(tx, ty, O_CARROT_SEED)
    elif tool_id == 8:
        if object == O_NONE and ground != G_GRASS:
            set_object(tx, ty, O_TOMATO_SEED)