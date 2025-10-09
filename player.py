"""This is the player class for the game. This is going to control the player's movement, health, abilities, attacks,
cooldowns, and anything else pertaining to the player. This class will then be called into the main game for use."""

# Importing modules
import pygame
import sys
import math
import random


# Initializing pygame
pygame.init()
pygame.font.init()

# Handling movement
screen_scroll = [0, 0]

# Setting size of display (this will likely be removed after player class has been made)
screen = pygame.display.set_mode((800, 600))
# Setting clock to tick
clock = pygame.time.Clock()

background_img = pygame.image.load("Sprites/BackgroundOfShibaSamurai.png")
background = pygame.transform.scale(background_img, (5000, 2500))

# Player
player_idle_images = [pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_0.png"), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_1.png"), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_2.png"), pygame.image.load("Sprites/Sprites/Player_Idle/idle_player_3.png")]
player_walking_right_images = [pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_0.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_1.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_2.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_3.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_4.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_5.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_6.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Right/player_walking_right_7.png")]
player_walking_left_images = [pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+0.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+1.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+2.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+3.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+4.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+5.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+6.png"), pygame.image.load("Sprites/Sprites/Player_Walking_Left/left_player_walking+7.png")]
right_sword_slash_images = [pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_0.png"), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_1.png"), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_2.png"), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_3.png"), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_4.png"), pygame.image.load("Sprites/Sprites/Right Sword Slash/Right_Sword_Slash_5.png")]
left_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_0.png"), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_1.png"), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_2.png"), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_3.png"), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_4.png"), pygame.image.load("Sprites/Sprites/Sword Slash Left/Left_Sword_Slash_5.png")]
down_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_0.png"), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_1.png"), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_2.png"), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_3.png"), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_4.png"), pygame.image.load("Sprites/Sprites/Sword Slash Down/sword_slash_down_5.png")]
up_sword_slash_images = [pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_0.png"), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_1.png"), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_2.png"), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_3.png"), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_4.png"), pygame.image.load("Sprites/Sprites/Sword Slash Up/Up_Sword_Slash_5.png")]
shuriken_images = [pygame.image.load("Sprites/Sprites/Shuriken/shuriken_0.png"), pygame.image.load("Sprites/Sprites/Shuriken/shuriken_1.png")]
spin_images = [pygame.image.load("Sprites/Sprites/Spin Attack/spin_00.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_01.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_02.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_03.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_04.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_05.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_06.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_07.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_08.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_09.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_10.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_11.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_12.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_13.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_14.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_15.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_16.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_17.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_18.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_19.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_20.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_21.png"), pygame.image.load("Sprites/Sprites/Spin Attack/spin_22.png")]
dash_images = [pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_0.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_1.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_2.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_3.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_4.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_5.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_6.png"), pygame.image.load("Sprites/Sprites/Dash_Smoke/dash_smoke_7.png")]
player_damage = pygame.image.load("Sprites/Sprites/player_damage_0.png")
# Enemies
archer_fox_right_images = [pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_0.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_1.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_2.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_3.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_4.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_5.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_6.png"), pygame.image.load("Sprites/Sprites/Archer_Fox/archer_fox_7.png")]
archer_fox_left_images = [pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_0.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_1.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_2.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_3.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_4.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_5.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_6.png"), pygame.image.load("Sprites/Sprites/Archer_Fox_Left/left_archer_fox_7.png")]
archer_fox_arrow = [pygame.image.load("Sprites/Sprites/Arrow/arrow_0.png"), pygame.image.load("Sprites/Sprites/Arrow/arrow_1.png")]
ninja_cat_right_images = [pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_0.png"), pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_1.png"), pygame.image.load("Sprites/Sprites/Ninja_Cat/Ninja_Cat_2.png")]
ninja_cat_left_images = [pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_0.png"), pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_1.png"), pygame.image.load("Sprites/Sprites/Ninja_Cat_Left/ninja_cat_left_2.png")]
panda_enemy_right_images = [pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_0.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_1.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_2.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_3.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_4.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_5.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_6.png"), pygame.image.load("Sprites/Sprites/Panda Enemy/Panda_Enemy_7.png")]
panda_enemy_left_images = [pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_0.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_1.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_2.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_3.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_4.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_5.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_6.png"), pygame.image.load("Sprites/Sprites/Panda_Enemy_Left/Panda_Left_7.png")]
archer_fox_arrow_left = pygame.image.load("Sprites/Sprites/arrow_left.png")


class ShurikenDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.picked_up = False

    def get_bounds(self):
        bounds = (self.true_x, self.true_y, 40, 40)
        return bounds

    def main(self):
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if not self.picked_up:
            screen.blit(shuriken_images[0], (self.true_x, self.true_y))


class HeavyPandaEnemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
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

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x, self.true_y, self.width, self.height)
        return bounds

    def main(self):
        self.animation_count += 1
        if self.animation_count == 80:
            self.animation_count = 0
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        if self.x - screen_scroll[0] > self.x_location_goal:
            self.x -= 1
            self.walking_right = False
            self.walking_left = True
        elif self.x - screen_scroll[0] < self.x_location_goal:
            self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 1
        elif self.y - screen_scroll[1] < self.y_location_goal:
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



class ArcherFoxEnemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.true_x = self.x - screen_scroll[0]
        self.true_y = self.y - screen_scroll[1]
        self.height = height
        self.width = width
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
                enemy_projectiles.append(ArcherFoxEnemyArrow(self.true_x, self.true_y))
                self.arrow_cooldown = 1

    def main(self):
        self.animation_count += 1
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
            self.walking_right = False
            self.walking_left = True
        elif self.x - screen_scroll[0] < self.x_location_goal:
            self.x += 1
            if self.x - screen_scroll[0] < self.x_location_goal:
                self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 1.5
        elif self.y - screen_scroll[1] < self.y_location_goal:
            self.y += 1.5
        # Attack cooldown
        if self.arrow_cooldown > 0:
            self.arrow_cooldown += 1
        if self.arrow_cooldown == 100:
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
        self.speed = 8
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
            self.animation_count += 1
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


class NinjaCatEnemy:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
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

    # Getting hit box
    def get_bounds(self):
        bounds = (self.true_x, self.true_y, self.width, self.height)
        return bounds

    def main(self):
        self.animation_count += 1
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
            self.walking_right = False
            self.walking_left = True
        elif self.x-screen_scroll[0] < self.x_location_goal:
            self.x += 1
            if self.x - screen_scroll[0] < self.x_location_goal:
                self.x += 1
                if self.x - screen_scroll[0] < self.x_location_goal:
                    self.x += 1
            self.walking_left = False
            self.walking_right = True
        if self.y - screen_scroll[1] > self.y_location_goal:
            self.y -= 2
        elif self.y - screen_scroll[1] < self.y_location_goal:
            self.y += 2
        self.location_goal_shift += 1
        if self.location_goal_shift == 150:
            self.location_goal_shift = 0
            self.x_location_goal = player.x + random.randint(-17, 17)
            self.y_location_goal = player.y + random.randint(-17, 17)
        if self.walking_left:
            screen.blit(ninja_cat_left_images[self.animation_count//10], (self.true_x, self.true_y))
        else:
            screen.blit(ninja_cat_right_images[self.animation_count//10], (self.true_x, self.true_y))


class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = 20
        self.health = 20
        self.last_health = 20
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
        self.spin_cooldown = 5000
        self.can_spin = True
        # Healing ability
        self.healing_factor = 5
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
            if self.health > 20:
                self.health = 20
            self.can_heal = False
            self.healing_cooldown = 0

    # Dashing method
    def dashing(self):
        if self.can_dash:
            self.is_dashing = True
            self.can_dash = False
            self.dashing_cooldown = 0
            # Checking for keys getting pressed
            keys_d = pygame.key.get_pressed()
            player_dashes.append(PlayerDash(player.x, player.y))

            # Adjusting screen scroll based on pressing movement keys
            if keys_d[pygame.K_LEFT] or keys_d[pygame.K_a]:
                screen_scroll[0] -= self.dash_distance

            if keys_d[pygame.K_d] or keys_d[pygame.K_RIGHT]:
                screen_scroll[0] += self.dash_distance


            if keys_d[pygame.K_w] or keys_d[pygame.K_UP]:
                screen_scroll[1] -= self.dash_distance


            if keys_d[pygame.K_s] or keys_d[pygame.K_DOWN]:
                screen_scroll[1] += self.dash_distance

    # Spinning method
    def spinning(self):
        if self.can_spin:
            player_spins.append(PlayerSpin(self.x, self.y))
            self.can_spin = False
            self.spin_cooldown = 0

    # Player main
    def main(self):
        self.idle_animation += 1
        if self.idle_animation == 40:
            self.idle_animation = 0
        self.walking_animation += 1
        if self.walking_animation == 80:
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
                    screen.blit(player_walking_left_images[self.walking_animation//10], (self.x, self.y))
                else:
                    screen.blit(player_walking_right_images[self.walking_animation//10], (self.x, self.y))


        self.immunity += 1

        """Checking for cooldowns"""
        # Healing
        if not self.can_heal:
            self.healing_cooldown += 1
            if self.healing_cooldown == 601:
                self.healing_cooldown = 600
        if self.healing_cooldown == 600:
            if self.health <= 19:
                self.can_heal = True

        # Dashing
        if not self.can_dash:
            self.dashing_cooldown += 1
            if self.dashing_cooldown == 3600:
                self.can_dash = True

        # Spinning
        if not self.can_spin:
            self.spin_cooldown += 1
            if self.spin_cooldown == 5000:
                self.can_spin = True

        # Shurikens
        if self.shuriken_count == 0:
            self.can_throw = False
        if self.shuriken_count > 0:
            self.can_throw = True
        if self.is_slashing:
            self.slash_counter += 1
            if self.slash_counter == 15:
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
        if mouse_x > player.x + 20:
            self.x += 60
            self.right = True
        elif mouse_x < player.x - 20:
            self.x -= 30
            self.left = True
        else:
            self.x += 0
        if mouse_y > player.y + 20:
            self.y += 60
            self.down = True
        elif mouse_y < player.y - 20:
            self.y -= 30
            self.up = True
        else:
            self.y += 0

    # Getting hit box
    def get_bounds(self):
        bounds = (self.x, self.y, 150, 150)
        return bounds

    def main(self):
        if self.counter < 10:
            self.animation += 1
            if self.animation == 240:
                self.animation = 0
            if self.right:
                screen.blit(pygame.transform.scale(right_sword_slash_images[self.animation//40], (150, 150)), (self.x-50, self.y))
            elif self.left:
                screen.blit(pygame.transform.scale(left_sword_slash_images[self.animation//40], (150, 150)), (self.x, self.y))
            else:
                if self.up:
                    screen.blit(pygame.transform.scale(up_sword_slash_images[self.animation//40], (150, 150)), (self.x, self.y))
                elif self.down:
                    screen.blit(pygame.transform.scale(down_sword_slash_images[self.animation//40], (150, 150)), (self.x, self.y))

            self.counter += 1


class PlayerHealthBar:
    def __init__(self):
        self.x = 10
        self.y = 550
        self.max_x = 100
        self.width = 100
        self.height = 20
        self.health_bar_color = (0, 255, 0)

    def main(self):
        self.width = player.health * 5
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
        if self.animation < 70:
            self.x = self.x_2 - screen_scroll[0]
            self.y = self.y_2 - screen_scroll[1]
            self.animation += 1
            screen.blit(dash_images[self.animation//10], (self.x, self.y))


class PlayerCooldowns:
    def __init__(self):
        self.x = 700
        self.dash_y = 450
        self.spin_y = 500
        self.heal_y = 550
        self.width = 80
        self.height = 20
        self.shuriken_y = 380
        self.shuriken_height = 80
        self.dash_width = player.dashing_cooldown / 45
        self.spin_width = player.spin_cooldown / 62.5
        self.heal_width = player.healing_cooldown / 7.5
        self.cooldown_font = pygame.font.SysFont("Ariel", 20)
        self.dash_cooldown_font = self.cooldown_font.render("Dash (R)", True, (0, 0, 0))
        self.spin_cooldown_font = self.cooldown_font.render("Spin (F)", True, (0, 0, 0))
        self.heal_cooldown_font = self.cooldown_font.render("Heal (E)", True, (0, 0, 0))
        self.shuriken_count = str(player.shuriken_count)
        self.shuriken_count_font = pygame.font.SysFont("Ariel", 40)
        self.shuriken_count_text = self.shuriken_count_font.render(self.shuriken_count, True, (0, 0, 0))

    def main(self):
        self.dash_width = player.dashing_cooldown / 45
        self.spin_width = player.spin_cooldown / 62.5
        self.heal_width = player.healing_cooldown / 7.5

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

        screen.blit(shuriken_images[0], (self.x, self.shuriken_y))
        screen.blit(self.shuriken_count_text, (self.x + 50, self.shuriken_y + 20))


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
            self.animation += 1
            screen.blit(pygame.transform.scale(spin_images[self.animation//5], (300, 300)), (self.x, self.y))


# To track throwing stars
class PlayerShuriken:
    def __init__(self, x, y, mouse_x_pos, mouse_y_pos):
        # Initializing these
        self.x = x
        self.y = y
        self.mouse_x = mouse_x_pos
        self.mouse_y = mouse_y_pos
        self.speed = 10
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
    def main(self, display):
        if self.display:
            self.x -= int(self.x_vel)
            self.y -= int(self.y_vel)

            self.animation += 1
            if self.animation == 20:
                self.animation = 0
            screen.blit(shuriken_images[self.animation // 10], (self.x-30, self.y-30))


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

        self.left_side = self.true_x - 50
        self.right_side = self.true_x + self.width + 50
        self.top_side = self.true_y - 50
        self.bottom_side = self.true_y + self.height + 50

        self.left_bounds = (self.true_x - 5, self.true_y, 5, self.height)
        self.right_bounds = (self.true_x + self.width, self.true_y, 5, self.height)
        self.top_bounds = (self.true_x, self.true_y - 5, self.width, 5)
        self.bottom_bounds = (self.true_x, self.true_y + self.height, self.width, 5)
        pygame.draw.rect(screen, self.color, (self.true_x - 5, self.true_y, 5, self.height))
        pygame.draw.rect(screen, self.color, (self.true_x + self.width, self.true_y, 5, self.height))
        pygame.draw.rect(screen, self.color, (self.true_x, self.true_y - 5, self.width, 5))
        pygame.draw.rect(screen, self.color, (self.true_x, self.true_y + self.height, self.width, 5))


# Creating player
player = Player(400, 300, 32, 32)
player_health_bar = PlayerHealthBar()
player_cooldown_bars = PlayerCooldowns()

# Creating collision zones
rock1 = CollisionBoxes(890, 560, 130, 100)
tree1 = CollisionBoxes(1080, 950, 200, 200)
tree2 = CollisionBoxes(1320, 600, 150, 150)
rock2 = CollisionBoxes(1360, 800, 130, 130)

# Creating enemy
enemy = NinjaCatEnemy(200, 200, 50, 80)
enemy2 = ArcherFoxEnemy(100, 200, 70, 90)
enemy3 = HeavyPandaEnemy(300, 100, 130, 150)

# List of shurikens
player_shurikens = []
player_spins = []
player_attack = []
dropped_shurikens = []
player_dashes = []

# List of enemy projectiles
enemy_projectiles = []

# List of enemies
enemies = [enemy, enemy2, enemy3]

# Collisions
"""
If the player collides with an enemy or an enemy projectile, the player will take damage = to damage of that
If an enemy collides with a player attack, the enemy will take damage = to damage of that
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


# Main game loop. This is mostly to be used to test things as the player class is made and will not remain here
while True:
    screen.fill((255, 255, 255))

    # Limiting Screen Scroll
    if screen_scroll[0] < 0:
        screen_scroll[0] = 0
    if screen_scroll[0] > 3790:
        screen_scroll[0] = 3790
    if screen_scroll[1] < -95:
        screen_scroll[1] = -95
    if screen_scroll[1] > 1790:
        screen_scroll[1] = 1790

    screen.blit(background, (-100-screen_scroll[0], -100-screen_scroll[1]))
    rock1.main()

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
                    player_shurikens.append(PlayerShuriken(player.x, player.y, mouse_x, mouse_y))
                    player.shuriken_count -= 1
            # E key to heal
            if event.key == pygame.K_e:
                player.healing()
                print(player.health)
            # R key to dash
            if event.key == pygame.K_r:
                player.dashing()

            # F key to spin
            if event.key == pygame.K_f:
                player.spinning()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not player.is_slashing:
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

    if keys[pygame.K_p]:
        print(player.x + screen_scroll[0] + 100)
        print(player.y + screen_scroll[1] + 100)


    # Adjusting screen scroll based on pressing movement keys
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        screen_scroll[0] -= 5
        player.walking_right = False
        player.walking_left = True
        player.not_moving = False
        screen_scroll_change_x = 5

        for shuriken in player_shurikens:
            shuriken.x += 5
        for arrow in enemy_projectiles:
            arrow.x += 5

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        screen_scroll[0] += 5
        player.walking_left = False
        player.walking_right = True
        player.not_moving = False
        screen_scroll_change_x = -5

        for shuriken in player_shurikens:
            shuriken.x -= 5
        for arrow in enemy_projectiles:
            arrow.x -= 5

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        screen_scroll[1] -= 5
        player.walking_up = True
        player.walking_down = False
        player.not_moving = False
        screen_scroll_change_y = 5

        for shuriken in player_shurikens:
            shuriken.y += 5
        for arrow in enemy_projectiles:
            arrow.y += 5

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        screen_scroll[1] += 5
        player.walking_up = False
        player.walking_down = True
        player.not_moving = False
        screen_scroll_change_y = -5

        for shuriken in player_shurikens:
            shuriken.y -= 5
        for arrow in enemy_projectiles:
            arrow.y -= 5

    if not keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if not keys[pygame.K_w] or keys[pygame.K_UP]:
            if not keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if not keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    player.not_moving = True


    # Drawing rectangle for reference (this will be removed in final code)
    pygame.draw.rect(screen, (0, 0, 0), (1360-screen_scroll[0], 800-screen_scroll[1], 130, 130))

    # Doing damage if needed
    if player.immunity >= 60:
        for enemy in enemies:
            if check_collision(player, enemy) and not enemy.dead:
                player.health -= enemy.damage
                player.immunity = 0
                print("hit")
                print(player.health)
        for projectile in enemy_projectiles:
            if projectile.display:
                if check_collision(player, projectile):
                    player.health -= 4
                    player.immunity = 0
                    print("hit")
                    print(player.health)
    for shuriken in player_shurikens:
        for enemy in enemies:
            if shuriken.display:
                if check_collision(shuriken, enemy):
                    enemy.health -= 3
                    print("enemy hit")
    for spin in player_spins:
        if spin.animation < 100:
            for enemy in enemies:
                if check_collision(spin, enemy):
                    enemy.health -= .3
    for attack in player_attack:
        if attack.counter < 10:
            for enemy in enemies:
                if check_collision(attack, enemy):
                    enemy.health -= 1
    for shuriken in dropped_shurikens:
        if check_collision(player, shuriken) and not shuriken.picked_up:
            player.shuriken_count += 3
            shuriken.picked_up = True

    if check_terrain_collision(player, rock1) == 1:
        screen_scroll[0] -= 5
        for shuriken in player_shurikens:
            shuriken.x += 5
        for arrow in enemy_projectiles:
            arrow.x += 5
    if check_terrain_collision(player, rock1) == 2:
        screen_scroll[0] += 5
        for shuriken in player_shurikens:
            shuriken.x -= 5
        for arrow in enemy_projectiles:
            arrow.x -= 5
    if check_terrain_collision(player, rock1) == 3:
        screen_scroll[1] -= 5
        for shuriken in player_shurikens:
            shuriken.y += 5
        for arrow in enemy_projectiles:
            arrow.y += 5
    if check_terrain_collision(player, rock1) == 4:
        screen_scroll[1] += 5
        for shuriken in player_shurikens:
            shuriken.y -= 5
        for arrow in enemy_projectiles:
            arrow.y -= 5


    for enemy in enemies:
        if check_terrain_collision(enemy, rock1) == 1:
            enemy.x -= enemy.speed
            enemy.x_location_goal = rock1.left_side
            if enemy.y_location_goal < enemy.true_y:
                enemy.y_location_goal = rock1.top_side
            else:
                enemy.y_location_goal = rock1.bottom_side

        if check_terrain_collision(enemy, rock1) == 2:
            enemy.x += enemy.speed
            enemy.x_location_goal = rock1.right_side
            if enemy.y_location_goal < enemy.true_y:
                enemy.y_location_goal = rock1.top_side
            else:
                enemy.y_location_goal = rock1.bottom_side

        if check_terrain_collision(enemy, rock1) == 3:
            enemy.y -= enemy.speed
            enemy.y_location_goal = rock1.top_side
            if enemy.x_location_goal < enemy.true_x:
                enemy.x_location_goal = rock1.left_side
            else:
                enemy.x_location_goal = rock1.right_side

        if check_terrain_collision(enemy, rock1) == 4:
            enemy.y += enemy.speed
            enemy.y_location_goal = rock1.bottom_side
            if enemy.x_location_goal < enemy.true_x:
                enemy.x_location_goal = rock1.left_side
            else:
                enemy.x_location_goal = rock1.right_side

    for shuriken in player_shurikens:
        if check_collision(rock1, shuriken):
            shuriken.display = False
    for arrow in enemy_projectiles:
        if check_collision(rock1, arrow):
            arrow.display = False


    # Updating player
    player.main()
    for spin in player_spins:
        spin.main()
    for attack in player_attack:
        attack.main()
    for dash in player_dashes:
        dash.main()



    # Updating enemy
    for enemy in enemies:
        if enemy.health > 0:
            enemy.main()
        if enemy.health <= 0 and not enemy.dead:
            enemy.dead = True
            drop_chance = random.randint(0, 20)
            if drop_chance <= 5:
                dropped_shurikens.append(ShurikenDrop(enemy.x, enemy.y))


    # Tracking projectiles
    for shuriken in player_shurikens:
        shuriken.main(screen)
    for arrow in enemy_projectiles:
        arrow.main()
    for item in dropped_shurikens:
        item.main()

    player_health_bar.main()
    player_cooldown_bars.main()

    # Capping framerate at 60 fps
    clock.tick(60)
    # Updating display
    pygame.display.update()
