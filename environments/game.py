import numpy as np
import copy
import time

from collections import deque   # 这个队列用来判断长将或长捉
import random
from board import board_list




####ignore#####
#### help gen #####
chess = ['司令','军长','师长','旅长','团长','营长','连长','排长','工兵','炸弹','地雷','军旗']
for i in range(len(chess)):
    print(f"{chess[i]} = np.array({[1 if i==j else 0  for j in range(len(chess))]}),")
#### help gen #####

# 棋子字符 -> 棋子数值 映射
chess_string2array = dict(
    司令=np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    军长=np.array([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    师长=np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    旅长=np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]),
    团长=np.array([0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]),
    营长=np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
    连长=np.array([0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]),
    排长=np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]),
    工兵=np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]),
    炸弹=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]),
    地雷=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]),
    军旗=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]),
    一一=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
)

def change_state(state_list, move):
    """move : 字符串'0010'"""
    copy_list = copy.deepcopy(state_list)
    y, x, toy, tox = int(move[0]), int(move[1]), int(move[2]), int(move[3])
    copy_list[toy][tox] = copy_list[y][x]
    copy_list[y][x] = '一一'
    return copy_list

# 打印盘面，可视化用到
def print_board(_state_array):
    # _state_array: [17, 17, 12], HWC
    board_line = []
    for i in range(17):
        for j in range(17):
            board_line.append(chess_string2array(_state_array[i][j]))
        print(board_line)
        board_line.clear()


def get_all_legal_moves():
    _move_id2move_action = {}
    _move_action2move_id = {}


# 列表棋盘状态到数组棋盘状态
def state_list2state_array(state_list):
    _state_array = np.zeros([17, 17, 12])
    for i in range(17):
        for j in range(17):
            _state_array[i][j] = chess_string2array[state_list[i][j]]
    return _state_array







###*******************棋子走法规则*******************###
# 为工兵单独设计路径搜索
def get_legal_moves(state_list,chess):
    # 获取棋子信息
    y,x = chess.pos
    roadType = board_list[y][x]
    legal_moves=[]
    # 先判断道路类型，然后判断是否在边界上
    if roadType == 'Camp':
        moves=[[y-1,x],[y+1,x],[y,x-1],[y,x+1],[y-1,x-1],[y-1,x+1],[y+1,x-1],[y+1,x+1]]
    elif roadType == 'Norm':
        moves= [[y-1,x],[y+1,x],[y,x-1],[y,x+1]]
    elif roadType == 'flag':
        moves=[]
    else:
    #铁路格子
        moves='railway'


    if moves=='railway':
        legal_moves=railway_moves(chess,y,x)
    else:
        for move in moves:
            if not board_list[move[0]][move[1]]:
                continue
            elif state_list[move[0]][move[1]].color == chess.color:
                continue
            elif state_list[move[0]][move[1]].color != chess.color and board_list[move[0]][move[1]] == 'Camp':
                continue
            else:
                legal_moves.append(move)
    return legal_moves


# 工兵在铁路上的合法走法
def engineer_moves(state_list,chess):
    """工兵的合法走法"""
    # 递归寻找
    pos = chess.pos
    legal_moves=[]
    left, right, up, down = 0, 0, 0, 0
    if board_list[pos[0] - 1][pos[1]] == 'RWay' or board_list[pos[0] - 1][pos[1]] == 'XWay' or board_list[pos[0] - 2][
        pos[1]] == 'CWay':
        up = 1
    if board_list[pos[0] + 1][pos[1]] == 'RWay' or board_list[pos[0] + 1][pos[1]] == 'XWay' or board_list[pos[0] + 2][
        pos[1]] == 'CWay':
        down = 1
    if board_list[pos[0]][pos[1] - 1] == 'RWay' or board_list[pos[0]][pos[1] - 1] == 'XWay' or board_list[pos[0]][
        pos[1] - 2] == 'CWay':
        left = 1
    if board_list[pos[0]][pos[1] + 1] == 'RWay' or board_list[pos[0]][pos[1] + 1] == 'XWay' or board_list[pos[0]][
        pos[1] + 2] == 'CWay':
        right = 1

    if up:




