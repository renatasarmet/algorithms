import numpy as np
import sys

possiveis = [[-1,0],
             [0,1],
             [1,0],
             [0,-1]
            ]

def verifica(pos_x, pos_y, maze):
    if pos_x < 0 or pos_y < 0:
        return False
    if pos_x > maze.shape[0]-1 or pos_y > maze.shape[1]-1:
        return False
    if maze[pos_x,pos_y] == 1:
        return False
    return True


def make_maze(maze, state, final):
    maze[state[0],state[1]] = 1
    list_states = []
    while state[0] != final[0] or state[1] != final[1]:
        nexts = []
        for p in possiveis:
            retorno = verifica(state[0]+p[0], state[1]+p[1], maze)
            if retorno:
                nexts.append([state[0]+p[0], state[1]+p[1]])
        if len(nexts) > 0:
            index = np.random.randint(0,len(nexts))
            state = nexts[index]
            del nexts[index]
            maze[state[0],state[1]] = 1
            list_states = nexts + list_states
        else:
            while True:
                percentage = .1
                index = np.random.randint(0,max(1,int(len(list_states)*percentage)))
                if verifica(list_states[index][0], list_states[index][1], maze):
                    state = list_states[index]
                    maze[state[0],state[1]] = 1
                    del list_states[index]
                    break
                del list_states[index]
    return maze

def maze_to_str(maze):
    maze_str = ''
    for i in range(maze.shape[0]):
        for j in range(maze.shape[1]):
            maze_str = maze_str + str(maze[i,j]) + ' '
        maze_str = maze_str[:-1]
        maze_str = maze_str + '\n'
    return maze_str


if __name__ == '__main__':

    if len(sys.argv) > 1:
        size = int(sys.argv[1].strip())
        file_name = f'input_maze_{size}.in'
        file = open(file_name,'w')

        maze = np.zeros((size,size),dtype=np.uint8)
        initial = (0,0)
        final = (size-1,size-1)
        maze_maked = make_maze(maze, initial, final)
        file.write(f"{size}\n")
        file.write(maze_to_str(maze))

        file.close()
    else:
        print("Error: you should enter the size")
