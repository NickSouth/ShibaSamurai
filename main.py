# Nick Southey
# Python With Mr. Forhan
# Python Final
# Survival Game Using Pygame
# Dec. 12, 2022 - ONGOING


"""
Welcome to:
SAMURAI SHIBA

This game is dedicated to my best friend Rocky, fly high.

This game is an infinite, round-based, top-down survival game. The player controls a shiba inu samurai as he defends his
village from numerous enemies. These enemies include a quick and agile but weak ninja cat, a sly archer fox, and a slow,
heavy panda sumo wrestler.
The player can slash with their sword, throw shurikens, or use their abilities to deal damage to enemies while trying to
stay alive themself.

I will try to be specific with what each part of the code does as I write it.
"""

# Overview of code
"""
The flow of the game will be as follows:

There will be four while loops, all embedded within the overarching while loop. 
The first loop will be for the start screen.
The second loop will be for the context and controls.
The third loop will be for the gameplay.
The fourth loop will be for the game over screen.

Once the player presses "START GAME", they will move into the context and controls, which will end after a certain
amount of frames and lead into the gameplay. If the player's health dips below 0, the game over screen will show.
"""

# Importing the modules
import pygame
import sys
import random
import math


"""
Below is the setup relating to pygame, which requires some initializing before it can work.
"""
# Initializing pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP, pygame.MOUSEBUTTONDOWN])

# Setting the display size
screen = pygame.display.set_mode((1400, 800))

# Setting the clock which will cap framerate at 60
clock = pygame.time.Clock()

# Defining some colors which will be used universally
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


"""
Below are the globally used variables that must be defined at the top of the code.
"""

# Start Screen
start_screen = True
just_opened = True
button_click = False
presses = 0
start_frame_count = 0
button_color = [50, 50, 50]
start_rect = pygame.Rect(800, 600, 500, 100)
start_black = [0, 0, 0]

# Context Screen
context_screen = False
context_frame_count = 0
context_frame_count_2 = 0

# Main game loop
game_loop = False
# Handling movement
screen_scroll = [0, 0]
walking_count = 299
# Tracking wave
wave_number = 1
enemy_total = 0
start_of_wave = True
wave_startup_frames = 0
# Balancing round
panda_enemy_max = wave_number//2
panda_enemy_min = wave_number//4
fox_enemy_max = int(wave_number * 1.2)
fox_enemy_min = int(wave_number * .8)
cat_enemy_max = wave_number * 2
cat_enemy_min = wave_number
# Lists relating to player
player_shurikens = []
player_spins = []
player_attack = []
dropped_shurikens = []
player_dashes = []
dropped_hearts = []
dropped_cooldown = []
dropped_bombs = []
# Lists relating to enemies
enemy_projectiles = []
enemies = []
# List of collision spots
collision_zones = []

# Game Over Screen
game_over = False
game_over_frames = 0


"""
Importing the images that will be used throughout the code.
"""
# Start Screen
start_image = pygame.image.load("Sprites/SamuraiShibaTitleScreen.png").convert()
# Game Loop

# Map
game_map = pygame.image.load("Sprites/BackgroundOfShibaSamurai.png").convert()
background = pygame.transform.scale(game_map, (5000, 2500))
scroll = pygame.transform.scale(pygame.image.load("Sprites/scroll.png").convert_alpha(), (500, 370))
round_scroll = pygame.transform.scale(scroll, (300, 80))


