#!/usr/bin/python
# coding:UTF-8

import sys
import numpy as np

class Map: # 迷路マップ
    i = 0 # index
    j = 0 # index

    def __init__(self, filename):
        self.file = open(filename)
        inputlines = self.file.readlines()
        self.num_row = len(inputlines) # the number of rows
        self.num_col = len(inputlines[0]) - 1 # the number of columns
        self.map = [[0 for j in range(self.num_col)] for i in range(self.num_row)] # initializing map

        for i in range(self.num_row):
            for j in range(self.num_col):
                self.map[i][j] = int(list(inputlines[i])[j])


    def printmap(self):
        for i in range(self.num_row):
            for j in range(self.num_col):
                if self.map[i][j] == 0:
                    print('□', end = '')
                elif self.map[i][j] == 1:
                    print('■', end = '')
                elif self.map[i][j] == 2:
                    print('S', end = '')
                elif self.map[i][j] == 3:
                    print('G', end = '')
            print('')


    def get_start_position(self): # get start position (row, column)
        for i in range(self.num_row):
            for j in range(self.num_col):
                if self.map[i][j] == 2:
                    return np.array([i, j])


    def get_goal_position(self): # get goal positon (row, column)
        for i in range(self.num_row):
            for j in range(self.num_col):
                if self.map[i][j] == 3:
                    return np.array([i, j])


    def get_position_info(self, position):
        return self.map[position[0]][position[1]]
