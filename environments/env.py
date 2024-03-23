import numpy as np

from board import Grid_list



class Game(object):
    def __init__(self):
        self.board = np.zeros((10,10))




    def game_init(self):
        '''
        初始化游戏
        :return:
        '''
        self.board.init()

    def game_layout(self):
        '''
        玩家开局布局
        :return:
        '''
         pass

    def game_start(self):
        '''
        游戏开始
        :return:
        '''
        pass

    def game_end(self):
        '''
        游戏结束
        :return:
        '''
        pass

    def player_lives(self):
        '''
        根据军棋是否存在判断玩家是否存活
        [1,1,1,1]
        :return:
        '''
        pass

    def player_color(self):
        '''
        当前玩家方向
        [1,0,0,0]
        :return:
        '''
        pass





if __name__ == '__main__':


    game = Game()
    game.game_init()
    game.game_layout()
    game.game_start()
    game.game_end()
    game.player_lives()
    game.player_color()

    pass