# Player
player_idle_images = [pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_3.png").convert_alpha()]
player_walking_right_images = [pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_7.png").convert_alpha()]
player_walking_left_images = [pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+7.png").convert_alpha()]

# Player abilities
right_sword_slash_images = [pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_5.png").convert_alpha()]
left_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_5.png").convert_alpha()]
down_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_5.png").convert_alpha()]
up_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_5.png").convert_alpha()]
shuriken_images = [pygame.image.load("Sprites/Sprites/Shuriken/shuriken_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Shuriken/shuriken_1.png").convert_alpha()]
spin_images = [pygame.image.load("Sprites/Sprites/Spin Attack/spin_00.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_01.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_02.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_03.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_04.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_05.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_06.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_07.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_08.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_09.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_10.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_11.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_12.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_13.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_14.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_15.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_16.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_17.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_18.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_19.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_20.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_21.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Spin Attack/spin_22.png").convert_alpha()]
dash_images = [pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_7.png").convert_alpha()]
player_damage = pygame.image.load("Sprites/Sprites/player_damage_0.png").convert_alpha()

# Enemies
archer_fox_right_images = [pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_7.png").convert_alpha()]
archer_fox_left_images = [pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_7.png").convert_alpha()]
archer_fox_arrow = [pygame.image.load("Sprites/Sprites/Arrow/arrow_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Arrow/arrow_1.png").convert_alpha()]
ninja_cat_right_images = [pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_2.png").convert_alpha()]
ninja_cat_left_images = [pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_2.png").convert_alpha()]
panda_enemy_right_images = [pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_7.png").convert_alpha()]
panda_enemy_left_images = [pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_2.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_3.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_4.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_5.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_6.png").convert_alpha(), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_7.png").convert_alpha()]
archer_fox_arrow_left = pygame.image.load("Sprites/Sprites/arrow_left.png").convert_alpha()
enemy_death_images = [pygame.image.load("Sprites/Sprites/enemy_death/enemy_death_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/enemy_death/enemy_death_1.png").convert_alpha(), pygame.image.load("Sprites/Sprites/enemy_death/enemy_death_2.png").convert_alpha()]

# Pickups
heart_pickup_images = [pygame.image.load("Sprites/Sprites/heart_pickup/heart_pickup_0.png").convert_alpha(), pygame.image.load("Sprites/Sprites/heart_pickup/heart_pickup_1.png").convert_alpha()]
cooldown_pickup_image = pygame.image.load("Sprites/Sprites/cooldown_pickup_0.png").convert_alpha()
bomb_pickup_image = pygame.image.load("Sprites/Sprites/bomb_pickup_0.png").convert_alpha()

"""
Importing all the sounds that will be used throughout the game
"""
pygame.mixer.music.load("Sounds/intro_music.wav")
pygame.mixer.music.play(-1)
ability_recharge = pygame.mixer.Sound("Sounds/ability_recharge.wav")
arrow_shot = pygame.mixer.Sound("Sounds/arrow_shot.wav")
bomb = pygame.mixer.Sound("Sounds/bomb.wav")
enemy_death = pygame.mixer.Sound("Sounds/enemy_death.wav")
game_over_sound = pygame.mixer.Sound("Sounds/game_over.wav")
heal = pygame.mixer.Sound("Sounds/heal.wav")
spin_sound = pygame.mixer.Sound("Sounds/hurricane.wav")
hurt_sound = pygame.mixer.Sound("Sounds/player_damage.wav")
round_start_sound = pygame.mixer.Sound("Sounds/round_start.wav")
shuriken_sound = pygame.mixer.Sound("Sounds/shuriken.wav")
smoke_bomb_sound = pygame.mixer.Sound("Sounds/smoke_bomb.wav")
sword_slash_sound = pygame.mixer.Sound("Sounds/sword_slash.wav")
walking_sound = pygame.mixer.Sound("Sounds/walking.wav")
pygame.mixer.Sound.play(walking_sound, -1)
pygame.mixer.Sound.set_volume(walking_sound, 0)
gong_start = pygame.mixer.Sound("Sounds/gong.wav")
shuriken_pickup = pygame.mixer.Sound("Sounds/shuriken_pickup.wav")

"""
Importing font that will be used throughout the game.
"""
# Start Screen
intro_font = pygame.font.SysFont("Ariel", 20)
startup_text = intro_font.render("In loving memory of Rocky...", True, WHITE)
start_font = pygame.font.Font("japanese.ttf", 80)
start_text = start_font.render("START GAME", True, (200, 200, 200))

# Context Screen
context_font = pygame.font.SysFont("Ariel", 25)
context_font_2 = pygame.font.SysFont("Ariel", 40)
context_text_1 = context_font_2.render("Welcome to SAMURAI SHIBA!", True, WHITE)
context_text_2 = context_font.render("You, Rocky, were minding your own business as a shiba inu samurai when your village was attacked.", True, WHITE)
context_text_3 = context_font.render("Now you're left defending.", True, WHITE)
context_text_4 = context_font.render("Press on your mouse to swing your sword.", True, WHITE)
context_text_5 = context_font.render("Press Q to throw your shurikens.", True, WHITE)
context_text_6 = context_font.render("Press E to heal.", True, WHITE)
context_text_7 = context_font.render("Press R to confuse enemies with a smoke bomb and make a getaway.", True, WHITE)
context_text_8 = context_font.render("Press F to spin into a damaging whirlwind.", True, WHITE)
context_text_9 = context_font.render("Click anywhere to start!", True, WHITE)

# Game Loop
round_intro_font = pygame.font.Font("japanese.ttf", 40)
round_intro_text = round_intro_font.render("ROUND "+str(wave_number), True, BLACK)
round_font = pygame.font.Font("japanese.ttf", 16)
round_text = round_font.render("Round", True, BLACK)
round_number_font = pygame.font.Font("japanese.ttf", 35)
round_number_text = round_number_font.render(str(wave_number), True, BLACK)
enemies_left_text = round_font.render("Enemies left:"+str(len(enemies)), True, BLACK)

# Game Over Screen
game_over_font = pygame.font.SysFont("Ariel", 100)
game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))


"""
Below are the classes that handle everything in the main game loop.
"""


# The player class and all of its subclasses
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = 40
        self.health = 40
        self.last_health = 40
        self.immunity = 20
        self.damage_frame = 0
        # Main attack
        self.is_slashing = False
        self.slash_counter = 0
        # Shuriken ability
        self.can_throw = True
        self.is_throwing = False
        self.shuriken_count = 5
        # Dash ability
        self.is_dashing = False
        self.dash_distance = 100
        self.dashing_cooldown = 3600
        self.can_dash = True
        # Spin ability
        self.is_spinning = False
        self.spin_cooldown = 4000
        self.can_spin = True
        # Healing ability
        self.healing_factor = 10
        self.healing_cooldown = 600
        self.can_heal = True
        # Animation
        self.walking_right = False
        self.walking_left = False
        self.walking_up = False
        self.walking_down = False
        self.walking_animation = 0
        self.not_moving = False
        self.idle_animation = 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, 70, 100)
        return bounds

    # Healing method
    def healing(self):
        if self.can_heal:
            self.health += self.healing_factor
            if self.health > 40:
                self.health = 40
            self.can_heal = False
            self.healing_cooldown = 0

    # Dashing method
    def dashing(self):
        if self.can_dash:
            self.is_dashing = True
            self.can_dash = False
            self.dashing_cooldown = 0
            player_dashes.append(PlayerDash(player.x, player.y))
            for foe in enemies:
                foe.x_location_goal = random.randint(0, 500)
                foe.y_location_goal = random.randint(0, 500)

    # Spinning method
    def spinning(self):
        if self.can_spin:
            player_spins.append(PlayerSpin(self.x, self.y))
            self.can_spin = False
            self.spin_cooldown = 0

    # Player main
    def main(self):
        self.idle_animation += 2
        if self.idle_animation == 40:
            self.idle_animation = 0
        self.walking_animation += 2
        if self.walking_animation == 56:
            self.walking_animation = 0

        # Updating player
        if self.health < self.last_health or self.damage_frame > 0:
            self.last_health = self.health
            self.damage_frame += 1
            if self.damage_frame == 10:
                self.damage_frame = 0
            screen.blit(player_damage, (self.x, self.y))
        else:
            self.last_health = self.health
            if self.not_moving:
                screen.blit(player_idle_images[self.idle_animation//10], (self.x, self.y))
            else:
                if self.walking_left:
                    screen.blit(player_walking_left_images[self.walking_animation//7], (self.x, self.y))
                else:
                    screen.blit(player_walking_right_images[self.walking_animation//7], (self.x, self.y))


        self.immunity += 1

        """Checking for cooldowns"""
        # Healing
        if not self.can_heal:
            self.healing_cooldown += 2
            if self.healing_cooldown >= 601:
                self.healing_cooldown = 600
        if self.healing_cooldown == 600:
            if self.health <= 39:
                self.can_heal = True

        # Dashing
        if not self.can_dash:
            self.dashing_cooldown += 2
            if self.dashing_cooldown == 3600:
                self.can_dash = True

        # Spinning
        if not self.can_spin:
            self.spin_cooldown += 2
            if self.spin_cooldown == 4000:
                self.can_spin = True

        # Shurikens
        if self.shuriken_count == 0:
            self.can_throw = False
        if self.shuriken_count > 0:
            self.can_throw = True

        if self.is_slashing:
            self.slash_counter += 1
            if self.slash_counter == 10:
                self.is_slashing = False
                self.slash_counter = 0


class PlayerAttack:
    def __init__(self, x, y, mouse_position_x, mouse_position_y):
        self.x = x
        self.y = y
        self.counter = 0
        self.mouse_x = mouse_position_x
        self.mouse_y = mouse_position_y
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.animation = 0
        if mouse_x > player.x + 50:
            self.x += 60
            self.right = True
        elif mouse_x < player.x - 50:
            self.x -= 50
            self.left = True
        else:
            self.x += 0
        if mouse_y > player.y + 50:
            self.y += 60
            self.down = True
        elif mouse_y < player.y - 50:
            self.y -= 50
            self.up = True
        else:
            self.y += 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, 150, 150)
        return bounds

    def main(self):
        if self.animation < 15:
            self.animation += 2
            if self.right:
                screen.blit(pygame.transform.scale(right_sword_slash_images[self.animation//3], (150, 150)), (self.x-50, self.y))
            elif self.left:
                screen.blit(pygame.transform.scale(left_sword_slash_images[self.animation//3], (150, 150)), (self.x, self.y))
            else:
                if self.up:
                    screen.blit(pygame.transform.scale(up_sword_slash_images[self.animation//3], (150, 150)), (self.x, self.y))
                elif self.down:
                    screen.blit(pygame.transform.scale(down_sword_slash_images[self.animation//3], (150, 150)), (self.x, self.y))


class PlayerHealthBar:
    def __init__(self):
        self.x = 10
        self.y = 770
        self.max_x = 400
        self.width = 400
        self.height = 20
        self.health_bar_color = (0, 255, 0)

    def main(self):
        self.width = player.health * 10
        if player.health > 10:
            self.health_bar_color = (0, 255, 0)
        elif player.health < 5:
            self.health_bar_color = (255, 0, 0)
        else:
            self.health_bar_color = (255, 255, 0)
        pygame.draw.rect(screen, (0, 0, 0), (self.x-2, self.y-2, self.max_x+4, self.height+4))
        pygame.draw.rect(screen, self.health_bar_color, (self.x, self.y, self.width, self.height))


class PlayerDash:
    def __init__(self, x, y):
        self.x = x + screen_scroll[0]
        self.y = y + screen_scroll[1]
        self.x_2 = x + screen_scroll[0]
        self.y_2 = y + screen_scroll[1]
        self.animation = 0

    def main(self):
        if self.animation < 98:
            self.x = self.x_2 - screen_scroll[0]
            self.y = self.y_2 - screen_scroll[1]
            self.animation += 2
            screen.blit(pygame.transform.scale(dash_images[self.animation//14], (200, 200)), (self.x-30, self.y-30))


class PlayerCooldowns:
    def __init__(self):
        self.x = 1200
        self.dash_y = 600
        self.spin_y = 650
        self.heal_y = 700
        self.width = 170
        self.height = 20
        self.shuriken_y = 530
        self.shuriken_height = 80
        self.dash_width = player.dashing_cooldown / 21.1764
        self.spin_width = player.spin_cooldown / 23.529
        self.heal_width = player.healing_cooldown / 3.529
        self.cooldown_font = pygame.font.SysFont("Ariel", 20)
        self.dash_cooldown_font = self.cooldown_font.render("Smoke Bomb (R)", True, (0, 0, 0))
        self.spin_cooldown_font = self.cooldown_font.render("Spin (F)", True, (0, 0, 0))
        self.heal_cooldown_font = self.cooldown_font.render("Heal (E)", True, (0, 0, 0))
        self.shuriken_count = str(player.shuriken_count)
        self.shuriken_count_font = pygame.font.SysFont("Ariel", 40)
        self.shuriken_count_text = self.shuriken_count_font.render(self.shuriken_count, True, (0, 0, 0))

    def main(self):
        self.dash_width = player.dashing_cooldown / 21.1764
        self.spin_width = player.spin_cooldown / 23.529
        self.heal_width = player.healing_cooldown / 3.529

        self.shuriken_count = str(player.shuriken_count)
        self.shuriken_count_text = self.shuriken_count_font.render(self.shuriken_count, True, (0, 0, 0))

        pygame.draw.rect(screen, (0, 0, 0), (self.x-2, self.dash_y-2, self.width+4, self.height+4))
        screen.blit(self.dash_cooldown_font, (self.x+15, self.dash_y-15))
        pygame.draw.rect(screen, (0, 0, 0), (self.x-2, self.spin_y-2, self.width+4, self.height+4))
        screen.blit(self.spin_cooldown_font, (self.x + 15, self.spin_y - 15))
        pygame.draw.rect(screen, (0, 0, 0), (self.x-2, self.heal_y-2, self.width+4, self.height+4))
        screen.blit(self.heal_cooldown_font, (self.x + 15, self.heal_y - 15))

        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.dash_y, self.dash_width, self.height))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.spin_y, self.spin_width, self.height))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.heal_y, self.heal_width, self.height))

        screen.blit(shuriken_images[0], (self.x + 20, self.shuriken_y))
        screen.blit(self.shuriken_count_text, (self.x + 70, self.shuriken_y + 20))


class PlayerSpin:
    def __init__(self, x, y):
        self.x = x - 100
        self.y = y - 100
        self.width = 300
        self.height = 300
        self.animation = 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, self.width, self.height)
        return bounds

    def main(self):
        if self.animation < 100:
            self.animation += 2
            screen.blit(pygame.transform.scale(spin_images[self.animation//5], (300, 300)), (self.x, self.y))


# To track throwing stars
class PlayerShuriken:
    def __init__(self, x, y, mouse_x_pos, mouse_y_pos):
        # Initializing these
        self.x = x
        self.y = y
        self.mouse_x = mouse_x_pos
        self.mouse_y = mouse_y_pos
        self.speed = 20
        self.height = 10
        self.width = 10
        self.animation = 0
        self.display = True

        # Calculating angles
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, self.width, self.height)
        return bounds

    # Main shuriken
    def main(self):
        if self.display:
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)

            self.animation += 2
            if self.animation == 20:
                self.animation = 0
            screen.blit(shuriken_images[self.animation // 10], (self.x-30, self.y-30))


# The enemies in the game

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class HeavyPandaEnemy(Enemy):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 150
        self.width = 130
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        self.x_location_goal = player.x + random.randint(-17, 17)
        self.y_location_goal = player.y + random.randint(-17, 17)
        self.location_goal_shift = 0
        self.health = 40
        self.damage = 5
        self.dead = False
        self.walking_right = False
        self.walking_left = False
        self.animation_count = 0
        self.speed = 2
        self.death_animation_count = 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x-50, self.true_y-50, self.width-50, self.height-50)
        return bounds

    # Dying method
    def die(self):
        if self.death_animation_count < 14:
            self.death_animation_count += 1
            screen.blit(pygame.transform.scale(enemy_death_images[self.death_animation_count//5], (100, 100)),
                        (self.x - screen_scroll[0], self.y - screen_scroll[1]))

    def main(self):
        self.animation_count += 2
        if self.animation_count == 80:
            self.animation_count = 0
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if self.x - screen_scroll[0] > self.x_location_goal:
            self.x -= 1
            if self.x - screen_scroll[0] > self.x_location_goal:
                self.x -= 1
            self.walking_right = False
            self.walking_left = True
        elif self.x - screen_scroll[0] < self.x_location_goal:
            self.x += 1
            if self.x - screen_scroll[0] < self.x_location_goal:
                self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 1
            if self.y - screen_scroll[1] > self.y_location_goal:
                self.y -= 1
        elif self.y - screen_scroll[1] < self.y_location_goal:
            self.y += 1
            if self.y - screen_scroll[1] < self.y_location_goal:
                self.y += 1

        self.location_goal_shift += 1
        if self.location_goal_shift == 150:
            self.location_goal_shift = 0
            self.x_location_goal = player.x + random.randint(-17, 17)
            self.y_location_goal = player.y + random.randint(-17, 17)
        if self.walking_left:
            screen.blit(pygame.transform.scale(panda_enemy_left_images[self.animation_count//10], (150, 150)), (self.true_x, self.true_y))
        else:
            screen.blit(pygame.transform.scale(panda_enemy_right_images[self.animation_count//10], (150, 150)), (self.true_x, self.true_y))


class ArcherFoxEnemy (Enemy):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        self.height = 90
        self.width = 70
        self.x_location_goal = player.x + random.randint(-100, 100)
        self.y_location_goal = player.y + random.randint(-100, 100)
        self.location_goal_shift = 0
        self.health = 10
        self.damage = 1
        self.dead = False
        self.walking_right = False
        self.walking_left = False
        self.animation_count = 0
        self.speed = 3
        self.death_animation_count = 0

        # Attack cooldowns
        self.arrow_cooldown = 0
        self.is_in_range = False

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x, self.true_y, self.width, self.height)
        return bounds

    # Attacking method
    def attack(self):
        if self.is_in_range:
            if self.arrow_cooldown == 0:
                pygame.mixer.Sound.play(arrow_shot)
                enemy_projectiles.append(ArcherFoxEnemyArrow(self.true_x, self.true_y))
                self.arrow_cooldown = 1

    # Dying method
    def die(self):
        if self.death_animation_count < 14:
            self.death_animation_count += 1
            screen.blit(enemy_death_images[self.death_animation_count//5], (self.x - screen_scroll[0], self.y - screen_scroll[1]))

    def main(self):
        self.animation_count += 2
        if self.animation_count == 80:
            self.animation_count = 0
        # Checking if enemy is in range and attacking
        if self.true_x + 100 >= player.x or self.true_x - 100 <= player.x:
            if self.true_y + 100 >= player.y or self.true_y - 100 <= player.y:
                self.is_in_range = True
        if self.true_x + 100 < player.x or self.true_x - 100 > player.x:
            if self.true_y + 100 < player.y or self.true_y - 100 > player.y:
                self.is_in_range = False
        self.attack()
        # Updating true self locations
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        # Drawing and moving
        if self.x - screen_scroll[0] > self.x_location_goal:
            self.x -= 1
            if self.x - screen_scroll[0] > self.x_location_goal:
                self.x -= 1
                if self.x - screen_scroll[0] > self.x_location_goal:
                    self.x -= 1
            self.walking_right = False
            self.walking_left = True
        elif self.x - screen_scroll[0] < self.x_location_goal:
            self.x += 1
            if self.x - screen_scroll[0] < self.x_location_goal:
                self.x += 1
                if self.x - screen_scroll[0] < self.x_location_goal:
                    self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 1
            if self.y - screen_scroll[1] > self.y_location_goal:
                self.y -= 1
        elif self.y - screen_scroll[1] < self.y_location_goal:
            self.y += 1
            if self.y - screen_scroll[1] < self.y_location_goal:
                self.y += 1
        # Attack cooldown
        if self.arrow_cooldown > 0:
            self.arrow_cooldown += 1
        if self.arrow_cooldown == 50:
            self.arrow_cooldown = 0
        # Location goal shifting
        self.location_goal_shift += 1
        if self.location_goal_shift == 200:
            self.location_goal_shift = 0
            self.x_location_goal = player.x + random.randint(-100, 100)
            self.y_location_goal = player.y + random.randint(-100, 100)
        if self.walking_left:
            screen.blit(archer_fox_left_images[self.animation_count//10], (self.true_x, self.true_y))
        else:
            screen.blit(archer_fox_right_images[self.animation_count//10], (self.true_x, self.true_y))


class ArcherFoxEnemyArrow:
    def __init__(self, x, y):
        # Initializing these
        self.x = x
        self.y = y
        aim_x = player.x
        aim_y = player.y
        self.speed = 16
        self.true_x = self.x
        self.true_y = self.y
        self.width = 10
        self.height = 10
        self.animation_count = 0
        self.flying_right = False
        self.flying_left = False
        self.display = True


        # Calculating angles
        self.angle = math.atan2(y - aim_y, x - aim_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, self.width, self.height)
        return bounds

    def main(self):
        if self.display:
            self.animation_count += 2
            if self.animation_count == 20:
                self.animation_count = 0
            self.x -= int(self.x_vel)
            if int(self.x_vel) <= 0:
                self.flying_right = True
            else:
                self.flying_left = True
            self.y -= int(self.y_vel)

            if self.flying_left:
                screen.blit(archer_fox_arrow_left, (self.x - 20, self.y - 20))
            else:
                screen.blit(archer_fox_arrow[self.animation_count//10], (self.x - 20, self.y - 20))


class NinjaCatEnemy (Enemy):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 80
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        self.x_location_goal = player.x + random.randint(-17, 17)
        self.y_location_goal = player.y + random.randint(-17, 17)
        self.location_goal_shift = 0
        self.health = 20
        self.damage = 3
        self.dead = False
        self.walking_right = False
        self.walking_left = False
        self.animation_count = 0
        self.speed = 4
        self.death_animation_count = 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x, self.true_y, self.width, self.height)
        return bounds

    # Dying method
    def die(self):
        if self.death_animation_count < 14:
            self.death_animation_count += 1
            screen.blit(enemy_death_images[self.death_animation_count//5], (self.x - screen_scroll[0], self.y - screen_scroll[1]))

    def main(self):
        self.animation_count += 2
        if self.animation_count == 30:
            self.animation_count = 0
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if self.x-screen_scroll[0] > self.x_location_goal:
            self.x -= 1
            if self.x - screen_scroll[0] > self.x_location_goal:
                self.x -= 1
                if self.x - screen_scroll[0] > self.x_location_goal:
                    self.x -= 1
                    if self.x - screen_scroll[0] > self.x_location_goal:
                        self.x -= 1
                        if self.x - screen_scroll[0] > self.x_location_goal:
                            self.x -= 1
            self.walking_right = False
            self.walking_left = True
        elif self.x-screen_scroll[0] < self.x_location_goal:
            self.x += 1
            if self.x - screen_scroll[0] < self.x_location_goal:
                self.x += 1
                if self.x - screen_scroll[0] < self.x_location_goal:
                    self.x += 1
                    if self.x - screen_scroll[0] < self.x_location_goal:
                        self.x += 1
                        if self.x - screen_scroll[0] < self.x_location_goal:
                            self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 1
            if self.y - screen_scroll[1] > self.y_location_goal:
                self.y -= 1
                if self.y - screen_scroll[1] > self.y_location_goal:
                    self.y -= 1
                    if self.y - screen_scroll[1] > self.y_location_goal:
                        self.y -= 1
        elif self.y - screen_scroll[1] < self.y_location_goal:
            self.y += 1
            if self.y - screen_scroll[1] < self.y_location_goal:
                self.y += 1
                if self.y - screen_scroll[1] < self.y_location_goal:
                    self.y += 1
                    if self.y - screen_scroll[1] < self.y_location_goal:
                        self.y += 1

        self.location_goal_shift += 1
        if self.location_goal_shift == 75:
            self.location_goal_shift = 0
            self.x_location_goal = player.x + random.randint(-17, 17)
            self.y_location_goal = player.y + random.randint(-17, 17)
        if self.walking_left:
            screen.blit(ninja_cat_left_images[self.animation_count//10], (self.true_x, self.true_y))
        else:
            screen.blit(ninja_cat_right_images[self.animation_count//10], (self.true_x, self.true_y))


# The drops of the game
class ShurikenDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]

    def get_bounds(self):
        bounds = (self.true_x, self.true_y, 40, 40)
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if not self.picked_up:
            screen.blit(shuriken_images[0], (self.true_x, self.true_y))


class HeartDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        self.animation_count = 0

    def get_bounds(self):
        bounds = (self.true_x, self.true_y, 40, 40)
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if not self.picked_up:
            self.animation_count += 1
            if self.animation_count == 10:
                self.animation_count = 0
            screen.blit(heart_pickup_images[self.animation_count//5], (self.true_x, self.true_y))


class CooldownDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]

    def get_bounds(self):
        bounds = (self.true_x, self.true_y, 40, 40)
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if not self.picked_up:
            screen.blit(cooldown_pickup_image, (self.true_x, self.true_y))


class BombDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]

    def get_bounds(self):
        bounds = (self.true_x, self.true_y, 40, 40)
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if not self.picked_up:
            screen.blit(bomb_pickup_image, (self.true_x, self.true_y))


# The collision detection boxes of the game
class CollisionBoxes:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.true_x = x - screen_scroll[0]
        self.true_y = y - screen_scroll[1]
        self.color = (0, 0, 0)

        self.left_bounds = (self.true_x - 5, self.true_y, 5, self.height)
        self.right_bounds = (self.true_x + self.width, self.true_y, 5, self.height)
        self.top_bounds = (self.true_x, self.true_y - 5, self.width, 5)
        self.bottom_bounds = (self.true_x, self.true_y + self.height, self.width, 5)

        self.left_side = self.true_x - 50
        self.right_side = self.true_x + self.width + 50
        self.top_side = self.true_y - 50
        self.bottom_side = self.true_y + self.height + 50

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x, self.true_y, self.width, self.height)
        return bounds

    # Getting hit box
    def get_bounds_1(self):
        bounds = self.left_bounds
        return bounds

    # Getting hit box
    def get_bounds_2(self):
        bounds = self.right_bounds
        return bounds

    # Getting hit box
    def get_bounds_3(self):
        bounds = self.top_bounds
        return bounds

    def get_bounds_4(self):
        bounds = self.bottom_bounds
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]

        self.left_side = self.true_x - 100
        self.right_side = self.true_x + self.width + 100
        self.top_side = self.true_y - 100
        self.bottom_side = self.true_y + self.height + 100

        self.left_bounds = (self.true_x - 5, self.true_y, 5, self.height)
        self.right_bounds = (self.true_x + self.width, self.true_y, 5, self.height)
        self.top_bounds = (self.true_x, self.true_y - 5, self.width, 5)
        self.bottom_bounds = (self.true_x, self.true_y + self.height, self.width, 5)
        pygame.draw.rect(screen, self.color, (self.true_x - 5, self.true_y, 5, self.height))
        pygame.draw.rect(screen, self.color, (self.true_x + self.width, self.true_y, 5, self.height))
        pygame.draw.rect(screen, self.color, (self.true_x, self.true_y - 5, self.width, 5))
        pygame.draw.rect(screen, self.color, (self.true_x, self.true_y + self.height, self.width, 5))


# Creating the player
player = Player(684, 380, 32, 40)
player_health_bar = PlayerHealthBar()
player_cooldown_bars = PlayerCooldowns()

# Creating collision zones
""" This is where the collision boxes will go """
block1 = CollisionBoxes(-749, -116, 100, 100)
block2 = CollisionBoxes(-555, 258, 200, 200)
block3 = CollisionBoxes(-293, 152, 100, 100)
block4 = CollisionBoxes(-341, -84, 200, 200)
block5 = CollisionBoxes(-364, 592, 200, 200)
block6 = CollisionBoxes(-672, 870, 200, 200)
block7 = CollisionBoxes(-381, 858, 150, 150)
block8 = CollisionBoxes(-1, 811, 250, 200)
block9 = CollisionBoxes(1432, 905, 115, 115)
block10 = CollisionBoxes(2125, 807, 115, 115)
block11 = CollisionBoxes(1974, 167, 100, 100)
block12 = CollisionBoxes(1674, 623, 200, 200)
block13 = CollisionBoxes(1725, -119, 200, 120)
block14 = CollisionBoxes(1214, -271, 360, 20)
block15 = CollisionBoxes(1187, -386, 500, 100)
river1 = CollisionBoxes(1450, -231, 200, 120)
river2 = CollisionBoxes(1500, -109, 200, 60)
river3 = CollisionBoxes(1550, -46, 200, 40)
river4 = CollisionBoxes(1551, 151, 200, 200)
river5 = CollisionBoxes(1561, 359, 120, 150)
river6 = CollisionBoxes(1503, 519, 103, 110)
river7 = CollisionBoxes(1401, 655, 80, 150)
river8 = CollisionBoxes(1285, 812, 100, 120)
river9 = CollisionBoxes(1449, 594, 50, 40)
river10 = CollisionBoxes(1600, 525, 50, 80)
river11 = CollisionBoxes(1500, 650, 50, 65)
river12 = CollisionBoxes(1350, 730, 50, 66)
river13 = CollisionBoxes(1399, 821, 25, 40)
river14 = CollisionBoxes(1250, 949, 120, 75)
river15 = CollisionBoxes(1173, 1030, 40, 10)
river16 = CollisionBoxes(1278, 1196, 90, 44)
river17 = CollisionBoxes(1213, 1246, 220, 100)
river18 = CollisionBoxes(1263, 1353, 360, 70)
river19 = CollisionBoxes(1240, 885, 30, 45)
block16 = CollisionBoxes(828, 1323, 450, 90)
block17 = CollisionBoxes(-966, 1285, 100, 80)
block18 = CollisionBoxes(-957, -378, 310, 90)
block19 = CollisionBoxes(2034, 1400, 250, 23)
block20 = CollisionBoxes(2467, 1262, 130, 100)
block21 = CollisionBoxes(350, -250, 190, 200)
block22 = CollisionBoxes(750, -115, 200, 150)
block23 = CollisionBoxes(869, 37, 220, 130)
block24 = CollisionBoxes(882, 167, 100, 30)
block25 = CollisionBoxes(991, -27, 370, 90)
block26 = CollisionBoxes(1091, 66, 80, 50)
block27 = CollisionBoxes(261, 8, 240, 297)
block28 = CollisionBoxes(500, 53, 125, 350)
block29 = CollisionBoxes(646, 225, 80, 70)
block30 = CollisionBoxes(266, 308, 310, 100)
block31 = CollisionBoxes(215, 500, 210, 75)
block32 = CollisionBoxes(226, 410, 300, 70)
block33 = CollisionBoxes(600, 310, 60, 40)
block34 = CollisionBoxes(545, 416, 50, 40)
block35 = CollisionBoxes(1253, 216, 230, 70)
block36 = CollisionBoxes(1115, 307, 215, 190)
block37 = CollisionBoxes(1000, 430, 110, 50)
block38 = CollisionBoxes(865, 489, 300, 190)
block39 = CollisionBoxes(771, 545, 90, 90)
block40 = CollisionBoxes(882, 677, 120, 150)
block41 = CollisionBoxes(1049, 809, 70, 50)
block42 = CollisionBoxes(809, 700, 80, 70)
block43 = CollisionBoxes(573, 632, 50, 230)
block44 = CollisionBoxes(567, 903, 150, 143)
block45 = CollisionBoxes(642, 795, 50, 70)
block46 = CollisionBoxes(850, 870, 100, 130)

non_river_boxes = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19, block20, block21, block22, block23, block24, block25, block26, block27, block28, block29, block30, block31, block32, block33, block34, block35, block36, block37, block38, block39, block40, block41, block42, block43, block44, block45, block46]
collision_boxes = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12, block13, block14, block15, block16, block17, block18, block19, block20, block21, block22, block23, block24, block25, block26, block27, block28, block29, block30, block31, block32, block33, block34, block35, block36, block37, block38, block39, block40, block41, block42, block43, block44, block45, block46, river1, river2, river3, river4, river5, river6, river7, river8, river9, river10, river11, river12, river13, river14, river15, river16, river17, river18, river19]

"""
Below is where the global functions will go
"""


def check_collision(obj1, obj2):

    # Get the bounding boxes for both objects
    obj1_bounds = obj1.get_bounds()
    obj2_bounds = obj2.get_bounds()

    # Check if the bounding boxes are overlapping
    if obj1_bounds[0] < obj2_bounds[0] + obj2_bounds[2] and obj1_bounds[0] + obj1_bounds[2] > obj2_bounds[0]:
        if obj1_bounds[1] < obj2_bounds[1] + obj2_bounds[3]:
            if obj1_bounds[1] + obj1_bounds[3] > obj2_bounds[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def check_terrain_collision(obj1, obj2):

    # Get the bounding boxes for both objects
    obj1_bounds = obj1.get_bounds()
    obj2_left_bounds = obj2.get_bounds_1()
    obj2_right_bounds = obj2.get_bounds_2()
    obj2_top_bounds = obj2.get_bounds_3()
    obj2_bottom_bounds = obj2.get_bounds_4()

    # Check if the bounding boxes are overlapping
    if obj1_bounds[0] < obj2_left_bounds[0] + obj2_left_bounds[2] and obj1_bounds[0] + obj1_bounds[2] > obj2_left_bounds[0]:
        if obj1_bounds[1] < obj2_left_bounds[1] + obj2_left_bounds[3]:
            if obj1_bounds[1] + obj1_bounds[3] > obj2_left_bounds[1]:
                return 1
    # Check if the bounding boxes are overlapping
    if obj1_bounds[0] < obj2_right_bounds[0] + obj2_right_bounds[2] and obj1_bounds[0] + obj1_bounds[2] > obj2_right_bounds[0]:
        if obj1_bounds[1] < obj2_right_bounds[1] + obj2_right_bounds[3]:
            if obj1_bounds[1] + obj1_bounds[3] > obj2_right_bounds[1]:
                return 2
    # Check if the bounding boxes are overlapping
    if obj1_bounds[0] < obj2_top_bounds[0] + obj2_top_bounds[2] and obj1_bounds[0] + obj1_bounds[2] > obj2_top_bounds[0]:
        if obj1_bounds[1] < obj2_top_bounds[1] + obj2_top_bounds[3]:
            if obj1_bounds[1] + obj1_bounds[3] > obj2_top_bounds[1]:
                return 3
    # Check if the bounding boxes are overlapping
    if obj1_bounds[0] < obj2_bottom_bounds[0] + obj2_bottom_bounds[2] and obj1_bounds[0] + obj1_bounds[2] > obj2_bottom_bounds[0]:
        if obj1_bounds[1] < obj2_bottom_bounds[1] + obj2_bottom_bounds[3]:
            if obj1_bounds[1] + obj1_bounds[3] > obj2_bottom_bounds[1]:
                return 4
            else:
                return False
        else:
            return False
    else:
        return False


"""
Below are the main game loops.
This is where all of the logic for the game will go and this will loop until the player quits it.
"""
while start_screen:
    if just_opened:
        start_frame_count += 1
        if start_frame_count == 150:
            just_opened = False
        screen.fill(start_black)
        start_black[0] += .6
        screen.blit(startup_text, (600, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    else:
        if button_click:
            presses += 1
        screen.fill(WHITE)
        screen.blit(start_image, (0, 0))
        pygame.draw.rect(screen, button_color, (800, 600, 500, 100))
        screen.blit(start_text, (825, 605))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Handle mouse click on start button
                mouse_pos = event.pos
                if start_rect.collidepoint(mouse_pos):
                    button_color[1] += 50
                    # Start game
                    button_click = True
                    pygame.mixer.Sound.play(gong_start)
        if presses == 5:
            context_screen = True
            start_screen = False
            break

    # Capping framerate at 60 fps
    clock.tick(30)
    # Updating display
    pygame.display.update()

pygame.mixer.music.pause()

while context_screen:
    screen.fill(BLACK)
    context_frame_count += 1
    if context_frame_count >= 20:
        context_frame_count = 20
    context_frame_count_2 += 1
    if context_frame_count_2 == 20:
        context_frame_count_2 = 0
    screen.blit(context_text_1, (500, 100))
    screen.blit(context_text_2, (300, 150))
    screen.blit(context_text_3, (500, 300))
    screen.blit(context_text_4, (500, 350))
    screen.blit(context_text_5, (500, 400))
    screen.blit(context_text_6, (500, 450))
    screen.blit(context_text_7, (500, 500))
    screen.blit(context_text_8, (500, 550))
    screen.blit(context_text_9, (580, 650))
    if context_frame_count_2 == 0:
        context_text_9 = context_font.render("Click anywhere to start!", True, WHITE)
    elif context_frame_count_2 == 11:
        context_text_9 = context_font.render("Click anywhere to start!", True, BLACK)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if context_frame_count >= 20:
                context_screen = False
                game_loop = True

    # Capping framerate at 20 fps
    clock.tick(20)
    # Updating display
    pygame.display.update()

pygame.mixer.music.load("Sounds/game_music.wav")
pygame.mixer.music.play(-1)

# Main game loop
while game_loop:
    if start_of_wave:
        wave_startup_frames += 1
        round_intro_text = round_intro_font.render("ROUND "+str(wave_number), True, BLACK)
        if wave_startup_frames == 60:
            pygame.mixer.Sound.play(round_start_sound)
            wave_startup_frames = 0
            round_number_text = round_number_font.render(str(wave_number), True, BLACK)
            # Resetting lists for performance
            enemies = []
            player_spins = []
            player_attack = []
            player_dashes = []
            enemy_projectiles = []
            panda_enemy_max = wave_number // 2
            panda_enemy_min = wave_number // 4
            fox_enemy_max = int(wave_number * 1.2)
            fox_enemy_min = int(wave_number * .8)
            cat_enemy_max = wave_number * 2
            cat_enemy_min = wave_number
            # Spawning enemies needed
            if wave_number == 1:
                panda_enemies = 0
                fox_enemies = 0
                cat_enemies = 5
                while cat_enemies > 0:
                    enemies.append(NinjaCatEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), (random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1]))))
                    cat_enemies -= 1
            if wave_number == 2:
                panda_enemies = 0
                fox_enemies = 0
                cat_enemies = random.randint(8, 12)
                while cat_enemies > 0:
                    enemies.append(NinjaCatEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    cat_enemies -= 1
            if wave_number == 3:
                panda_enemies = 0
                fox_enemies = 5
                while fox_enemies > 0:
                    enemies.append(ArcherFoxEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    fox_enemies -= 1
                cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)
                while cat_enemies > 0:
                    enemies.append(NinjaCatEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    cat_enemies -= 1
            if wave_number == 4:
                panda_enemies = 1
                while panda_enemies > 0:
                    enemies.append(HeavyPandaEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    panda_enemies -= 1
                fox_enemies = 7
                while fox_enemies > 0:
                    enemies.append(ArcherFoxEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    fox_enemies -= 1
                cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)
                while cat_enemies > 0:
                    enemies.append(NinjaCatEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    cat_enemies -= 1
            if wave_number >= 5:
                panda_enemies = random.randint(panda_enemy_min, panda_enemy_max)
                while panda_enemies > 0:
                    enemies.append(HeavyPandaEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    panda_enemies -= 1
                fox_enemies = random.randint(fox_enemy_min, fox_enemy_max)
                while fox_enemies > 0:
                    enemies.append(ArcherFoxEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    fox_enemies -= 1
                cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)
                while cat_enemies > 0:
                    enemies.append(NinjaCatEnemy(random.randrange(-1750 - screen_scroll[0], 3000 - screen_scroll[0]), random.randrange(-700 - screen_scroll[1], 1600 - screen_scroll[1])))
                    cat_enemies -= 1
            start_of_wave = False


    if player.walking_down or player.walking_up or player.walking_right or player.walking_left:
        pygame.mixer.Sound.set_volume(walking_sound, 5)
    else:
        pygame.mixer.Sound.set_volume(walking_sound, 0)

    enemy_total = 0
    for enemy in enemies:
        if enemy.health > 0:
            enemy_total += 1

    if enemy_total == 0 and not start_of_wave:
        wave_number += 1
        start_of_wave = True

    if player.health <= 0:
        pygame.mixer.Sound.play(game_over_sound)
        pygame.mixer_music.pause()
        pygame.mixer.Sound.set_volume(walking_sound, 0)
        game_loop = False
        game_over = True
    screen.fill((255, 255, 255))

    # Limiting Screen Scroll
    if screen_scroll[0] < -1650:
        screen_scroll[0] = -1650
    if screen_scroll[0] > 1800:
        screen_scroll[0] = 1800
    if screen_scroll[1] < -770:
        screen_scroll[1] = -770
    if screen_scroll[1] > 930:
        screen_scroll[1] = 930
    for box in collision_boxes:
        box.main()
    screen.blit(background, (-1750 - screen_scroll[0], -770 - screen_scroll[1]))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Quitting pygame if needed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # Key presses
        if event.type == pygame.KEYDOWN:
            # Q key for shurikens
            if event.key == pygame.K_q:
                if player.can_throw:
                    pygame.mixer.Sound.play(shuriken_sound)
                    player_shurikens.append(PlayerShuriken(player.x, player.y, mouse_x, mouse_y))
                    player.shuriken_count -= 1
            # E key to heal
            if event.key == pygame.K_e:
                if player.healing_cooldown == 600:
                    pygame.mixer.Sound.play(heal)
                player.healing()
            # R key to dash
            if event.key == pygame.K_r:
                if player.dashing_cooldown == 3600:
                    pygame.mixer.Sound.play(smoke_bomb_sound)
                player.dashing()

            # F key to spin
            if event.key == pygame.K_f:
                if player.spin_cooldown == 4000:
                    pygame.mixer.Sound.play(spin_sound)
                player.spinning()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not player.is_slashing:
                pygame.mixer.Sound.play(sword_slash_sound)
                player_attack.append(PlayerAttack(player.x, player.y, mouse_x, mouse_y))
                player.is_slashing = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.walking_right = False
            if event.key == pygame.K_a:
                player.walking_left = False
            if event.key == pygame.K_w:
                player.walking_up = False
            if event.key == pygame.K_s:
                player.walking_down = False

    # Checking for keys getting pressed
    keys = pygame.key.get_pressed()

    # Adjusting screen scroll based on pressing movement keys
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        screen_scroll[0] -= 10
        player.walking_right = False
        player.walking_left = True
        player.not_moving = False
        screen_scroll_change_x = 10

        for shuriken in player_shurikens:
            shuriken.x += 10
        for arrow in enemy_projectiles:
            arrow.x += 10

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        screen_scroll[0] += 10
        player.walking_left = False
        player.walking_right = True
        player.not_moving = False
        screen_scroll_change_x = -10

        for shuriken in player_shurikens:
            shuriken.x -= 10
        for arrow in enemy_projectiles:
            arrow.x -= 10

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        screen_scroll[1] -= 10
        player.walking_up = True
        player.walking_down = False
        player.not_moving = False
        screen_scroll_change_y = 10

        for shuriken in player_shurikens:
            shuriken.y += 10
        for arrow in enemy_projectiles:
            arrow.y += 10

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        screen_scroll[1] += 10
        player.walking_up = False
        player.walking_down = True
        player.not_moving = False
        screen_scroll_change_y = -10

        for shuriken in player_shurikens:
            shuriken.y -= 10
        for arrow in enemy_projectiles:
            arrow.y -= 10

    if not keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if not keys[pygame.K_w] or keys[pygame.K_UP]:
            if not keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if not keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    player.not_moving = True

    # Doing damage if needed
    if player.immunity >= 60:
        for enemy in enemies:
            if check_collision(player, enemy) and not enemy.dead:
                player.health -= enemy.damage
                pygame.mixer.Sound.play(hurt_sound)
                player.immunity = 0
        for projectile in enemy_projectiles:
            if projectile.display:
                if check_collision(player, projectile):
                    pygame.mixer.Sound.play(hurt_sound)
                    player.health -= 4
                    player.immunity = 0
    for shuriken in player_shurikens:
        for enemy in enemies:
            if shuriken.display:
                if check_collision(shuriken, enemy):
                    enemy.health -= 3
    for spin in player_spins:
        if spin.animation < 100:
            for enemy in enemies:
                if check_collision(spin, enemy):
                    enemy.health -= .3
    for attack in player_attack:
        if attack.animation < 10:
            for enemy in enemies:
                if check_collision(attack, enemy):
                    enemy.health -= 1
    for shuriken in dropped_shurikens:
        if check_collision(player, shuriken) and not shuriken.picked_up:
            pygame.mixer.Sound.play(shuriken_pickup)
            player.shuriken_count += 3
            shuriken.picked_up = True
    for item in dropped_bombs:
        if check_collision(player, item) and not item.picked_up:
            item.picked_up = True
            pygame.mixer.Sound.play(shuriken_pickup)
            for enemy in enemies:
                enemy.health = 0
    for heart in dropped_hearts:
        if check_collision(player, heart) and not heart.picked_up:
            heart.picked_up = True
            player.health += 20
            pygame.mixer.Sound.play(ability_recharge)
            if player.health >= 40:
                player.health = 40
    for cooldown in dropped_cooldown:
        if check_collision(player, cooldown) and not cooldown.picked_up:
            cooldown.picked_up = True
            pygame.mixer.Sound.play(heal)
            player.dashing_cooldown = 3558
            player.spin_cooldown = 3998
            player.healing_cooldown = 598

    # Collision detection
    for box in collision_boxes:
        if check_terrain_collision(player, box) == 1:
            screen_scroll[0] -= 10
            for shuriken in player_shurikens:
                shuriken.x += 10
            for arrow in enemy_projectiles:
                arrow.x += 10
        if check_terrain_collision(player, box) == 2:
            screen_scroll[0] += 10
            for shuriken in player_shurikens:
                shuriken.x -= 10
            for arrow in enemy_projectiles:
                arrow.x -= 10
        if check_terrain_collision(player, box) == 3:
            screen_scroll[1] -= 10
            for shuriken in player_shurikens:
                shuriken.y += 10
            for arrow in enemy_projectiles:
                arrow.y += 10
        if check_terrain_collision(player, box) == 4:
            screen_scroll[1] += 10
            for shuriken in player_shurikens:
                shuriken.y -= 10
            for arrow in enemy_projectiles:
                arrow.y -= 10

        for enemy in enemies:
            if check_terrain_collision(enemy, box) == 1:
                enemy.x -= enemy.speed
                enemy.x_location_goal = box.left_side
                if enemy.y_location_goal < enemy.true_y:
                    enemy.y_location_goal = box.top_side
                else:
                    enemy.y_location_goal = box.bottom_side

            if check_terrain_collision(enemy, box) == 2:
                enemy.x += enemy.speed
                enemy.x_location_goal = box.right_side
                if enemy.y_location_goal < enemy.true_y:
                    enemy.y_location_goal = box.top_side
                else:
                    enemy.y_location_goal = box.bottom_side

            if check_terrain_collision(enemy, box) == 3:
                enemy.y -= enemy.speed
                enemy.y_location_goal = box.top_side
                if enemy.x_location_goal < enemy.true_x:
                    enemy.x_location_goal = box.left_side
                else:
                    enemy.x_location_goal = box.right_side

            if check_terrain_collision(enemy, box) == 4:
                enemy.y += enemy.speed
                enemy.y_location_goal = box.bottom_side
                if enemy.x_location_goal < enemy.true_x:
                    enemy.x_location_goal = box.left_side
                else:
                    enemy.x_location_goal = box.right_side

    for box in non_river_boxes:
        for shuriken in player_shurikens:
            if check_collision(box, shuriken):
                shuriken.display = False
        for arrow in enemy_projectiles:
            if check_collision(box, arrow):
                arrow.display = False

    # Updating player
    player.main()
    for spin in player_spins:
        spin.main()
    for attack in player_attack:
        if attack.animation <= 11:
            attack.main()
    for dash in player_dashes:
        dash.main()

    # Updating enemy
    for enemy in enemies:
        if enemy.health > 0:
            enemy.main()
        if enemy.health <= 0 and not enemy.dead:
            enemy.dead = True
            pygame.mixer.Sound.play(enemy_death)
            drop_chance = random.randint(0, 100)
            if drop_chance <= 25:
                dropped_shurikens.append(ShurikenDrop(enemy.x, enemy.y))
            elif 25 < drop_chance < 35:
                dropped_hearts.append(HeartDrop(enemy.x, enemy.y))
            elif 35 < drop_chance < 45:
                dropped_cooldown.append(CooldownDrop(enemy.x, enemy.y))
            elif drop_chance > 98:
                dropped_bombs.append(BombDrop(enemy.x, enemy.y))
        if enemy.dead:
            enemy.die()

    # Tracking projectiles
    for shuriken in player_shurikens:
        shuriken.main()
    for arrow in enemy_projectiles:
        arrow.main()
    for item in dropped_shurikens:
        item.main()
    for item in dropped_bombs:
        item.main()
    for item in dropped_cooldown:
        item.main()
    for item in dropped_hearts:
        item.main()

    player_health_bar.main()
    screen.blit(scroll, (1100, 440))
    player_cooldown_bars.main()

    if start_of_wave:
        screen.blit(round_scroll, (575, 270))
        screen.blit(round_intro_text, (650, 290))
    else:
        pygame.draw.rect(screen, BLACK, (1289, 9, 102, 42))
        pygame.draw.rect(screen, (252, 229, 169), (1290, 10, 100, 40))
        screen.blit(round_text, (1300, 20))
        screen.blit(round_number_text, (1350, 12))
        enemies_left_text = round_font.render("Enemies left: "+str(enemy_total), True, BLACK)
        pygame.draw.rect(screen, BLACK, (24, 24, 139, 27))
        pygame.draw.rect(screen, (252, 229, 169), (25, 25, 137, 25))
        screen.blit(enemies_left_text, (30, 30))


    # Quitting pygame if needed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capping framerate at 60 fps
    clock.tick(30)
    # Updating display
    pygame.display.update()


while game_over:
    screen.fill(BLACK)
    game_over_frames += 1
    if game_over_frames == 200:
        game_over = False
    screen.blit(game_over_text, (450, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Capping framerate at 60 fps
    clock.tick(30)
    # Updating display
    pygame.display.update()

pygame.quit()
sys.exit()
