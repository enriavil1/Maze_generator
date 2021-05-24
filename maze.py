import pygame
import random
import time
from node import Node


class Maze():

    def __init__(self, screen, node_size, width, height):
        self.screen = screen
        self.node_size = node_size

        self.columns = width//node_size
        self.rows = height//node_size

        self.width = width
        self.height = height
        
        self.visited = [[False for j in range(self.columns)] for i in range(self.rows)]

        self.nodes = [[Node(i,j, node_size) for j in range(self.columns)] for i in range(self.rows)]
        self.node_graph = {}

        self.starting_node = self.nodes[0][0]
        self.ending_node = self.nodes[-1][-1]

        self.bfs_visits = set()
        self.path = []

        self.create_initial_connections()
    
    def create_initial_connections(self):
        for node in self.node_iter():
            row = node.row
            column = node.column
            node.default_connections[self.get_node(row-1, column)] = "UP"
            node.default_connections[self.get_node(row+1, column)] = "DOWN"
            node.default_connections[self.get_node(row, column+1)] = "RIGHT"
            node.default_connections[self.get_node(row, column-1)] = "LEFT"

    def get_node(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return self.nodes[row][column]
        else:
            return None
    
    def generate_graph(self):
        for node in self.node_iter():
            self.node_graph[node] = node.get_connections()
        
    def node_iter(self):
        for i in range(self.rows):
            for j in range(self.columns):
                yield self.nodes[i][j]


    def generate_maze(self, current = None):
        if current == None:
            current = self.nodes[0][0]
        
        i,j = current.row, current.column
        self.show_current_node(current)
        self.visited[i][j] = True

        choices = self.nodes[i][j].get_default_connections()
        random.shuffle(choices)

        for coordinates in choices:
            row = coordinates[0]
            column = coordinates[1]

            if self.visited[row][column] != True:
                node = self.nodes[row][column]
                move = current.default_connections[node]

                current.toggle_wall(move,self.screen)
                node.opposite_toggle_wall(move)

                current.connections[move] = node
                #time.sleep(.075)
                self.return_node_to_black(current)

                self.generate_maze(node)

            self.show_backtrack(current)
        self.return_node_to_black(current)

    
    def solve_bfs(self):
        self.mark_start_and_end()
        self.generate_graph()
        self.visited = set()
        self.path = [self.starting_node]
        path_and_node = [self.starting_node,self.path]

        bfs_queue = [path_and_node]

        while bfs_queue:
            current, self.path = bfs_queue.pop(0)

            self.visited.add(current)
            self.show_searched_nodes(current)

            for node in self.node_graph[current]:
                if node not in self.visited:
                    if current == self.ending_node:
                        self.path += [current]
                        self.make_path()
                        return self.path
                    else:
                        bfs_queue.append([node,self.path+[node]])

    def show_searched_nodes(self, node):
        if node == self.starting_node or node == self.ending_node:
            return

        x = node.column * self.node_size
        y = node.row * self.node_size

        rect = pygame.Rect(x, y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (100,100,255), rect, 0)
        node.draw_walls(self.screen)
        pygame.display.update()

    
    def show_current_node(self, node):
        x = node.column * self.node_size
        y = node.row * self.node_size

        rect = pygame.Rect(x, y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (255,0,255), rect, 0)
        pygame.display.update()

    def show_backtrack(self,node):
        x = node.column * self.node_size
        y = node.row * self.node_size

        rect = pygame.Rect(x, y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (0,0,255), rect, 0)
        node.draw_walls(self.screen)
        pygame.display.update()

    def return_node_to_black(self, node):
        x = node.column * self.node_size
        y = node.row * self.node_size

        rect = pygame.Rect(x, y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (0,0,0), rect, 0)
        node.draw_walls(self.screen)
        pygame.display.update()
    
    def mark_start_and_end(self):
        starting_x, starting_y = self.starting_node.column * self.node_size, self.starting_node.row * self.node_size

        rect = pygame.Rect(starting_x, starting_y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (255,0,0), rect, 0)
        self.starting_node.draw_walls(self.screen)

    
        ending_x, ending_y = self.ending_node.column * self.node_size, self.ending_node.row * self.node_size
        
        rect = pygame.Rect(ending_x, ending_y, self.node_size, self.node_size)
        pygame.draw.rect(self.screen, (0,255,0), rect, 0)
        self.ending_node.draw_walls(self.screen)
        pygame.display.update()
    
    def make_path(self):
        for i in range(len(self.path)-1):
            current = self.path[i]
            next_node = self.path[i+1]

            current_x, current_y = current.column * self.node_size + self.node_size//2, current.row * self.node_size + self.node_size//2
            next_x, next_y = next_node.column * self.node_size + self.node_size//2, next_node.row * self.node_size + self.node_size//2

            pygame.draw.line(self.screen, (255,255,0), (current_x,current_y),(next_x,next_y), 5)
            pygame.display.update()
            







