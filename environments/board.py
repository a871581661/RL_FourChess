


BOARD_LENGTH = 17
DIRECTIONS={'left':[0,-1],'right':[0,1],'up':[-1,0],'down':[1,0]}

RAILWAY_LIST = ['RWay','XWay','CWay']
ROAD_LIST = ['Flag','Norm']
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
        self.directions = None
        self.connections= self._get_connections()
        self.chess=None

    def _get_connections(self):
        # 判断边界,
        # 方向为上下左右
        connections=[[-1,0],[1,0],[0,-1],[0,1]]
        y = self.pos[0]
        x = self.pos[1]
        if y == 0:
            connections.pop(0)
        if y == BOARD_LENGTH:
            connections.pop(1)
        if x == 0:
            connections.pop(2)
        if x == BOARD_LENGTH:
            connections.pop(3)
        return connections

    def compare(self):



class CampGrid(NormGrid):
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.connections = self._get_connections()

    def _get_connections(self):
        # 判断边界,
        # 方向为上下左右
        connections=[[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]
        return connections



class RWayGrid(NormGrid):
    '''
    direction : [[0, -1], [0, 1], [-1, 0], [1, 0]], 显示存在铁路的方向

    '''
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.directions = self._get_directions()
        self.connections = self._get_connections()
        self.step = [1,1,1,1]

    def _get_directions(self):
        directions = []
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for dir in dirs:
            if self.pos[0]+dir[0]>=BOARD_LENGTH or self.pos[1]+dir[1]>=BOARD_LENGTH:
                continue
            if board_list[self.pos[0]+dir[0]][self.pos[1]+dir[1]] in RAILWAY_LIST:
                directions.append(dir)
        return directions
    def _get_connections(self):
        connections = []
        staight_ways = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        tile_ways =[[-1, -1], [-1, 1], [1, -1], [1, 1]]
        y,x = self.pos
        for way in staight_ways:
            way_y,way_x =way
            if board_list[y+way_y][x+way_x] in ROAD_LIST:
                connections.append(way)
        for way in tile_ways:
            way_y,way_x =way
            if board_list[y+way_y][x+way_x] == 'Camp':
                connections.append(way)
        return connections



class XWayGrid(NormGrid):
    def __init__(self, pos: list, ):
        '''
        extra_diretion : xway_direction,extra_direction
        XWay.extra_diretion = (xway_direction,extra_direction)
        :param pos:
        '''
        super().__init__(pos)
        self.directions = self._get_directions()
        self.connections = self._get_connections()
        self.extra_direction = self._get_extra_direction()
        self.step = [1, 1, 1, 1]

    def _get_directions(self):
        directions = []
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        xway_towards= [[1, 1], [1, -1], [-1, 1], [-1,-1]]
        for dir in dirs:
            if self.pos[0] + dir[0] >= BOARD_LENGTH or self.pos[1] + dir[1] >= BOARD_LENGTH:
                continue
            if board_list[self.pos[0] + dir[0]][self.pos[1] + dir[1]] in RAILWAY_LIST:
                directions.append(dir)
        return directions

    def _get_extra_direction(self):
        y,x = self.pos
        directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dir in directions:
            dir_y ,dir_x = dir
            if board_list[y+dir_y][board_list[x+dir_x]] == 'XWay':
                xway_direction = dir
                break
        xway_y,xway_x = xway_direction
        if board_list[y+xway_y][x]=='None':
            extra_direction = [xway_y,0]
        else:
            extra_direction= [0,xway_x]
        return xway_direction,extra_direction







for i in dir:
    while board_list.chess ==  empty :
        list.append(pos)

        if board_list == xway:



class CWayGrid(NormGrid):
    def __init__(self, pos: list, ):
        super().__init__(pos)
        self.directions = self._get_directions()
        self.step = [1, 1, 1, 1]

    def _get_directions(self):
        directions = []
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for dir in dirs:
            if self.pos[0] + dir[0] >= BOARD_LENGTH or self.pos[1] + dir[1] >= BOARD_LENGTH:
                continue
            if board_list[self.pos[0] + dir[0]][self.pos[1] + dir[1]] in RAILWAY_LIST:
                directions.append(dir)
        return directions




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





def get_railway_move():
    board_list[x,y].direction
    for direction in board_list[x,y].directions:
        while board_list[x,y]






class CHESS(object):
    def __init__(self):

        is_boom=False
        is_eng=False
        is_flag=False
        is_mine=False
        value = 0







def move(move):
    if board_list[move].chess:
        board_list[move].chess.attack()

