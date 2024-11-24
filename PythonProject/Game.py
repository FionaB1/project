import pygame
import os
import random
pygame.font.init()
pygame.mixer.init()


WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Funky Game")

CAVEMEN = pygame.transform.scale(pygame.image.load(os.path.join("images", "cavemen.png")), (1000, 500))
EGYPT = pygame.transform.scale(pygame.image.load(os.path.join("images", "egypt.png")), (1000, 500))
GREEK = pygame.transform.scale(pygame.image.load(os.path.join("images", "greek.png")), (1000, 500))
MEDIVAL = pygame.transform.scale(pygame.image.load(os.path.join("images", "medival.png")), (1000, 500))
MODERN = pygame.transform.scale(pygame.image.load(os.path.join("images", "modern.png")), (1000, 500))
FUTURE1 = pygame.transform.scale(pygame.image.load(os.path.join("images", "future1.png")), (1000, 500))
FUTURE2 = pygame.transform.scale(pygame.image.load(os.path.join("images", "future2.png")), (1000, 500))

DOTTED_CIRCLE = pygame.transform.scale(pygame.image.load(os.path.join("images", "dottedCircle.png")), (200, 100))
ARROW = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join("images", "arrow.png")), (100,100)),0,1)
ARROW_RECT = ARROW.get_rect()
ARROW2 = pygame.transform.flip(ARROW, 1, 0)
ARROW2_RECT = ARROW2.get_rect()
MAN = pygame.transform.scale(pygame.image.load(os.path.join("images", "man.png")), (100, 100))

CAVEMEN_NORMAL = pygame.image.load(os.path.join("images", "caveman1.png"))
CAVEMEN_NORMAL = pygame.transform.scale(CAVEMEN_NORMAL, (90, 120))
CAVEMEN_FIGHT = pygame.image.load(os.path.join("images", "caveman2.png"))
CAVEMEN_FIGHT = pygame.transform.scale(CAVEMEN_FIGHT, (90, 120))
EGYPTIAN_NORMAL = pygame.image.load(os.path.join("images", "egyptian1.png"))
EGYPTIAN_NORMAL = pygame.transform.scale(EGYPTIAN_NORMAL, (90, 120))
EGYPTIAN_FIGHT = pygame.image.load(os.path.join("images", "egyptian2.png"))
EGYPTIAN_FIGHT = pygame.transform.scale(EGYPTIAN_FIGHT, (90, 120))
FUTURE_CHARACTER = pygame.image.load(os.path.join("images", "future1.1.png"))
FUTURE_CHARACTER = pygame.transform.scale(FUTURE_CHARACTER, (90, 120))
FUTURE2_CHARACTER = pygame.image.load(os.path.join("images", "future2.1.png"))
FUTURE2_CHARACTER = pygame.transform.scale(FUTURE2_CHARACTER, (90, 120))
GREEK_NORMAL = pygame.image.load(os.path.join("images", "greek1.png"))
GREEK_NORMAL = pygame.transform.scale(GREEK_NORMAL, (90, 120))
GREEK_FIGHT = pygame.image.load(os.path.join("images", "greek2.png"))
GREEK_FIGHT = pygame.transform.scale(GREEK_FIGHT, (90, 120))
MEDIVAL_NORMAL = pygame.image.load(os.path.join("images", "medival1.png"))
MEDIVAL_NORMAL = pygame.transform.scale(MEDIVAL_NORMAL, (90, 120))
MEDIVAL_FIGHT = pygame.image.load(os.path.join("images", "medival2.png"))
MEDIVAL_FIGHT = pygame.transform.scale(MEDIVAL_FIGHT, (90, 120))
MODERN_NORMAL = pygame.image.load(os.path.join("images", "modern1.png"))
MODERN_NORMAL = pygame.transform.scale(MODERN_NORMAL, (90, 120))
MODERN_FIGHT = pygame.image.load(os.path.join("images", "modern2.png"))
MODERN_FIGHT = pygame.transform.scale(MODERN_FIGHT, (90, 120))
FINAL1 = pygame.image.load(os.path.join("images", "final1.png"))
FINAL1 = pygame.transform.scale(FINAL1, (90, 120))
FINAL2 = pygame.image.load(os.path.join("images", "final2.png"))
FINAL2 = pygame.transform.scale(FINAL2, (90, 120))

FPS = 60
VEL = 2

START_FONT = pygame.font.SysFont('pressstart2p', 100)
TEXT_FONT = pygame.font.SysFont('pressstart2p', 30)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 155, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)

clock = pygame.time.Clock()
EVENT_TIMER = pygame.USEREVENT

def main():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()  # When space is pressed, start the game
                    print("space")
        start_page()  # Show the start screen

