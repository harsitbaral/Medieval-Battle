import pygame
import sys
from Button import Button
from Warrior import Warrior
from Knight import Knight
from Defender import Defender
from Vampire import Vampire
from Lancer import Lancer
from Healer import Healer

pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Medieval Battle - Harsit + Dip")

BACKGROUND = pygame.image.load("assets/background.png")

WARRIOR_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/warrior_idle.png"))
WARRIOR_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/warrior_punch.png"))
KNIGHT_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/knight_idle.png"))
KNIGHT_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/knight_punch.png"))
DEFENDER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/defender_idle.png"))
DEFENDER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/defender_punch.png"))
VAMPIRE_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/vampire_idle.png"))
VAMPIRE_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/vampire_punch.png"))
LANCER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/lancer_idle.png"))
LANCER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/lancer_punch.png"))
HEALER_IDLE_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/healer_idle.png"))
HEALER_PUNCH_SPRITE = pygame.transform.scale2x(pygame.image.load("assets/healer_punch.png"))

warrior1 = Warrior("warrior", 50, 5, WARRIOR_IDLE_SPRITE, 0, 0)
knight1 = Knight("knight", 50, 7, KNIGHT_IDLE_SPRITE, 0, 0)
defender1 = Defender("defender", 60, 3, 2, DEFENDER_IDLE_SPRITE, 0, 0)
vampire1 = Vampire("vampire", 40, 4, 0.5, VAMPIRE_IDLE_SPRITE, 0, 0)
lancer1 = Lancer("lancer", 50, 6, LANCER_IDLE_SPRITE, 0, 0)
healer1 = Healer("healer", 60, 0, HEALER_IDLE_SPRITE, 0, 0)
corresponding_warriors = {"warrior": warrior1, 
                          "knight": knight1, 
                          "defender": defender1, 
                          "vampire": vampire1,
                          "lancer": lancer1,
                          "healer": healer1}

def return_font(size):
    return pygame.font.SysFont("Roboto", size)

def fight(warrior_1, warrior_2):
    warrior_1.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{warrior_1.name}_punch.png"))
    
    print(f"warrior 1 {warrior_1.name}. x: {warrior_1.x}")
    
    if warrior_1.x == 840:
        # print("thing is on the right")
        warrior_1.sprite = pygame.transform.flip(warrior_1.sprite, True, False)
        warrior_1.x = 480
    elif warrior_1.x == 440:
        warrior_1.x = 800
    else:
        print('wtf', warrior_1.x)
    
    warrior_2.set_health(warrior_2.get_health()-warrior_1.get_attack())
    warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.health}", True, "white")
    warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.health}", True, "white")
    
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))
        SCREEN.blit(warrior_1.sprite, warrior_1.sprite.get_rect(center=(warrior_1.x, 500)))
        SCREEN.blit(warrior_2.sprite, warrior_2.sprite.get_rect(center=(warrior_2.x, 500)))
        SCREEN.blit(warrior_1_health_text, warrior_1_health_text.get_rect(center=(200, 200)))
        SCREEN.blit(warrior_2_health_text, warrior_2_health_text.get_rect(center=(700, 200)))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if warrior1.x == 480:
                    warrior1.x = 840
                elif warrior1.x == 800:
                    warrior1.x = 440
    
                if warrior_1.get_health() > 0 and warrior_2.get_health() <= 0:
                    return True
                return False
        pygame.display.update()

