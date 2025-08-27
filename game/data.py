G_GRASS = 0
G_DIRT = 1
G_DIRT_WET = 2

O_NONE = 0
O_FENCE = 1
O_LOG = 2
O_ROCK = 3

O_CORN_SEED = 4
O_CORN_S1 = 5
O_CORN_S2 = 6
O_CORN_S3 = 7
O_CORN_S4 = 8
O_CORN = 9

O_CARROT_SEED = 10
O_CARROT_S1 = 11
O_CARROT_S2 = 12
O_CARROT_S3 = 13
O_CARROT_S4 = 14
O_CARROT = 15

O_TOMATO_SEED = 16
O_TOMATO_S1 = 17
O_TOMATO_S2 = 18
O_TOMATO_S3 = 19
O_TOMATO_S4 = 20
O_TOMATO = 21

BLOCK_OBJECTS = {O_FENCE, O_LOG, O_ROCK}

GROUND_SPRITES = {
    G_GRASS: "grass",
    G_DIRT: "soil",
    G_DIRT_WET: "soil_wet",
}

OBJECT_SPRITES = {
    O_FENCE: "fence", O_LOG: "log", O_ROCK: "rock",
    O_CORN_SEED: "corn_seed", O_CORN_S1: "corn_0", O_CORN_S2: "corn_1", O_CORN_S3: "corn_2", O_CORN_S4: "corn_3", O_CORN: "corn",
    O_CARROT_SEED: "carrot_seed", O_CARROT_S1: "carrot_0", O_CARROT_S2: "carrot_1", O_CARROT_S3: "carrot_2", O_CARROT_S4: "carrot_3", O_CARROT: "carrot",
    O_TOMATO_SEED: "tomato_seed", O_TOMATO_S1: "tomato_0", O_TOMATO_S2: "tomato_1", O_TOMATO_S3: "tomato_2", O_TOMATO_S4: "tomato_3", O_TOMATO: "tomato",
}

CROPS = [
    [O_CORN_SEED, O_CORN_S1, O_CORN_S2, O_CORN_S3, O_CORN_S4, O_CORN],
    [O_CARROT_SEED, O_CARROT_S1, O_CARROT_S2, O_CARROT_S3, O_CARROT_S4, O_CARROT],
    [O_TOMATO_SEED, O_TOMATO_S1, O_TOMATO_S2, O_TOMATO_S3, O_TOMATO_S4, O_TOMATO],
]

def is_seed(obj_id):
    for seq in CROPS:
        if obj_id == seq[0]:
            return True
    return False

def is_ready_to_harvest(obj_id):
    for seq in CROPS:
        if obj_id == seq[-2]:
            return True
    return False

def get_crop_result(obj_id):
    for seq in CROPS:
        if obj_id == seq[-2]:
            return seq[-1]
    return 0