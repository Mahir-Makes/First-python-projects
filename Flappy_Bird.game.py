import pygame
import random
pygame.init()
screen = pygame.display.set_mode((900, 1200))
b_pos = [450, 440]
b_size = [30, 30]
b_color = ((250, 250, 10))
b_flap = (0)
gravity = (0)
p_size = [50, 500]
p_color = ((10, 200, 10))
p_vel = (0)
p_pos = [0,0]
p_pos2 =[0,0]
g_pos = [0, 727]
g_size = [1300, 1500]
clock = pygame.time.Clock()
exit = False
while not exit:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                   b_flap = 40
                   p_vel =+ 10
                   gravity =+3.5
      screen.fill((10, 150, 250))
      b_rect = pygame.Rect(b_pos[0], b_pos[1], b_size[0], b_size[1])
      pipe1_rect = pygame.Rect(p_pos[0], p_pos[1], p_size[0], p_size[1])
      pipe2_rect = pygame.Rect(p_pos2[0], p_pos2[1], p_size[0], p_size[1])
      pygame.draw.rect(screen, ((10, 200, 10)), (g_pos, g_size) )
      pygame.draw.rect(screen, b_color, (b_pos, b_size))
      b_pos[1] += gravity
      b_pos[1] -= b_flap
      if b_pos[1] > 700:
            b_pos[1] = 700
            break
      if b_pos[1] < 0:
            b_pos[1] = 0
      p_pos[0] -= p_vel
      p_pos2[0] -= p_vel
      if p_pos[0]<-50 and p_pos2[0]<-40:
            p_pos[0] =+ 1200
            p_pos2[0] =+ 1200
            pos_y1 = random.randint(0,200)
            p_pos[1] = pos_y1 -230
            p_pos2[1] = pos_y1 +400
      p_vel += 0.01
      pygame.draw.rect(screen, p_color, (p_pos, p_size))
      pygame.draw.rect(screen, p_color, (p_pos2, p_size))
      if b_rect.colliderect(pipe1_rect) or b_rect.colliderect(pipe2_rect):
            break
      pygame.display.flip()
      b_flap = 0
      clock.tick(40)