#!/usr/bin/python
# coding:UTF-8

import sys
import random
import numpy as np
import Map
import QLearning
import QTable
import Agent

if __name__ == "__main__":
    args = sys.argv # reading filename from command-line arguments
    argc = len(args)
    if(argc != 5):
        print('usage : $ python', args[0], 'maze_map(.txt file) episode(number) reward(0-1 float) punishment(0-1 float)')
        exit()
    n_episode = int(args[2]) # the number of episodes
    reward = float(args[3]) # reward
    punishment = float(args[4]) # punishment

    # fix seed for reproducibility(再現性)
    random.seed(0)
    np.random.seed(0)

    maze_map = Map.Map(args[1])
    maze_map.printmap() # print maze (initial state)
    agent = Agent.Agent(maze_map)
    qtable = QTable.QTable(maze_map)
    qlearning = QLearning.QLearning(n_episode, reward, punishment)

    # execute QLearning
    qlearning.execute_qlearning(maze_map, agent, qtable)

    # printing result
    qtable.print_result(maze_map)

#end of program
