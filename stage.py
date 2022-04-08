import random
import pygame
import string


class Map:
    def __init__(self, width, height, tile_size,mine_percent):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.map = [["-" for x in range(width)] for y in range(height)]
        self.mine_num = int(width*height*mine_percent)
        self.generate_bomb()
        """
        * = bomb
        # = nothing
        f = mark bomb
        - = unclicked
        1-9 = number of bombs around
        """
        self.Tile_color = (142,204,57)
        self.Tile_alternate_color = (167,217,72)
        self.mark_color = (245, 179, 66)
        self.nothing_color = (215,184,153)
        self.nothing_alternate_color = (229,194,159)
        self.num_color = [(25,118,210),(57,142,61),(211,47,47),(123,31,162),(255,143,0),(72,230,241),(255,191,0),(73,39,4)]
        self.font = pygame.font.SysFont("Comic sans", int(self.tile_size//1.2))

    def generate_bomb(self):
        for i in range(self.mine_num):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.map[y][x] != "*":
                self.map[y][x] = "*"
            else:
                i -= 1

    def clicked_bomb(self, x, y):
        if self.map[y][x] == "*":
            return True
        else:
            return False

    def check_bomb(self, x, y):
      if self.map[y][x] == "-":
        if (0 <= x < self.width) and (0 <= y < self.height):
            to_check = []
            area = [(-1, -1), (-1, 0), (-1, 1), (0, -1),(0, 1), (1, -1), (1, 0), (1, 1)]
            bomb_count = 0
            for check_pos in area:
                if (x+check_pos[1] >= 0 and x+check_pos[1] < self.width) and (y+check_pos[0] >= 0 and y+check_pos[0] < self.height):
                    if self.map[y+check_pos[0]][x+check_pos[1]] == "*":
                        bomb_count += 1
                    elif self.map[y+check_pos[0]][x+check_pos[1]] == "-":
                      to_check.append((x+check_pos[1], y+check_pos[0]))
            self.map[y][x] = str(bomb_count)
            if bomb_count == 0:
                for check_pos in to_check:
                    self.check_bomb(check_pos[0], check_pos[1])
            

    def draw(self, screen):
        for x in range(self.height):
            for y in range(self.width):
                if self.map[y][x] == "-" or self.map[y][x] == "*":
                # if self.map[y][x] == "-":
                    if (x+y)%2 == 0:
                      pygame.draw.rect(screen, self.Tile_color, (x*self.tile_size,y*self.tile_size, self.tile_size, self.tile_size))
                    else:
                      pygame.draw.rect(screen, self.Tile_alternate_color, (x*self.tile_size,y*self.tile_size, self.tile_size, self.tile_size))
                # elif self.map[y][x] == "*":
                #   pygame.draw.rect(screen, (255,0,0), (x*self.tile_size,y*self.tile_size, self.tile_size, self.tile_size))

                elif self.map[y][x] in string.digits:
                    if (x+y)%2 == 0:
                      pygame.draw.rect(screen, self.nothing_color, (x*self.tile_size,y*self.tile_size, self.tile_size, self.tile_size))
                    else:
                      pygame.draw.rect(screen, self.nothing_alternate_color, (x*self.tile_size,y*self.tile_size, self.tile_size, self.tile_size))

                    if not self.map[y][x] == "0":
                      txt_to_render = self.font.render(self.map[y][x], True, self.num_color[int(self.map[y][x])-1])
                      screen.blit(txt_to_render, (x*self.tile_size +self.tile_size//4, y*self.tile_size))

                elif self.map[y][x] == "f":
                    pygame.draw.rect(screen, self.mark_color, (x*self.tile_size,
                                     y*self.tile_size, self.tile_size, self.tile_size))

