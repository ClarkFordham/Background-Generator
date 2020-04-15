from random import *

class Array_gen():
    color_list = []
    width = 0
    height = 0
    
    def __init__(self, colors, width, height):
        self.color_list = colors
        self.width = width
        self.height = height

    def create_array(self):
        seed()
        random_order = []
        for x in range(0,self.width):
            for y in range(0, self.height):
                random_order.append((x,y))
        shuffle(random_order)
        result = [["" for i in range(0,self.height)] for i in range(0,self.width)]
        
        for pos in random_order:
            weights = [1] * len(self.color_list)
            for x in range(pos[0]-2, pos[0]+2):
                for y in range(pos[1]-2, pos[1]+2):
                    if x < len(result) and y < len(result[0]) and result[x][y] != "":
                        weights[self.color_list.index(result[x][y])] += 5
            result[pos[0]][pos[1]] = choices(self.color_list, weights=weights)[0]

        return result