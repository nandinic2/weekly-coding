import random

def path_finder(maze):
    # starting point
    s = maze[0][0]
    # ending point
    e = maze[len(maze)-1][len(maze)-1]
    # makes maze into list
    maze = list(map(list, a.splitlines()))
    # saves maze nodes in hash
    level = {s:0}
    parent = {s: None}
    # current position
    frontier = [s]
    # sets length of maze
    length = len(maze)
    # count
    i = 1
    # while there is something in frontier
    while frontier:
        # where explored nodes are
        next = []
        for u in frontier:
            for v in Adj:
                if v not in level:
                    # adds positions to the level and parent hash
                    level[v] = i
                    parent[v] = u
                    # add v to explored list
                    next.append(v)
                    # if location is equal to the end
                    if v == e:
                        return True
                    else:
                        return False
        # moves position forward
        i += 1


def find_edges(maze):
    node = [0,0]
    x,y = node
    edges = []
    length = len(maze)
    # add conditions for nw, sw, ne, se
    for x,y in (x, y+1), (x, y-1), (x+1, y), (x-1, y):
        if 0 <= x < length and 0 <= y < length:
            # check if matrix[x][y] is a free space
            if maze[x][y] == '.':
                edges.append([x,y])
    return edges


def path_finder(maze):
  node = [0,0]
  queue = [[node]]
  #keeps nodes already iterated through
  explored = []
  goal = [len(maze)-1, len(maze)-1]
  while queue:
    #FIFO
    path = queue.pop(0)
    node = path[-1]
    # check of we have searched path before
    if node not in explored:
      explored.append(node)
      #layer one connections to node
      edges = find_edges(maze)
      for edge in edges:
        new_list = list(path)
        new_list.append(edge)
        queue.append(new_list)
        if edge == goal:
            return True
