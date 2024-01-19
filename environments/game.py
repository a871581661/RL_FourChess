import numpy as np
import copy
import time

from collections import deque   # 这个队列用来判断长将或长捉
import random


BOARD_LENGTH = 17

# 列表来表示棋盘，红方在上，黑方在下。使用时需要使用深拷贝
'''
Norm:普通格子
RWay:铁路格子
XWay:拐弯铁路格子
Camp:行营格子
CWay:中心铁路格子
Flag:大本营格子
'''
board_list= [
    ['None', 'None', 'None', 'None', 'None', 'None', 'Norm', 'Flag', 'Norm', 'Flag', 'Norm', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'RWay', 'RWay', 'RWay', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Norm', 'Camp', 'Norm', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'XWay', 'RWay', 'RWay', 'RWay', 'XWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['Norm', 'RWay', 'RWay', 'RWay', 'RWay', 'XWay', 'CWay', 'None', 'CWay', 'None', 'CWay', 'XWay', 'RWay', 'RWay', 'RWay', 'RWay', 'Norm', ],
    ['Flag', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'Flag', ],
    ['Norm', 'RWay', 'Norm', 'Camp', 'Norm', 'RWay', 'CWay', 'None', 'CWay', 'None', 'CWay', 'RWay', 'Norm', 'Camp', 'Norm', 'RWay', 'Norm', ],
    ['Flag', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'Flag', ],
    ['Norm', 'RWay', 'RWay', 'RWay', 'RWay', 'XWay', 'CWay', 'None', 'CWay', 'None', 'CWay', 'XWay', 'RWay', 'RWay', 'RWay', 'RWay', 'Norm', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'XWay', 'RWay', 'RWay', 'RWay', 'XWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Norm', 'Camp', 'Norm', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'Camp', 'Norm', 'Camp', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'RWay', 'RWay', 'RWay', 'RWay', 'RWay', 'None', 'None', 'None', 'None', 'None', 'None', ],
    ['None', 'None', 'None', 'None', 'None', 'None', 'Norm', 'Flag', 'Norm', 'Flag', 'Norm', 'None', 'None', 'None', 'None', 'None', 'None', ]
]


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

#棋盘格类型规则确定:铁路，普通，行营，大本营等
class Game_Grid(object):
    def __init__(self,protect,railway,camp,connect):
        self.protect = protect
        self.railway = railway
        self.camp = camp
        self.connect = connect

class Grid_Railway(Game_Grid):
    def __init__(self):
        super().__init__(protect=False,railway=True,camp=False,connect=True)





###*******************棋子走法规则*******************###
def get_legal_moves(state_list, y, x):
"""获取某个棋子的合法走法"""
    # state_list: 17*17, 二维列表
    # y, x: 棋子的坐标
    # return: list, 元素为字符串，如'0010'
    # 1. 获取棋子的类型
    # 2. 根据棋子的类型，获取棋子的合法走法
    # 3. 返回
    chess_type = state_list[y][x]
    if chess_type == '一一':
        return []
    elif chess_type == '司令':
        return get_legal_moves_siling(state_list, y, x)
    elif chess_type == '军长':
        return get_legal_moves_junchang(state_list, y, x)
    elif chess_type == '师长':
        return get_legal_moves_shizhang(state_list, y, x)
    elif chess_type == '旅长':
        return get_legal_moves_lvzhang(state_list, y, x)
    elif chess_type == '团长':
        return get_legal_moves_tuanzhang(state_list, y, x)
    elif chess_type == '营长':
        return get_legal_moves_yingzhang(state_list, y, x)
    elif chess_type == '连长':
        return get_legal_moves_lianzhang(state_list, y, x)
    elif chess_type == '排长':
        return get_legal_moves_paizhang(state_list, y, x)
    elif chess_type == '工兵':
        return get_legal_moves_gongbing(state_list, y, x)
    elif chess_type == '炸弹':
        return get_legal_moves_zhadan(state_list, y, x)
    elif chess_type == '地雷':
        return get_legal_moves_dilei(state_list, y, x)
    elif chess_type == '军旗':
        return get_legal_moves_junqi(state_list, y, x)
    else:
        raise ValueError('棋子类型错误')




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





