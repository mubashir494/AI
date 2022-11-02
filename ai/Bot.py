from Battleship import GRID_SIZE, HitStatus
import copy
import random
def gen_rand(le):
    return random.randint(0, le)

full_list = []
for a in range(0,10):
    for b in range (0,10):
        full_list.append((a,b))


class Bot:
    # __last_turn_status = HitStatus.NONE
    # __last_turn_loc = (0,0)
    # __my_hit_list = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # __tried_list = copy.copy(full_list)

    def __init__(self):
        self.__last_turn_status = HitStatus.NONE
        self.__last_turn_loc = (0,0)
        self.__my_hit_list = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.__tried_list = copy.copy(full_list)

    def do_turn(self, hit_grid, last_turn_status) -> (str, int):
        self.__last_turn_status = last_turn_status

        x , y = self.__last_turn_loc[0], self.__last_turn_loc[1]
        print("-------------------------------------------------------------")
        print((x,y))
        print(self.__last_turn_status)
        print_hit_board(hit_grid)
        # print(hit_grid)
        # print (self.__my_hit_list)
        if self.__last_turn_status == HitStatus.HIT:
            print ("hit !!!!")
            print (self.__tried_list)
            print((x,y))
            self.__tried_list.remove((x,y))
            self.__my_hit_list[x][y] = True
            if (x + 1) <= 9 and ((x+1,y) in self.__tried_list):
                self.__last_turn_loc = ((x+1), y)
                print(self.__last_turn_loc)
                return chr((x+98)), y
            elif (x - 1) >= 0 and ((x-1,y) in self.__tried_list):
                self.__last_turn_loc = ((x-1), y)
                print(self.__last_turn_loc)
                return chr((x+96)), y
            elif (y + 1) <= 9 and ((x,y+1) in self.__tried_list):
                self.__last_turn_loc = (x, (y+1))
                print(self.__last_turn_loc)
                return chr((x+97)), y+1
            elif (y - 1) >= 0 and ((x,y-1) in self.__tried_list):
                self.__last_turn_loc = (x, (y-1))
                print(self.__last_turn_loc)
                return chr((x+97)), y-1
            else:
                ind = gen_rand(len(self.__tried_list) - 1)
                self.__last_turn_loc = self.__tried_list[ind]
                return (chr(self.__tried_list[ind][0]+97) , self.__tried_list[ind][1])

        elif self.__last_turn_status == HitStatus.MISS:
            print ("miss !!!!")
            print (self.__tried_list)
            self.__tried_list.remove((x,y))
            ind = gen_rand(len(self.__tried_list) - 1)
            print (ind)
            print (self.__tried_list[ind])
            print ((chr(self.__tried_list[ind][0]+97) , self.__tried_list[ind][1]))
            self.__last_turn_loc = self.__tried_list[ind]
            return (chr(self.__tried_list[ind][0]+97) , self.__tried_list[ind][1])
            # self.__my_hit_list[x][y] = True
        elif self.__last_turn_status == HitStatus.TRIED_ALREADY:
            print('Tried Already !!!!!!')
            print (self.__tried_list)
            self.__tried_list.remove((x,y))
            ind = gen_rand(len(self.__tried_list) - 1)
            self.__last_turn_loc = self.__tried_list[ind]
            return (chr(self.__tried_list[ind][0]+97) , self.__tried_list[ind][1])
            # self.__my_hit_list[x][y] = True
        # TODO Do something clever
        

        # TODO Must return a tuple (colLetter, rowNumber)
        return 'a', 0


def print_hit_board(hit_grid):
    board_str = '#  ' + ''.join([f"{letter}  " for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:GRID_SIZE]]) + '#\n'
    x = -1
    y = -1
    for row_index, row in enumerate(hit_grid):
        board_str += f"{row_index}  "
        for col_index, tile in enumerate(row):
            board_str += hit_grid[row_index][col_index].value
            board_str += "  "
        board_str += '#\n'

    board_str += "#  " + '#  ' * GRID_SIZE + '#\n'
    print(board_str)
