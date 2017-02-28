#!/usr/bin/python
# coding:UTF-8

import sys

class QLearning:
    gamma = 0.90
    alpha = 0.1

    def __init__(self, number, rwd, pns):
        self.n_episode = number
        self.reward = rwd
        self.punishment = pns


    def execute_qlearning(self, maze_map, agent, qtable):
        for episode in range(1, self.n_episode + 1): # 1 ~ n_episode
            print('episode : ' + str(episode))
            while (all(agent.get_agent_position() == maze_map.get_goal_position())) == False: # not at goal
                agent.agent_move(maze_map, qtable, self)
            # when the agent reaches the goal, episode ends
            agent.set_agent_posision(maze_map.get_start_position())


    def update_qtable(self, maze_map, qtable, cur_pos, next_pos, dire):
        # cur_pos = current position [hoge1, hoge2]
        # next_pos = next position [hoge3, hoge4]
        # dire = direction
        cur_row = cur_pos[0]
        cur_col = cur_pos[1]
        next_row = next_pos[0]
        next_col = next_pos[1]

        if maze_map.get_position_info(next_pos) == 3: # if the next is goal
            #reward = 100
            r = self.reward
        else: # if the next is not goal
            r = self.punishment

        qvalue_t = qtable.get_qvalue(cur_row, cur_col, dire)
        max_qvalue_t_next = qtable.get_q_vector(next_row, next_col).max(0)

        # updating
        qvalue_t = qvalue_t + self.alpha * (r + self.gamma * max_qvalue_t_next - qvalue_t)
        qtable.set_qvalue(cur_row, cur_col, dire, qvalue_t)
