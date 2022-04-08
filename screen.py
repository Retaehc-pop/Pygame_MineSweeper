import pygame

class StartScreen:
  def __init__(self,screen_width,screen_height) -> None:
      self.screen_width = screen_width
      self.screen_height = screen_height
      self.font = pygame.font.SysFont("Comic sans", 50)
      self.font_mini = pygame.font.SysFont("Comic sans", 20)

  def draw(self, screen: pygame.Surface) -> None:
      screen.blit(self.font.render("Minesweeper", True, (0, 0, 0)), (180, 200))
      screen.blit(self.font_mini.render("[SPACE] to start/reset", True, (0, 0, 0)), (self.screen_width//3, self.screen_height//2))


class WinScreen:
  def __init__(self,time,player_map) -> None:
      self.time_used = time
      self.total_bomb = player_map.mine_num

  def draw(self, screen: pygame.Surface) -> None:
      pass

class LostScreen:
  def __init__(self,time,player_map) -> None:
      self.time_used = time
      self.total_bomb = player_map.mine_num
      self.font = pygame.font.SysFont("Comic sans", 50)

  def draw(self, screen: pygame.Surface) -> None:
      screen.blit(self.font.render("You get KABOOMED", True, (0, 0, 0)), (100, 200))
      screen.blit(self.font.render(f"time:{self.time_used/1000}", True, (0, 0, 0)), (200, 400))

