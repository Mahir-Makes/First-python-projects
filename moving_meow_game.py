import pygame
import sys
pygame.init()
screen_window = pygame.display.set_mode((1000, 500))
screen_text = pygame.display.set_caption("quantum engine")
meow_img=pygame.image.load("meow.png")
radius = 100
meow_img = pygame.transform.scale(meow_img, (500, 500))
pos = [-100, 200]
exit = False
clock = pygame.time.Clock()
while not exit:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
      screen_window.fill((10, 10, 10))
      screen_window.blit(meow_img, (pos[0], pos[1]))
      clock.tick(60)
      pos[0] += 10
      if pos[0]>1500:
            pos[0] =-560
      pygame.display.flip()
pygame.quit()