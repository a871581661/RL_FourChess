BOARD_SHAPE = 17
BOARD_LENGTH = BOARD_SHAPE-1
RAILWAY_LIST = ['RWay','XWay','CWay']
ROAD_LIST = ['Flag','Norm']
'''
负责提供Grid_list,棋盘格子的初始化
'''


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

# gen
Grid_list = [[None for _ in range(BOARD_SHAPE)] for _ in range(BOARD_SHAPE)]


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
        y,x = self.pos
        if y == 0:
            connections.pop(0)
        if y == BOARD_LENGTH:
            connections.pop(1)
        if x == 0:
            connections.pop(2)
        if x == BOARD_LENGTH:
            connections.pop(3)

        for connection in connections:
            c_y,c_x = connection
            if board_list[y+c_y][x+c_x] == 'None':
                connections.remove(connection)

        return connections

    def compare(self):
        pass

class FlagGrid(NormGrid):
    def __init__(self,pos:list,):
        super().__init__(pos)
        self.connections = self._get_connections()




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
            if self.pos[0]+dir[0]>=BOARD_LENGTH or self.pos[1]+dir[1]>BOARD_LENGTH:
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
        self.target_direction,self.extra_direction = self._get_extra_direction()
        self.step = [1, 1, 1, 1]

    def _get_directions(self):
        directions = []
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        xway_towards= [[1, 1], [1, -1], [-1, 1], [-1,-1]]
        for dir in dirs:
            if self.pos[0] + dir[0] >= BOARD_LENGTH or self.pos[1] + dir[1] > BOARD_LENGTH:
                continue
            if board_list[self.pos[0] + dir[0]][self.pos[1] + dir[1]] in RAILWAY_LIST:
                directions.append(dir)
        return directions

    def _get_extra_direction(self):
        y,x = self.pos
        directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dir in directions:
            dir_y ,dir_x = dir
            if board_list[y+dir_y][x+dir_x] == 'XWay':
                xway_direction = dir
                break
        xway_y,xway_x = xway_direction
        if board_list[y+xway_y][x]=='None':
            extra_direction = [xway_y,0]
        else:
            extra_direction= [0,xway_x]
        return xway_direction,extra_direction



class CWayGrid(NormGrid):
    def __init__(self, pos: list, ):
        super().__init__(pos)

        self.directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        self.connections = None
        self.step = self._get_step()


    def _get_step(self):
        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        step = [1,1,1,1]
        for idx,dir in enumerate(dirs):
            if board_list[self.pos[0] + dir[0]][self.pos[1] + dir[1]] == 'None':
                step[idx] = 2
        return step


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

def creat_Grid_list():
    for idy,grids in enumerate(board_list):
        for idx,grid in enumerate(grids):
            if grid == 'None':
                Grid_list[idy][idx] = None
            elif grid == 'Norm':
                Grid_list[idy][idx] = NormGrid([idy,idx])
            elif grid == 'Flag':
                Grid_list[idy][idx] = FlagGrid([idy,idx])
            elif grid == 'Camp':
                Grid_list[idy][idx] = CampGrid([idy,idx])
            elif grid == 'RWay':
                Grid_list[idy][idx] = RWayGrid([idy,idx])
            elif grid == 'XWay':
                Grid_list[idy][idx] = XWayGrid([idy,idx])
            elif grid == 'CWay':
                Grid_list[idy][idx] = CWayGrid([idy,idx])



# 创建棋盘
creat_Grid_list()


def grids_init():
    pass


if __name__ == '__main__':
    pass