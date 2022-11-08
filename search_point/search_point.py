import random
import math

BOARD_SIZE = 5

def generate_position(size):
    x = random.randrange(0, size)
    y = random.randrange(0, size)

    return (x, y)

def calc_distance(pos1, pos2):
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x ** 2 + diff_y ** 2)

def move_position(direction, pos):

    current_x, current_y = pos

    if direction == "w":
        current_y -= 1
    elif direction == "s" :
        current_y += 1
    elif direction == "a" :
        current_x -= 1
    elif direction == "d" :
        current_x += 1

    return (current_x, current_y)


def search_point():
    point_pos = generate_position(BOARD_SIZE)
    player_pos = generate_position(BOARD_SIZE)
    count = 0
    while (point_pos != player_pos):
        
        distance = calc_distance(point_pos, player_pos)
        print("Target:", distance)

        c = input("W: Up A: Left S: Down D: Right input -> ")
        count += 1
        player_pos = move_position(c, player_pos)
    
    print("Hit! Count =", count)

search_point()