def start_page():
    WIN.fill(YELLOW)
    line = START_FONT.render("PRESS SPACE TO START", 1, BLACK)
    line2 = TEXT_FONT.render("Use ASD to move character (on left)", 1, BLACK)
    line3 = TEXT_FONT.render("Use JKL to move arrow (on right)", 1, BLACK)
    WIN.blit(line, (WIDTH//2 - line.get_width()//2, HEIGHT//2-line.get_height()//2))
    WIN.blit(line2, (10,10))
    WIN.blit(line3, (10, 30))
    pygame.display.update()

def game():
    level = 1
    arrow = 0
    position = 1
    target = random.randint(1,3)
    pos2 = 1
    bossLevel = level + 1
    health = level+3
    bossHealth = bossLevel+3
    pygame.time.set_timer(EVENT_TIMER, 3000//level)
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False  # Exit game loop if the window is closed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow quitting the game with ESC
                    game_running = False  # Exit game loop if ESC is pressed
                elif event.key == pygame.K_j:
                    arrow = 1
                elif event.key == pygame.K_k:
                    arrow = 2
                elif event.key == pygame.K_l:
                    arrow = 3
                elif event.key == pygame.K_a:
                    position = 1
                elif event.key == pygame.K_s:
                    position = 2
                elif event.key == pygame.K_d:
                    position = 3
            if event.type == EVENT_TIMER:
                pos2 = random.randint(1,3)
                target = random.randint(1,3)
            if position == target:
                print(health)
                health-=1
                print(health)
            if arrow == pos2:
                bossHealth-=1
            if health == 0:
                health = level+3
                bossHealth = bossLevel+1
            if bossHealth == 0:
                level+=1
                bossLevel+=1
                health = level + 3
                bossHealth = bossLevel + 1
        draw_window(level, arrow, position, pos2, target, health, bossLevel, bossHealth)  # Draw the game window continuously

def draw_window(level, arrow, position, pos2, target, health, bossLevel, bossHealth):
    level_char = CAVEMEN_NORMAL
    boss_char = CAVEMEN_NORMAL
    if level == 1:
        WIN.blit(CAVEMEN,(0,0))
        level_char = CAVEMEN_NORMAL
        boss_char = EGYPTIAN_FIGHT
    elif level == 2:
        WIN.blit(EGYPT,(0,0))
        level_char = EGYPTIAN_NORMAL
        boss_char = GREEK_NORMAL
    elif level == 3:
        WIN.blit(GREEK,(0,0))
        level_char = GREEK_NORMAL
        boss_char = MEDIVAL_NORMAL
    elif level == 4:
        WIN.blit(MEDIVAL,(0,0))
        level_char = MEDIVAL_NORMAL
        boss_char = MODERN_NORMAL
    elif level == 5:
        WIN.blit(MODERN,(0,0))
        level_char = MODERN_NORMAL
        boss_char = FUTURE_CHARACTER
    elif level == 6:
        WIN.blit(FUTURE1,(0,0))
        level_char = FUTURE_CHARACTER
        boss_char = FUTURE2_CHARACTER
    elif level == 7:
        WIN.blit(FUTURE2,(0,0))
        level_char = FUTURE2_CHARACTER
        boss_char = FINAL1
    elif level == 8:
        WIN.fill(BLACK)
        position = 4
        pos2 = 4
        arrow = 4
        target = 4
    if level<8:
        WIN.blit(DOTTED_CIRCLE, (10, 350))
        WIN.blit(DOTTED_CIRCLE, (120, 350))
        WIN.blit(DOTTED_CIRCLE, (230, 350))
        WIN.blit(DOTTED_CIRCLE, (550, 350))
        WIN.blit(DOTTED_CIRCLE, (660, 350))
        WIN.blit(DOTTED_CIRCLE, (770, 350))
        if position == 1:
            WIN.blit(level_char, (60, 300))
        if position == 2:
            WIN.blit(level_char, (170, 300))
        if position == 3:
            WIN.blit(level_char, (280, 300))
        elif position == 4:
            WIN.blit(level_char, (600, 1200))
        if pos2 == 1:
            WIN.blit(boss_char, (600, 300))
        elif pos2 == 2:
            WIN.blit(boss_char, (710, 300))
        elif pos2 == 3:
            WIN.blit(boss_char, (820, 300))
        elif pos2 == 4:
            WIN.blit(boss_char, (2000, 3000))
        if arrow == 1:
            arrowThrow1()
        elif arrow == 2:
            arrowThrow2()
        elif arrow == 3:
            arrowThrow3()
        elif arrow == 4:
            WIN.blit(ARROW, (2000, 2000))
        if target == 1:
            arrow2Throw1()
        elif target == 2:
            arrow2Throw2()
        elif target == 3:
            arrow2Throw3()
        elif target == 4:
            WIN.blit(ARROW2, (2300, 2700))
        temp = 400*(health/(level+3))
        temp2 = 400 * (bossHealth / (level + 3))
        healthBar1 = pygame.Rect(20,20,temp, 20)
        pygame.draw.rect(WIN, YELLOW, healthBar1)
        healthBar2 = pygame.Rect(520, 20, temp2, 20)
        pygame.draw.rect(WIN, YELLOW, healthBar2)
    else:
        line = START_FONT.render("Humanity is it's own", 1, WHITE)
        WIN.blit(line, (WIDTH // 2 - line.get_width() // 2, 80))
        line2 = START_FONT.render("greatest enemy and the", 1, WHITE)
        WIN.blit(line2, (WIDTH // 2 - line2.get_width() // 2, 150))
        line3 = START_FONT.render("cause of its own", 1, WHITE)
        WIN.blit(line3, (WIDTH // 2 - line3.get_width() // 2, 220))
        line4 = START_FONT.render("destruction.", 1, WHITE)
        WIN.blit(line4, (WIDTH // 2 - line4.get_width() // 2, 290))

    pygame.display.update()

def arrow2Throw1():

    WIN.blit(ARROW2, (60, 270))

def arrow2Throw2():
    WIN.blit(ARROW2, (170, 270))

def arrow2Throw3():
    WIN.blit(ARROW2, (280, 270))

def arrowThrow1():
    WIN.blit(ARROW, (530, 270))

def arrowThrow2():
    WIN.blit(ARROW, (640, 270))

def arrowThrow3():
    WIN.blit(ARROW, (750, 270))

# Run the game
main()

# Quit Pygame
pygame.quit()