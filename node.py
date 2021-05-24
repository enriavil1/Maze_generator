import pygame

class Node():

    def __init__(self, row, column, size):
        self.row = row
        self.column = column
        self.size = size

        self.default_connections = {}
        self.connections = {}

        self.moves = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}


    def get_default_connections(self):
        connections = []
        for node in self.default_connections.keys():
            if node != None:
                connections.append((node.row, node.column))
        
        return connections

    def get_connections(self):
        connections = []
        for node in self.default_connections.keys():
            move = self.default_connections[node]

            if self.moves[move]:
                self.connections[node] = move
                connections.append(node)
        
        return connections
    
    def toggle_wall(self, dir, screen):
        self.moves[dir] = True

        for move in self.moves.keys():

            if self.moves[move] and move == "UP":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y)
                end_pos = (x+self.size, y)
                pygame.draw.line(screen, (0,0,0), start_pos, end_pos,3)
                

            
            if self.moves[move] and move == "DOWN":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y+self.size)
                end_pos = (x+self.size, y+self.size)
                pygame.draw.line(screen, (0,0,0), start_pos, end_pos,3)
            
            
            if self.moves[move] and move == "RIGHT":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x+self.size, y)
                end_pos = (x+self.size, y+self.size)
                pygame.draw.line(screen, (0,0,0), start_pos, end_pos,3)

            
            if self.moves[move] and move == "LEFT":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y+self.size)
                end_pos = (x, y)
                pygame.draw.line(screen, (0,0,0), start_pos, end_pos,3)
    
    def opposite_toggle_wall(self, move):
        if move == "UP":
            self.moves["DOWN"] = True
        
        if move == "DOWN":
            self.moves["UP"] = True
        
        if move == "RIGHT":
            self.moves["LEFT"] = True
        
        if move == "LEFT":
            self.moves["RIGHT"] = True
        
    
    def draw_walls(self, screen):

        for move in self.moves:

            if self.moves[move] == False and move == "UP":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y)
                end_pos = (x+self.size, y)
                pygame.draw.line(screen, (255,255,255), start_pos, end_pos, 3)

            
            if self.moves[move] == False and move == "DOWN":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y+self.size)
                end_pos = (x+self.size, y+self.size)
                pygame.draw.line(screen, (255,255,255), start_pos, end_pos, 3)
            
            
            if self.moves[move] == False and move == "RIGHT":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x+self.size, y)
                end_pos = (x+self.size, y+self.size)
                pygame.draw.line(screen, (255,255,255), start_pos, end_pos, 3)

            
            if self.moves[move] == False and move == "LEFT":
                x = self.column* self.size
                y = self.row * self.size
                start_pos = (x, y+self.size)
                end_pos = (x, y)
                pygame.draw.line(screen, (255,255,255), start_pos, end_pos, 3)
            
               
            



        