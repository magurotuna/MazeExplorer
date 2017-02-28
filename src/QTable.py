#!/usr/bin/python
# coding:UTF-8

import numpy as np

class QTable:
    i = 0 # index
    j = 0 # index
    k = 0 # index
    num_action = 4 # the number of actions(up, down, right, left)

    def __init__(self, maze_map):
        self.qtable = np.random.rand(maze_map.num_row, maze_map.num_col, self.num_action) + np.array([[[1 for i in range(self.num_action)] for j in range(maze_map.num_col)] for k in range(maze_map.num_row)])
        # 1~2 random values fill all elements of QTable


    def get_direction(self, maze_map, agent):
        # getting direction the agent should go to (based on Q-Value)
        pos = agent.get_agent_position()
        movable_vec = self.qtable[pos[0]][pos[1]] * agent.get_movable_position(maze_map)
        return movable_vec.argmax(0)


    def get_qvalue(self, row, col, action): # getter
        return self.qtable[row][col][action]


    def set_qvalue(self, row, col, action, value): # setter
        self.qtable[row][col][action] = value


    def get_q_vector(self, row, col):
        # getting vector that includes q-value of each action
        return self.qtable[row][col]


    def print_result(self, maze_map): # when QLearning is finished, execute this
        for i in range(maze_map.num_row):
            for j in range(maze_map.num_col):
                pos = maze_map.get_position_info((i, j))
                if pos == 1:
                    print('■', end = '')
                    continue
                elif pos == 2:
                    print('S', end = '')
                    continue
                elif pos == 3:
                    print('G', end = '')
                    continue
                elif pos == 0:
                    max_direction = self.qtable[i][j].argmax(0)
                    if max_direction == 0:
                        print('↑', end = '')
                    elif max_direction == 1:
                        print('↓', end = '')
                    elif max_direction == 2:
                        print('←', end = '')
                    elif max_direction == 3:
                        print('→', end = '')
            print('')