def engineer_moves_recursion(legal_moves:list,state_list,pos):
    if board_list[pos[0]][pos[1]] == 'CWay':
        if board_list[pos[0]-1][pos[1]] in ['RWay','XWay']:
            if [pos[0]-1,pos[1]] not in legal_moves:
                if state_list[pos[0]-1][pos[1]].is_empty():
                    legal_moves.append([pos[0]-1,pos[1]])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0]-1,pos[1]])
                elif state_list[pos[0]-1][pos[1]].color != chess.color:
                    legal_moves.append([pos[0]-1,pos[1]])
        elif board_list[pos[0]-2][pos[1]] == 'CWay':
            if [pos[0]-2,pos[1]] not in legal_moves:
                if state_list[pos[0]-2][pos[1]].is_empty():
                    legal_moves.append([pos[0]-2,pos[1]])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0]-2,pos[1]])
                elif state_list[pos[0]-2][pos[1]].color != chess.color:
                    legal_moves.append([pos[0]-2,pos[1]])

        if board_list[pos[0] + 1][pos[1]] in ['RWay', 'XWay']:
            if [pos[0] + 1, pos[1]] not in legal_moves:
                if state_list[pos[0] + 1][pos[1]].is_empty():
                    legal_moves.append([pos[0] + 1, pos[1]])
                    engineer_moves_recursion(legal_moves, state_list, [pos[0] + 1, pos[1]])
                elif state_list[pos[0] - 1][pos[1]].color != chess.color:
                    legal_moves.append([pos[0] - 1, pos[1]])
        elif board_list[pos[0] + 2][pos[1]] == 'CWay':
            if [pos[0] + 2, pos[1]] not in legal_moves:
                if state_list[pos[0] + 2][pos[1]].is_empty():
                    legal_moves.append([pos[0] + 2, pos[1]])
                    engineer_moves_recursion(legal_moves, state_list, [pos[0] + 2, pos[1]])
                elif state_list[pos[0] + 2][pos[1]].color != chess.color:
                    legal_moves.append([pos[0] + 2, pos[1]])

        if board_list[pos[0]][pos[1]-1] in ['RWay','XWay']:
            if [pos[0],pos[1]-1] not in legal_moves:
                if state_list[pos[0]][pos[1]-1].is_empty():
                    legal_moves.append([pos[0],pos[1]-1])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0],pos[1]-1])
                elif state_list[pos[0]][pos[1]-1].color != chess.color:
                    legal_moves.append([pos[0],pos[1]-1])
        elif board_list[pos[0]][pos[1]-2] == 'CWay':
            if [pos[0],pos[1]-2] not in legal_moves:
                if state_list[pos[0]][pos[1]-2].is_empty():
                    legal_moves.append([pos[0],pos[1]-2])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0],pos[1]-2])
                elif state_list[pos[0]][pos[1]-2].color != chess.color:
                    legal_moves.append([pos[0],pos[1]-2])

        if board_list[pos[0]][pos[1]+1] in ['RWay','XWay']:
            if [pos[0],pos[1]+1] not in legal_moves:
                if state_list[pos[0]][pos[1]+1].is_empty():
                    legal_moves.append([pos[0],pos[1]+1])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0],pos[1]+1])
                elif state_list[pos[0]][pos[1]+1].color != chess.color:
                    legal_moves.append([pos[0],pos[1]+1])
        elif board_list[pos[0]][pos[1]+2] == 'CWay':
            if [pos[0],pos[1]+2] not in legal_moves:
                if state_list[pos[0]][pos[1]+2].is_empty():
                    legal_moves.append([pos[0],pos[1]+2])
                    engineer_moves_recursion(legal_moves,state_list,[pos[0],pos[1]+2])
                elif state_list[pos[0]][pos[1]+2].color != chess.color:
                    legal_moves.append([pos[0],pos[1]+2])


    elif board_list[pos[0]][pos[1]] == 'RWay':
        if board_list[pos[0]-1][pos[1]] in ['RWay','XWay','CWay']:
            if [pos[0]-1,pos[1]]


















