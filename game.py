import random
from time import sleep
import pygame

class RacingFlames:
    def __init__(self):

        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.screen = None
        self.start()

    def start(self):

        self.bumped = False
        self.Player_Image = pygame.image.load('car1.png')
        self.PlayerX = (self.screen_width * 0.45)
        self.PlayerY = (self.screen_height * 0.8)
        self.Player_width = 60
        self.Enemy_Image = pygame.image.load('car.png')
        self.Enemy_ImageX = random.randrange(310, 450)
        self.Enemy_ImageY = -600
        self.Enemy_velocity = 5
        self.Enemy_width = 40
        self.Enemy_height = 100
        self.bg_Image = pygame.image.load("back_ground0.jpg")
        self.bg_X1 = (self.screen_width / 2) - (360 / 2)
        self.bg_X2 = (self.screen_width / 2) - (360 / 2)
        self.bg_Y1 = 0
        self.bg_Y2 = -600
        self.bg_velocity = 10
        self.count = 0

    def Player(self, PlayerX, PlayerY):
        self.screen.blit(self.Player_Image, (PlayerX, PlayerY))

    def window(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Racing flames')
        self.run()

    def run(self):

        while not self.bumped:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bumped = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.PlayerX -= 40
                    if event.key == pygame.K_RIGHT:
                        self.PlayerX += 40

            self.screen.fill(self.white)
            self.background()
            self.run_Enemy_Image(self.Enemy_ImageX, self.Enemy_ImageY)
            self.Enemy_ImageY += self.Enemy_velocity

            if self.Enemy_ImageY > self.screen_height:
                self.Enemy_ImageY = 0 - self.Enemy_height
                self.Enemy_ImageX = random.randrange(310, 450)

            self.Player(self.PlayerX, self.PlayerY)
            self.high_score(self.count)
            self.count += 0.01
            if (self.count % 100 == 0):
                self.Enemy_velocity += 1
                self.bg_velocity += 1

            if self.PlayerY < self.Enemy_ImageY + self.Enemy_height:
                if self.PlayerX > self.Enemy_ImageX and self.PlayerX < self.Enemy_ImageX + self.Enemy_width or self.PlayerX + self.Player_width > self.Enemy_ImageX and self.PlayerX + self.Player_width < self.Enemy_ImageX + self.Enemy_width:
                    self.bumped = True
                    self.gameover("GAME OVER")

            if self.PlayerX < 310 or self.PlayerX > 460:
                self.bumped = True
                self.gameover("GAME OVER")

            pygame.display.update()
            self.clock.tick(120)

    def gameover(self, msg):
        font = pygame.font.SysFont("O4B_19.TTF", 72, True)
        text = font.render(msg, True, (0,0,0))
        self.screen.blit(text, (400 - text.get_width() // 2, 340 - text.get_height() // 2))
        pygame.display.update()
        self.clock.tick(120)
        sleep(1)
        RacingFlames.start()
        RacingFlames.window()

    def background(self):
        self.screen.blit(self.bg_Image, (self.bg_X1, self.bg_Y1))
        self.screen.blit(self.bg_Image, (self.bg_X2, self.bg_Y2))

        self.bg_Y1 += self.bg_velocity
        self.bg_Y2 += self.bg_velocity

        if self.bg_Y1 >= self.screen_height:
            self.bg_Y1 = -600

        if self.bg_Y2 >= self.screen_height:
            self.bg_Y2 = -600

    def run_Enemy_Image(self, particleX, particleY):
        self.screen.blit(self.Enemy_Image, (particleX, particleY))

    def high_score(self, count):
        font = pygame.font.SysFont('O4B_19.TTF', 40)
        text = font.render("SCORE : " + str(count), True, self.black)
        self.screen.blit(text, (0, 0))


if __name__ == '__main__':
    RacingFlames = RacingFlames()
    RacingFlames.window()
