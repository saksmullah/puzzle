import os
import sys
import cfg2
import random #/ to choose our picture randomly in the puzzle game
import pygame



def is_game_over(board, size):
   if not isinstance(size, int):  #check if the game size is the right type
      return True
   num_cells = size * size #multiplying the vertical to the horizontal size to get total number of cells
   for i in range(num_cells - 1):
      if board[i] != i: False #this checks if the cell and the board is not equal to the actual cell, it should be false
   return True #if every cell was in the right place, it should return True


 #what this function moveRigt on the bottom do that the piece from the left, moves to the right and the left
# one is empty
def moveRight(board, blank_cell_index, num_of_coloums):
   if blank_cell_index % num_of_coloums == 0:#when you divide blank cell index to the number of colums,
      # your not getting anything left, then you return true
      return blank_cell_index
   board[blank_cell_index-1] = board[blank_cell_index]
   board[blank_cell_index] = board[blank_cell_index-1]
   return blank_cell_index - 1

def moveLeft(board, blank_cell_index, num_of_coloums):
   if (blank_cell_index +1) % num_of_coloums == 0:
      return blank_cell_index
   board[blank_cell_index + 1] = board[blank_cell_index]
   board[blank_cell_index] = board[blank_cell_index+1]
   return blank_cell_index + 1

def moveDown(board, blank_cell_index, num_of_coloums):
   if blank_cell_index < num_of_coloums: #checking if the blank cell index is smaller then the number of coloums
      return blank_cell_index
   board[blank_cell_index - num_of_coloums] = board[blank_cell_index]
   board[blank_cell_index] = board[blank_cell_index - num_of_coloums]
   return blank_cell_index - num_of_coloums


def moveUp(board, blank_cell_index, num_rows, num_of_coloums):
   if blank_cell_index >= (num_rows - 1) * num_of_coloums:
      return blank_cell_index
   board[blank_cell_index + num_of_coloums] = board[blank_cell_index]
   board[blank_cell_index] = board[blank_cell_index + num_of_coloums]
   return blank_cell_index + num_of_coloums

def createboard(number_of_rows, number_of_coloums, number_of_cells):
   board = []

   for i in range(number_of_cells): board.append(i)

   blank_cell_index = number_of_cells - 1
   board[blank_cell_index] = -1

   for i in range(cfg2.random):#this is the file made from the cfg file and random is 100 as our range
      direction = random.randint(0, 3)

      if direction == 0: blank_cell_index = moveLeft(board, blank_cell_index, number_of_coloums)
      elif direction == 1: blank_cell_index = moveRight(board,blank_cell_index, number_of_coloums)
      elif direction == 2: blank_cell_index = moveUp(board,blank_cell_index,number_of_rows, number_of_coloums)
      elif direction == 3: blank_cell_index = moveDown(board, blank_cell_index, number_of_coloums)

   return board, blank_cell_index

def get_images_path(rootdir):
   image_names = os.listdir(rootdir)
   assert len(image_names) > 0
   return os.path.join(rootdir, random.choice(image_names))


def show_interface(screen, width, height):
   screen.fill(cfg2.background_colour)
   font = pygame.font.Font(cfg2.fontpath, width/15)
   title = font.render('good job! you won!', True, (233, 150, 122))
   rect = title.get_rect()
   rect.midtop = (width/2, height/2.5)
   screen.blit(title, rect) #to draw images to the screen
   pygame.display.update()
   while True:
      for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
      pygame.display.update()

def show_start_interface(screen, width, height):
   screen.fill(cfg2.background_colour)
   t_font = pygame.font.Font(cfg2.fontpath, width // 4)
   c_font = pygame.font.Font(cfg2.fontpath, width // 20)
   title = t_font.render('Puzzle', True, cfg2.red_colour)
   content_1 = c_font.render("Press H, M or L to choose your puzzle", True, cfg2.blue_colour)
   content_2 = c_font.render("H - 5x5, M - 4x4, L - 3x3", True, cfg2.blue_colour)
   t_rect = title.get_rect()
   t_rect.midtop = (width / 2, height / 10)
   c_rect1 = content_1.get_rect()
   c_rect1.midtop = (width / 2, height / 2.2)
   c_rect2 = content_2.get_rect()
   c_rect2.midtop = (width / 2, height / 1.8)
   screen.blit(title, t_rect)
   screen.blit(content_1, c_rect1)
   screen.blit(content_2, c_rect2)
   while True:
      for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
         elif event.type == pygame.KEYDOWN:
            if event.key == ord('L'): return 3
            elif event.key == ord('M'): return 4
            elif event.key == ord('H'): return 5
      pygame.display.update()

def main():
   pygame.mixer.init()
   pygame.mixer.music.load(cfg2.song)
   pygame.mixer.music.play(-1)
   pygame.init()
   clock = pygame.time.Clock()


   game_image_used = pygame.image.load(get_images_path(cfg2.picture_root_dir))
   game_image_used = pygame.transform.scale(game_image_used, cfg2.screenzize)
   game_image_used_rect = game_image_used.get_rect()

   screen = pygame.display.set_mode(cfg2.screenzize)
   pygame.display.set_caption('Pokemon')

   size = show_start_interface(screen, game_image_used_rect.width, game_image_used_rect.height)
   assert isinstance(size, int)
   number_rows, number_coloums = size,size
   number_cells = size * size

   cell_width = game_image_used_rect.width//number_coloums
   cell_height = game_image_used_rect.height//number_rows



   while True:
      game_board, blank_cell_index = createboard(number_rows, number_coloums, number_cells)
      if not is_game_over(game_board,size):
         break

   is_running = True


if __name__ == "__main__":
   main()