# 普通路径搜索
def railway_moves(state_list,chess):
    """铁路格子的合法走法"""
    # chess: Game_Grid
    # return: list, 元素为字符串，如'0010'
    # 1. 获取棋子的位置
    # 2. 获取棋子的合法走法
    # 3. 返回
    pos = chess.pos
    legal_moves=[]
    if chess.type == '工兵':
        return engineer_moves(chess)
    else:
        #先做首轮4边搜索确定搜索方向
        left,right,up,down = 0,0,0,0
        if board_list[pos[0]-1][pos[1]] == 'RWay' or board_list[pos[0]-1][pos[1]] == 'XWay' or board_list[pos[0]-2][pos[1]] == 'CWay':
            up = 1
        if board_list[pos[0]+1][pos[1]] == 'RWay' or board_list[pos[0]+1][pos[1]] == 'XWay' or board_list[pos[0]+2][pos[1]] == 'CWay':
            down = 1
        if board_list[pos[0]][pos[1]-1] == 'RWay' or board_list[pos[0]][pos[1]-1] == 'XWay' or board_list[pos[0]][pos[1]-2] == 'CWay':
            left = 1
        if board_list[pos[0]][pos[1]+1] == 'RWay' or board_list[pos[0]][pos[1]+1] == 'XWay' or board_list[pos[0]][pos[1]+2] == 'CWay':
            right = 1

        if up:
            for i in range(pos[0]-1,-1,-1):
                if board_list[i][pos[1]] is 'None' :
                    continue
                if state_list[i][pos[1]].is_empty():
                    legal_moves.append([i,pos[1]])
                elif state_list[i][pos[1]].color != chess.color:
                    legal_moves.append([i,pos[1]])
                    break
                else:
                    break

                if board_list[i][pos[1]] == 'XWay':
                    if board_list[i-1][pos[1]-1]=='XWay':
                        for j in range(pos[1]-1,-1,-1):
                            if board_list[i-1][j] is 'Norm':
                                break
                            if state_list[i-1][j].is_empty():
                                legal_moves.append([i-1,j])
                            if state_list[i-1][j].color != chess.color:
                                legal_moves.append([i-1,j])
                                break
                    elif board_list[i-1][pos[1]+1]=='XWay':
                        for j in range(pos[1]+1,17):
                            if board_list[i-1][j] is 'Norm':
                                break
                            if state_list[i-1][j].is_empty():
                                legal_moves.append([i-1,j])
                            if state_list[i-1][j].color != chess.color:
                                legal_moves.append([i-1,j])
                                break
        else:
            if board_list[pos[0]-1][pos[1]] == 'None':
                pass
            elif state_list[pos[0]-1][pos[1]].is_empty():
                legal_moves.append([pos[0]-1,pos[1]])
            elif state_list[pos[0]-1][pos[1]].color != chess.color and board_list[pos[0]-1][pos[1]] != 'Camp':
                legal_moves.append([pos[0]-1,pos[1]])


    if down:
        for i in range(pos[0]+1,17):
            if board_list[i][pos[1]] is 'None' :
                continue
            if state_list[i][pos[1]].is_empty():
                legal_moves.append([i,pos[1]])
            elif state_list[i][pos[1]].color != chess.color:
                legal_moves.append([i,pos[1]])
                break
            else:
                break

            if board_list[i][pos[1]] == 'XWay':
                if board_list[i+1][pos[1]-1]=='XWay':
                    for j in range(pos[1]-1,-1,-1):
                        if board_list[i+1][j] is 'Norm':
                            break
                        if state_list[i+1][j].is_empty():
                            legal_moves.append([i+1,j])
                        if state_list[i+1][j].color != chess.color:
                            legal_moves.append([i+1,j])
                            break
                elif board_list[i+1][pos[1]+1]=='XWay':
                    for j in range(pos[1]+1,17):
                        if board_list[i+1][j] is 'Norm':
                            break
                        if state_list[i+1][j].is_empty():
                            legal_moves.append([i+1,j])
                        if state_list[i+1][j].color != chess.color:
                            legal_moves.append([i+1,j])
                            break
    else:
        if board_list[pos[0]+1][pos[1]] == 'None':
            pass
        elif state_list[pos[0]+1][pos[1]].is_empty():
            legal_moves.append([pos[0]+1,pos[1]])
        elif state_list[pos[0]+1][pos[1]].color != chess.color and board_list[pos[0]+1][pos[1]] != 'Camp':
            legal_moves.append([pos[0]+1,pos[1]])

    if left:
        for i in range(pos[1]-1,-1,-1):
            if board_list[pos[0]][i] is 'None' :
                continue
            if state_list[pos[0]][i].is_empty():
                legal_moves.append([pos[0],i])
            elif state_list[pos[0]][i].color != chess.color:
                legal_moves.append([pos[0],i])
                break
            else:
                break

            if board_list[pos[0]][i] == 'XWay':
                if board_list[pos[0]-1][i-1]=='XWay':
                    for j in range(pos[0]-1,-1,-1):
                        if board_list[j][i-1] is 'Norm':
                            break
                        if state_list[j][i-1].is_empty():
                            legal_moves.append([j,i-1])
                        if state_list[j][i-1].color != chess.color:
                            legal_moves.append([j,i-1])
                            break
                elif board_list[pos[0]+1][i-1]=='XWay':
                    for j in range(pos[0]+1,17):
                        if board_list[j][i-1] is 'Norm':
                            break
                        if state_list[j][i-1].is_empty():
                            legal_moves.append([j,i-1])
                        if state_list[j][i-1].color != chess.color:
                            legal_moves.append([j,i-1])
                            break
    else:
        if board_list[pos[0]][pos[1]-1] == 'None':
            pass
        elif state_list[pos[0]][pos[1]-1].is_empty():
            legal_moves.append([pos[0],pos[1]-1])
        elif state_list[pos[0]][pos[1]-1].color != chess.color and board_list[pos[0]][pos[1]-1] != 'Camp':
            legal_moves.append([pos[0],pos[1]-1])

    if right:
        for i in range(pos[1]+1,17):
            if board_list[pos[0]][i] is 'None' :
                continue
            if state_list[pos[0]][i].is_empty():
                legal_moves.append([pos[0],i])
            elif state_list[pos[0]][i].color != chess.color:
                legal_moves.append([pos[0],i])
                break
            else:
                break

            if board_list[pos[0]][i] == 'XWay':
                if board_list[pos[0]-1][i+1]=='XWay':
                    for j in range(pos[0]-1,-1,-1):
                        if board_list[j][i+1] is 'Norm':
                            break
                        if state_list[j][i+1].is_empty():
                            legal_moves.append([j,i+1])
                        if state_list[j][i+1].color != chess.color:
                            legal_moves.append([j,i+1])
                            break
                elif board_list[pos[0]+1][i+1]=='XWay':
                    for j in range(pos[0]+1,17):
                        if board_list[j][i+1] is 'Norm':
                            break
                        if state_list[j][i+1].is_empty():
                            legal_moves.append([j,i+1])
                        if state_list[j][i+1].color != chess.color:
                            legal_moves.append([j,i+1])
                            break
    else:
        if board_list[pos[0]][pos[1]+1] == 'None':
            pass
        elif state_list[pos[0]][pos[1]+1].is_empty():
            legal_moves.append([pos[0],pos[1]+1])
        elif state_list[pos[0]][pos[1]+1].color != chess.color and board_list[pos[0]][pos[1]+1] != 'Camp':
            legal_moves.append([pos[0],pos[1]+1])
    return legal_moves






def is_legal_move(state_list,chess,move):
    """判断走法是否合法"""
















def get_legal_moves(chess):
"""获取某个棋子的合法走法"""
    if chess == '工兵':
        y,x = chess.pos




def get_all_legal_moves(state_list):
    """获取所有合法走法"""
    # state_list: 17*17, 二维列表
    # return: list, 元素为字符串，如'0010'
    # 1. 获取所有棋子的位置
    # 2. 获取每个棋子的合法走法
    # 3. 合并所有棋子的合法走法
    # 4. 返回
    all_legal_moves = []
    for i in range(17):
        for j in range(17):
            if state_list[i][j] != '一一':
                all_legal_moves.extend(get_legal_moves(state_list, i, j))
    return all_legal_moves



if __name__ =='__main__':
    print('hello world')




# 用python 实现 四国军棋 游戏





