import pygame
from stage import Map
from screen import StartScreen, WinScreen, LostScreen
pygame.init()


def get_tile(pos,tile_size):
    return pos[0]//tile_size,pos[1]//tile_size

def draw(SCREEN,*args):
    SCREEN.fill((0,0,0))
    for arg in args:
        arg.draw(SCREEN)
    pygame.display.update()

"""
* = bomb
0 = nothing
f = mark bomb
- = unclicked
1-9 = number of bombs around
"""
def main():
    player_map = Map(32,32,HEIGHT//32,mine_percent=0.2)
    running = True
    game_end = False
    game_start = False
    win = False
    play_time = 0
    while running:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if keys[pygame.K_SPACE]:
            start_timer = pygame.time.get_ticks()
            game_end = False
            win = False
            player_map = Map(32,32,HEIGHT//32,mine_percent=0.2)

        # game
        mouse_tile = get_tile((mouse[0],mouse[1]),tile_size=player_map.tile_size)
        if not game_start:
            if keys[pygame.K_SPACE]:
                game_start = True
            draw(SCREEN,player_map,StartScreen(WIDTH,HEIGHT))
        else:
            if game_end:
                if win:
                    draw(SCREEN,player_map,WinScreen(play_time,player_map))
                else:
                    draw(SCREEN,player_map,LostScreen(play_time,player_map))
            else:
                if not "-" in [tile for row in player_map.map for tile in row ]:
                    game_end = True
                    win = True
                    play_time = (pygame.time.get_ticks()-start_timer)

                if click[0]:
                    is_bomb = player_map.clicked_bomb(mouse_tile[0],mouse_tile[1])
                    if is_bomb:
                        play_time = (pygame.time.get_ticks()-start_timer)
                        game_end = True
                        win = False
                    else:
                        player_map.check_bomb(mouse_tile[0],mouse_tile[1])
                # elif click[2]: 
                #     if player_map.map[mouse_tile[1]][mouse_tile[0]] == "-":
                #         player_map.map[mouse_tile[1]][mouse_tile[0]] = "f" 
                #     elif player_map.map[mouse_tile[1]][mouse_tile[0]] == "f":
                #         player_map.map[mouse_tile[1]][mouse_tile[0]] = "-" 
                draw(SCREEN, player_map)


        

if __name__ == '__main__':
    HEIGHT = 640
    WIDTH = 640
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MINESWEEPER")
    main()