import pygame

pygame.init()

walkRight = [pygame.image.load('Walk (1).png'),pygame.image.load('Walk (2).png'),
             pygame.image.load('Walk (3).png'),pygame.image.load('Walk (4).png'),
             pygame.image.load('Walk (5).png'),pygame.image.load('Walk (6).png'),
             pygame.image.load('Walk (7).png'),pygame.image.load('Walk (8).png'),
             pygame.image.load('Walk (9).png'),pygame.image.load('Walk (10).png')]
walkLeft = [pygame.image.load('L1.png'),pygame.image.load('L2.png'),
            pygame.image.load('L3.png'),pygame.image.load('L4.png'),
            pygame.image.load('L5.png'),pygame.image.load('L6.png'),
            pygame.image.load('L7.png'),pygame.image.load('L8.png'),
            pygame.image.load('L9.png'),pygame.image.load('L10.png')]

green = (0, 255, 0)
blue = (0, 0, 255)

file_0 = 'music.wav'
pygame.mixer.init()
pygame.mixer.music.load(file_0)
pygame.mixer.music.play(-1)


win = pygame.display.set_mode((962,600))
pygame.display.set_caption("Medieval Game")

bg = pygame.image.load("oyun_arka_planim.png")
bg2 = pygame.image.load("oyun_arka_planim(2).png")  #BUNU EKLEMELİSİN
bg3 = pygame.image.load('bg_03.png')
keyy = (pygame.image.load("key.png"))
win.blit(keyy, (50,500))

clock = pygame.time.Clock()

chars = {"char": [pygame.image.load("standing2.png"),pygame.image.load("standing.png")]}
win.blit(chars["char"][1],(300,450))

pygame.display.update()



class Player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.standing = True
        self.isJump = False
        self.last_move = None
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self, win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.last_move = "left"
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                self.last_move = "right"

        else:
            if self.last_move == "left":
                win.blit(chars["char"][0], (self.x,self.y))
            elif self.last_move == "right":
                win.blit(chars["char"][1], (self.x,self.y))
            else:
                win.blit(chars["char"][1], (self.x,self.y))

def draw_3(win):
     basamak_taban = pygame.draw.rect(win, (88, 0, 0), [0, 540, 962, 60])
     basamak1 = pygame.draw.rect(win, (0,0,0),[385,465,117,75])
     basamak2 = pygame.draw.rect(win, (0, 0, 0), [494, 390, 120, 80])
     basamak3 = pygame.draw.rect(win, (0, 0, 0), [591,308,120,84])




class GameKey(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.key = True
    def draw2(self,win):
        if self.key == False:
            win.blit(keyy, (0,1000))
        else:
            win.blit(keyy, (50,500))
            #exec(open('sahne_01.py').read())
            #pygame.quit()

new_scene = False
def redrawGameWindow():
    if (new_scene == True):
        win.blit(bg3, (0,0))
        draw_3(win)
        man.draw(win)

    else:
        win.blit(bg, (0,0))
        man.draw(win)
    yellow_key.draw2(win)
    pygame.display.update()

man = Player(300, 450, 100,120)
yellow_key = GameKey(50, 450, 40, 43)


walking = True
while (walking):
    clock.tick(27)


    keys = pygame.key.get_pressed()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()


    if keys[pygame.K_LEFT] and (man.x > man.vel):
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and (man.x < 962 - man.width - man.vel):
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.left = False
        man.right = False
        man.standing = True
        man.walkCount = 0

    if (man.x == 50) and (man.y == 450):
        yellow_key.key = False
    if (man.x == 660) and (yellow_key.key == False) and (new_scene == False)  and (man.isJump == False):
        new_scene = True
        man.x = 50
        man.y = 450

        #pygame.mixer.music.stop()

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()


pygame.quit()
