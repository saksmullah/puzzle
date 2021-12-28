import os
import sys
import cfg
import random #/ to choose our picture randomly in the puzzle game
import pygame
from pygame.locals import *
pygame.init()


def isGameOver(board, size):
   assert isinstance(size, int)
   num_cells = size * size
   for i in range(num_cells - 1):
      if board[i] != i: return False
   return True


def moveR(board, blank_cell_idx, num_cols):
   if blank_cell_idx % num_cols == 0: return blank_cell_idx
   board[blank_cell_idx - 1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx - 1]
   return blank_cell_idx - 1


def moveL(board, blank_cell_idx, num_cols):
   if (blank_cell_idx + 1) % num_cols == 0: return blank_cell_idx
   board[blank_cell_idx + 1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx + 1]
   return blank_cell_idx + 1


def moveD(board, blank_cell_idx, num_cols):
   if blank_cell_idx < num_cols: return blank_cell_idx
   board[blank_cell_idx - num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx - num_cols]
   return blank_cell_idx - num_cols


def moveU(board, blank_cell_idx, num_rows, num_cols):
   if blank_cell_idx >= (num_rows - 1) * num_cols:
      return blank_cell_idx
   board[blank_cell_idx + num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx + num_cols]
   return blank_cell_idx + num_cols


def CreateBoard(num_rows, num_cols, num_cells):
   board = []
   for i in range(num_cells): board.append(i)

   blank_cell_idx = num_cells - 1
   board[blank_cell_idx] = -1
   for i in range(cfg.random):

      direction = random.randint(0, 3)
      if direction == 0:
         blank_cell_idx = moveL(board, blank_cell_idx, num_cols)
      elif direction == 1:
         blank_cell_idx = moveR(board, blank_cell_idx, num_cols)
      elif direction == 2:
         blank_cell_idx = moveU(board, blank_cell_idx, num_rows, num_cols)
      elif direction == 3:
         blank_cell_idx = moveD(board, blank_cell_idx, num_cols)
   return board, blank_cell_idx


def GetImagePath(rootdir):
   imagenames = os.listdir(rootdir)
   assert len(imagenames) > 0
   return os.path.join(rootdir, random.choice(imagenames))


