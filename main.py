import pygame
import sys
from maze import Maze

def create_grid(screen, node_size, height, width, color):
    for i in range(height):
        for j in range(width):

            rect = pygame.Rect(node_size*j, node_size*i, node_size, node_size)

            pygame.draw.rect(screen, color, rect, 1)


def main():

    width = 900
    height = 900
    node_size = 30
    black = (0,0,0)
    white = (255,255,255)

    pygame.init()
    screen = pygame.display.set_mode((width,height), 0, 32)
    screen.fill(black)
    create_grid(screen,node_size,height,width, white)

    running = True

    maze = Maze(screen, node_size, width, height)

    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    maze.generate_maze()
                    maze.solve_bfs()

        pygame.display.update()
    
    pygame.quit()
    sys.exit()

main()