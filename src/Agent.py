#!/usr/bin/python
# coding:UTF-8

import sys
import random
import numpy as np

epsilon = 0.2 # epsilon-greedy method

class Agent:
    def __init__(self, maze_map):
        self.agent_pos = maze_map.get_start_position()


    def get_agent_position(self):
        return self.agent_pos


    def set_agent_posision(self, agent_next_pos):
        self.agent_pos = agent_next_pos


    def get_agent_position_neighbour(self, direction):
        # direction... 0:up, 1:down, 2:left, 3:right
        if direction == 0:
            vec = np.array([-1, 0])
        elif direction == 1:
            vec = np.array([1, 0])
        elif direction == 2:
            vec = np.array([0, -1])
        elif direction == 3:
            vec = np.array([0, 1])

        return (self.agent_pos + vec)


    def get_movable_position(self, maze_map):
        # getting places where the agent can go
        # [up, down, left, right], 1 is OKAY, -100000000 is NG
        # ex. np.array [1, 0, 1, 0] means the agent can go to down and right
        tmp = np.array([1, 1, 1, 1])
        for i in range(4):
            if maze_map.get_position_info(self.get_agent_position_neighbour(i)) == 1:
                tmp[i] = -100000000
        return tmp


    def agent_move(self, maze_map, qtable, qlearning):
        # defining the movement of the agent
        # if random.random() <= epsilon then the agent's action is random
        # else the agent is goint to take action that has the highest Qvalue
        if random.random() <= epsilon:
            direction = random.choice((0, 1, 2, 3))
            while self.get_movable_position(maze_map)[direction] != 1:
                # when cannot go to random choice direction
                direction = random.choice((0, 1, 2, 3))

            cur_pos = self.get_agent_position()
            next_pos = self.get_agent_position_neighbour(direction)


            # update Q-Value
            qlearning.update_qtable(maze_map, qtable, cur_pos, next_pos, direction)

            # the agent moves
            self.set_agent_posision(next_pos)

        else:
            direction = qtable.get_direction(maze_map, self)

            cur_pos = self.get_agent_position()
            next_pos = self.get_agent_position_neighbour(direction)

            # update Q-Value
            qlearning.update_qtable(maze_map, qtable, cur_pos, next_pos, direction)

            # the agent moves
            self.set_agent_posision(next_pos)
