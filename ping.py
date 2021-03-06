from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,Player_speed,width,height):
        super().__init__()
        self.image =  transform.scale(image.load(player_image),(width,height))
        self.speed = Player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys= key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys= key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

game = True
finish = False
width = 600
height = 500
window = display.set_mode((width,height))
back = (200,250,250)
window.fill(back)

speed_x = 3
speed_y = 3

clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont(None, 70)
lose_1 = font1.render("YOU 1 LOSE!!!",1,(255,0,0))
lose_2 = font1.render("YOU 2 LOSE!!!",1,(255,0,0))

pin = GameSprite("ball.png",200,200,4,50,50)
rack_1 = Player("fon.jpg",30,200,4,30,150)
rack_2 = Player("fon.jpg",520,200,4,30,150)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        rack_1.update_l()
        rack_2.update_r()
        
        pin.rect.x += speed_x
        pin.rect.y += speed_y

        pin.reset()
        rack_1.reset()
        rack_2.reset()
        if sprite.collide_rect(rack_1, pin) or sprite.collide_rect(rack_2, pin):
            speed_x *= -1
        if pin.rect.y > 450 or pin.rect.y < 0:
            speed_y *= -1
        if pin.rect.x > 600:
            window.blit(lose_2,(180,20))
        if pin.rect.x < 0:
            window.blit(lose_1,(180,200))
    display.update()
    clock.tick(FPS)