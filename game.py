from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 4:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 4:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 60:
            self.rect.y += self.speed

background = (200,200,200)
win_width = 700
win_height = 600
window = display.set_mode((win_width, win_height))
window.fill(background)
FPS = 60
clock = time.Clock()
game = True
finish = False
player_left = Player("Player.png", 0, 600, 920, 512, 4) 
player_right = Player("Player2.png", 650, 1200, 1000, 555, 4)
ball = GameSprite("minecraftball.png", 630, 800, 1000, 468, 4)
font.init()
font = font.SysFont("Arial", 40)
lose_left = font.render("1 Игрок Проиграл!", True, (200, 2, 0))
lose_right = font.render("2 Игрок Проиграл!", True, (200, 2, 0))
speed_x = 4
speed_y = 4

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if not finish:
        window.fill(background)
        player_left.update_left()
        player_right.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_x *= 1
            speed_y *= -1
        if ball.rect.x < -50:
            finish = True
            window.blit(lose_left, (200, 200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_right, (200,200))

        player_left.reset()
        player_right.reset()
        ball.reset()
    clock.tick(FPS)
    display.update()
    