def choose_warriors():    
    choose_warriors_text = return_font(36).render("Please choose your warriors:", True, "black")
    choose_warriors_text_rect = choose_warriors_text.get_rect(center=(640, 100))
    
    choose_warrior_button = Button(WARRIOR_IDLE_SPRITE, (120, 200), None, return_font(40), "white", "white", "warrior")
    choose_knight_button = Button(KNIGHT_IDLE_SPRITE, (320, 200), None, return_font(40), "white", "white", "knight")
    choose_defender_button = Button(DEFENDER_IDLE_SPRITE, (520, 200), None, return_font(40), "white", "white", "defender")
    choose_vampire_button = Button(VAMPIRE_IDLE_SPRITE, (720, 200), None, return_font(40), "white", "white", "vampire")
    choose_lancer_button = Button(LANCER_IDLE_SPRITE, (920, 200), None, return_font(40), "white", "white", "lancer")
    choose_healer_button = Button(HEALER_IDLE_SPRITE, (1120, 200), None, return_font(40), "white", "white", "healer")
    
    warriors_chosen = 0
    
    choose_warriors_buttons = [choose_warrior_button, choose_knight_button, 
                               choose_defender_button, choose_vampire_button,
                               choose_lancer_button, choose_healer_button]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in choose_warriors_buttons:
                    if button.checkForInput(pygame.mouse.get_pos()):
                        if warriors_chosen == 0:
                            warrior_1 = button.warrior
                            warriors_chosen += 1
                        elif warriors_chosen == 1:
                            warrior2 = button.warrior
                            warriors_chosen += 1
                        if warriors_chosen == 2:
                            return warrior_1, warrior2
                        
        SCREEN.fill("white")
        SCREEN.blit(choose_warriors_text, choose_warriors_text_rect)
        for button in choose_warriors_buttons:
            button.update(SCREEN)
        
        pygame.display.update()

def winner_screen(winner):
    SCREEN.fill("white")
    print("winner")
    pass
    
def main_game():
    global current_turn, warrior_1_health_text, warrior_2_health_text
    
    # chosen_warrior2.sprite = pygame.transform.flip(chosen_warrior2.sprite, True, False)
    information_text = return_font(30).render("Click anywhere to start a round", True, "white")
    information_text_rect = information_text.get_rect(center=(640, 50))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if current_turn == 1:
                    if fight(chosen_warrior1, chosen_warrior2):
                        winner_screen(chosen_warrior1)
                    current_turn = 2
                elif current_turn == 2:
                    if fight(chosen_warrior2, chosen_warrior1):
                        winner_screen(chosen_warrior2, chosen_warrior1)
                    current_turn = 1
                    
        SCREEN.blit(BACKGROUND, (0, 0))
        
        # print(chosen_warrior1.x)
        chosen_warrior1.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{chosen_warrior1.name}_idle.png"))
        chosen_warrior2.sprite = pygame.transform.scale2x(pygame.image.load(f"assets/{chosen_warrior2.name}_idle.png"))
        chosen_warrior2.sprite = pygame.transform.flip(chosen_warrior2.sprite, True, False)
        chosen_warrior1.x = 440
        chosen_warrior2.x = 840
        SCREEN.blit(warrior_1_health_text, warrior_1_health_text.get_rect(center=(200, 200)))
        SCREEN.blit(warrior_2_health_text, warrior_2_health_text.get_rect(center=(700, 200)))
        warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.health}", True, "white")
        warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.health}", True, "white")
        SCREEN.blit(chosen_warrior1.sprite, chosen_warrior1.sprite.get_rect(center=(chosen_warrior1.x, 500)))
        SCREEN.blit(chosen_warrior2.sprite, chosen_warrior2.sprite.get_rect(center=(chosen_warrior2.x, 500)))
        SCREEN.blit(information_text, information_text_rect)
        
        pygame.display.update()

chosen_warrior1, chosen_warrior2 = choose_warriors()
chosen_warrior1 = corresponding_warriors[chosen_warrior1]
chosen_warrior2 = corresponding_warriors[chosen_warrior2]

chosen_warrior1.x = 440
chosen_warrior2.x = 840

warrior_1_health_text = return_font(32).render(f"Warrior 1 Health: {chosen_warrior1.health}", True, "white")
warrior_2_health_text = return_font(32).render(f"Warrior 2 Health: {chosen_warrior2.health}", True, "white")

current_turn = 1
    
main_game()