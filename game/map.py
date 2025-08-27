import pygame
from assets import load_img

G_GRASS = 0
G_DIRT = 1
G_DIRT_WET = 2

O_NONE = 0
O_FENCE = 1
O_SEED = 2
O_LOG = 3
O_ROCK = 4
O_PLANT_S1 = 5
O_PLANT_S2 = 6
O_PLANT_S3 = 7
O_PLANT_S4 = 8

BLOCK_OBJECTS = {O_FENCE}

MAP_GROUND = [
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
    [G_GRASS]*20,
]

MAP_OBJECTS = [
    [O_FENCE]*20,
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]+[O_NONE]*18+[O_FENCE],
    [O_FENCE]*20,
]

_tile_cache={}
_last_tilesize=None
_walls=[]
_wall_listeners=[]

def register_wall_listener(callback):
    _wall_listeners.append(callback)
    if _walls:
        callback(list(_walls))

def _img(key, name, size):
    d=_tile_cache.setdefault(size,{})
    if key not in d: d[key]=load_img(name,size)
    return d[key]

def draw_map(surface, tilesize):
    s = (tilesize, tilesize)
    ground_res = {
        G_GRASS:  "grass",
        G_DIRT:   "soil",
        G_DIRT_WET:"soil_wet",
    }
    obj_res = {
        O_FENCE:   "fence",
        O_SEED:    "corn_seed",
        O_PLANT_S1:"corn_0",
        O_PLANT_S2:"corn_1",
        O_PLANT_S3:"corn_2",
        O_PLANT_S4:"corn_3",
    }
    for y,row in enumerate(MAP_GROUND):
        for x,t in enumerate(row):
            surface.blit(_img(("g",t,s), ground_res[t], s),(x*tilesize,y*tilesize))
    for y,row in enumerate(MAP_OBJECTS):
        for x,t in enumerate(row):
            if t!=O_NONE:
                surface.blit(_img(("o",t,s), obj_res[t], s),(x*tilesize,y*tilesize))

def in_bounds(tx,ty):
    return 0<=ty<len(MAP_GROUND) and 0<=tx<len(MAP_GROUND[0])

def tile_rect(tx,ty,tilesize):
    return pygame.Rect(tx*tilesize, ty*tilesize, tilesize, tilesize)

def _rebuild_walls(tilesize=None):
    global _last_tilesize, _walls
    if tilesize is not None: _last_tilesize=tilesize
    if _last_tilesize is None: return
    t=_last_tilesize
    _walls=[]
    for y,row in enumerate(MAP_OBJECTS):
        for x,obj in enumerate(row):
            if obj in BLOCK_OBJECTS:
                _walls.append(pygame.Rect(x*t, y*t, t, t))
    for cb in _wall_listeners:
        cb(list(_walls))

def get_collision_tiles(tilesize):
    _rebuild_walls(tilesize)
    return list(_walls)

def set_ground(tx,ty,tile_id):
    if in_bounds(tx,ty): MAP_GROUND[ty][tx]=tile_id

def set_object(tx,ty,obj_id):
    if in_bounds(tx,ty):
        MAP_OBJECTS[ty][tx]=obj_id
        _rebuild_walls()

def get_ground(tx,ty):
    return MAP_GROUND[ty][tx] if in_bounds(tx,ty) else None

def get_object(tx,ty):
    return MAP_OBJECTS[ty][tx] if in_bounds(tx,ty) else None

def draw_cursor(surface, tx, ty, tilesize):
    rect=tile_rect(tx,ty,tilesize)
    surf=pygame.Surface((tilesize,tilesize), pygame.SRCALPHA); surf.fill((255,255,255,40))
    surface.blit(surf, rect.topleft); pygame.draw.rect(surface,(255,255,255),rect,1)