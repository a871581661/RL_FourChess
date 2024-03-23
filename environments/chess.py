import numpy as np
EnvChess2RealChess = { 1:'军棋',2:'工兵',3:'排长',4:'连长',5:'营长',6:'团长',7:'旅长',8:'师长',9:'军长',10:'司令',11:'地雷',12:'炸弹'}
RealChess2EnvChess = { '军棋':1,'工兵':2,'排长':3,'连长':4,'营长':5,'团长':6,'旅长':7,'师长':8,'军长':9,'司令':10,'地雷':11,'炸弹':12}

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

def chess_compare(attack_chess:str,defand_chess:str):
    '''
    比较两个棋子的大小
    :param attack_chess:
    :param defand_chess:
    :return: 进攻方获胜 >1 ，防守方获胜 <-1 ，平局 0
    '''
    real_ac = EnvChess2RealChess[attack_chess]
    real_dc = EnvChess2RealChess[defand_chess]
    if defand_chess == '地雷':
        if attack_chess == '工兵':
            return 1
        else:
            return -1
    if defand_chess == '炸弹' or attack_chess == '炸弹':
        return 0

    return real_ac - real_dc









