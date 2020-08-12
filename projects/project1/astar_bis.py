from typing import List, Any


class Node:

    def __init__(self, parent=None, position=None, state=""):
        self.parent = parent
        self.position = position
        self.state = state

        self.g = 0
        self.h = 0
        self.f = 0

    def addPArent(self, parent):
        self.parent=parent
    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return "The state : "+self.state + " The position  : (" + str(self.position[0]) + "," + str(self.position[1])+")";


def astar(maze, start, end):
    start_node = start
    start_node.g = start_node.h = start_node.f = 0
    end_node = end
    end_node.g = end_node.h = end_node.f = 0
    open_list: List[Any] = []
    closed_list = []

    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []
        for item in maze[current_node]:
            item.addPArent(current_node)
            children.append(item)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            #Cost function is the number of links beetween current and starting point
            child.g = current_node.g + 1
            #THe heuristics is the estimed distance value beetween current point and goal
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.h=0
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue
            open_list.append(child)


def main():

    maze = {

        Node(state='A', position=(0, 0)): [Node(state='B', position=(0, 4)), Node(state='C', position=(2, 0))],
        Node(state='B', position=(0, 4)): [Node(state='F', position=(2, 4))],
        Node(state='C', position=(2, 0)): [Node(state='D', position=(2, 1))],
        Node(state='D', position=(2, 1)): [Node(state='E', position=(4, 1))],
        Node(state='E', position=(4, 1)): [Node(state='J', position=(4, 0))],
        Node(state='F', position=(2, 4)): [Node(state='G', position=(2, 3))],
        Node(state='G', position=(2, 3)): [Node(state='H', position=(3, 3))],
        Node(state='H', position=(3, 3)): [Node(state='I', position=(3, 1))],
        Node(state='I', position=(3, 1)): [Node(state='E', position=(4, 1))],
        Node(state='J', position=(4, 0)): None
    }

    start = Node(state='A', position=[0, 0])
    end = Node(state='J', position=[4, 0])

    path = astar(maze, start, end)
    for item in path:
        print(item)


if __name__ == '__main__':
    main()