def ShowEndInterface(screen, width, height):
   pygame.mixer.init()
   pygame.mixer.music.load(cfg.marshallah_song)
   pygame.mixer.music.play(1)
   screen.fill(cfg.background_colour)
   font = pygame.font.Font(cfg.fontpath, width // 15)
   title = font.render('Mashallah brother!, You won', True, (233, 150, 122))
   content = font.render('Do you want to play again?', True, (0,255,0))
   content2 = font.render('Press R restart or click X', True, (0,0, 255))
   rect3 = content2.get_rect()
   rect3.midtop = (width/2, height/2)
   rect2 = content.get_rect()
   rect2.midleft = (width / 6, height / 2.5)
   screen.blit(content,rect2)
   screen.blit(content2,rect3)
   rect = title.get_rect()
   rect.midtop = (width / 2, height / 4)
   screen.blit(title, rect)
   pygame.display.update()
   while True:
      for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
         elif event.type == pygame.KEYDOWN:
            if event.key == ord('r'):
               main()
      pygame.display.update()



def ShowStartInterface(screen, width, height):
   pygame.mixer.init() # This is when the game starts and plays a nasheed background
   pygame.mixer.music.load(cfg.victory_nasheed)
   pygame.mixer.music.play(-1)

   screen.fill(cfg.background_colour)
   tfont = pygame.font.Font(cfg.fontpath, width // 10)
   cfont = pygame.font.Font(cfg.fontpath, width // 20)
   title = tfont.render('Islamic Puzzle', True, cfg.red_colour)
   content1 = cfont.render("Press H, M or L to choose your puzzle", True, cfg.blue_colour)
   content2 = cfont.render('H - 5x5, M - 4x4, L - 3x3', True, cfg.blue_colour)
   trect = title.get_rect()
   trect.midtop = (width / 2, height / 10)
   crect1 = content1.get_rect()
   crect1.midtop = (width / 2, height / 2.2)
   crect2 = content2.get_rect()
   crect2.midtop = (width / 2, height / 1.8)
   screen.blit(title, trect)
   screen.blit(content1, crect1)
   screen.blit(content2, crect2)
   while True:
      for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
         elif event.type == pygame.KEYDOWN:
            if event.key == ord('l'):
               return 3
            elif event.key == ord('m'):
               return 4
            elif event.key == ord('h'):
               return 5
      pygame.display.update()

def main():
   pygame.init()
   clock = pygame.time.Clock()
   game_img_used = pygame.image.load(GetImagePath(cfg.picture_root_dir))
   game_img_used = pygame.transform.scale(game_img_used, cfg.screenzize)
   game_img_used_rect = game_img_used.get_rect()

   screen = pygame.display.set_mode(cfg.screenzize) #MADE A REZIABLE SCREEN TO IT
   pygame.display.set_caption('Islamic Puzzle')
   size = ShowStartInterface(screen, game_img_used_rect.width, game_img_used_rect.height)
   assert isinstance(size, int)
   num_rows, num_cols = size, size
   num_cells = size * size
   cell_width = game_img_used_rect.width // num_cols
   cell_height = game_img_used_rect.height // num_rows

   while True:
      pygame.event.pump()
      event = pygame.event.wait()
      if event.type == QUIT:
         pygame.display.quit()
      game_board, blank_cell_idx = CreateBoard(num_rows, num_cols, num_cells)
      if not isGameOver(game_board, size):
         break

   is_running = True
   while is_running:
      for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

         elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
               blank_cell_idx = moveL(game_board, blank_cell_idx, num_cols)
            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
               blank_cell_idx = moveR(game_board, blank_cell_idx, num_cols)
            elif event.key == pygame.K_UP or event.key == ord('w'):
               blank_cell_idx = moveU(game_board, blank_cell_idx, num_rows, num_cols)
            elif event.key == pygame.K_DOWN or event.key == ord('s'):
               blank_cell_idx = moveD(game_board, blank_cell_idx, num_cols)

         elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            x_pos = x // cell_width
            y_pos = y // cell_height
            idx = x_pos + y_pos * num_cols
            if idx == blank_cell_idx - 1:
               blank_cell_idx = moveR(game_board, blank_cell_idx, num_cols)
            elif idx == blank_cell_idx + 1:
               blank_cell_idx = moveL(game_board, blank_cell_idx, num_cols)
            elif idx == blank_cell_idx + num_cols:
               blank_cell_idx = moveU(game_board, blank_cell_idx, num_rows, num_cols)
            elif idx == blank_cell_idx - num_cols:
               blank_cell_idx = moveD(game_board, blank_cell_idx, num_cols)



      if isGameOver(game_board, size):
         game_board[blank_cell_idx] = num_cells - 1
         is_running = False

      screen.fill(cfg.background_colour)
      for i in range(num_cells):
         if game_board[i] == -1:
            continue
         x_pos = i // num_cols
         y_pos = i % num_cols
         rect = pygame.Rect(y_pos * cell_width, x_pos * cell_height, cell_width, cell_height)
         img_area = pygame.Rect((game_board[i] % num_cols) * cell_width, (game_board[i] // num_cols) * cell_height,
                                cell_width, cell_height)
         screen.blit(game_img_used, rect, img_area)

      for i in range(num_cols + 1):
         pygame.draw.line(screen, cfg.black_colour, (i * cell_width, 0), (i * cell_width, game_img_used_rect.height))
      for i in range(num_rows + 1):
         pygame.draw.line(screen, cfg.black_colour, (0, i * cell_height), (game_img_used_rect.width, i * cell_height))
      pygame.display.update()
      clock.tick(cfg.FPS)

   ShowEndInterface(screen, game_img_used_rect.width, game_img_used_rect.height)


if __name__ == "__main__":
   main()
