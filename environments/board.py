


BOARD_LENGTH = 17
DIRECTIONS={'left':[0,-1],'right':[0,1],'up':[-1,0],'down':[1,0]}

RAILWAY_LIST = []

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


#棋盘格类型规则确定:铁路，普通，行营，大本营等
class NormGrid(object):
    def __init__(self,pos:list,):
        self.pos = pos
        self.up = self.upGrid()
        self.down = self.downGrid()
        self.left = self.leftGrid()
        self.right = self.rightGrid()

    ### 用于寻找方向
    def upGrid(self):
        if self.pos[0]==0:
            return None
        else:
            return [self.pos[0]-1,self.pos[1]]
    def downGrid(self):
        if self.pos[0]==BOARD_LENGTH-1:
            return None
        else:
            return [self.pos[0]+1,self.pos[1]]
    def leftGrid(self):
        if self.pos[1]==0:
            return None
        else:
            return [self.pos[0],self.pos[1]-1]
    def rightGrid(self):
        if self.pos[1]==BOARD_LENGTH-1:
            return None
        else:
            return [self.pos[0],self.pos[1]+1]





class CampGrid(NormGrid):
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.up = self.upGrid()
        self.down = self.downGrid()
        self.left = self.leftGrid()
        self.right = self.rightGrid()
        self.type = 'Camp'



class RWayGrid(NormGrid):
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.up = self.upGrid()
        self.down = self.downGrid()
        self.left = self.leftGrid()
        self.right = self.rightGrid()
        self.type = 'RWay'


class CWayGrid(NormGrid):
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.up = self.upGrid()
        self.down = self.downGrid()
        self.left = self.leftGrid()
        self.right = self.rightGrid()
        self.type = 'CWay'

    def upGrid(self):
        if board_list[self.pos[0]-1][self.pos[1]]=='None':
            return [self.pos[0]-2,self.pos[1]]
        else:
            return [self.pos[0]-1,self.pos[1]]
    def downGrid(self):
        if board_list[self.pos[0]+1][self.pos[1]]=='None':
            return [self.pos[0]+2,self.pos[1]]
        else:
            return [self.pos[0]+1,self.pos[1]]
    def leftGrid(self):
        if board_list[self.pos[0]][self.pos[1]-1]=='None':
            return [self.pos[0],self.pos[1]-2]
        else:
            return [self.pos[0],self.pos[1]-1]
    def rightGrid(self):
        if board_list[self.pos[0]][self.pos[1]+1]=='None':
            return [self.pos[0],self.pos[1]+2]
        else:
            return [self.pos[0],self.pos[1]+1]





class XWayGrid(NormGrid):
    diretions = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.up = self.upGrid()
        self.down = self.downGrid()
        self.left = self.leftGrid()
        self.right = self.rightGrid()
        self.type = 'XWay'
        self.connection = self._getConnection()


    def _getConnection(self):

        for diretion in diretions:
            if board_list[self.pos[0]+diretion[0]][self.pos[1]+diretion[1]]!='XWay':
                return [self.pos[0]+diretion[0],self.pos[1]+diretion[1]]
















