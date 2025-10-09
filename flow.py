import random
wave_number = 7
print(wave_number)
panda_enemy_max = wave_number//2
panda_enemy_min = wave_number//4
fox_enemy_max = wave_number * 1.2
fox_enemy_min = wave_number * .8
cat_enemy_max = wave_number * 2
cat_enemy_min = wave_number
total_enemy_count = 0
panda_enemies = 0
fox_enemies = 0
cat_enemies = 0
enemies = [panda_enemies, fox_enemies, cat_enemies]
while True:
    enemy_total = panda_enemies + fox_enemies + cat_enemies
    panda_enemy_max = wave_number // 2
    panda_enemy_min = wave_number // 4
    fox_enemy_max = int(wave_number * 1.2)
    fox_enemy_min = int(wave_number * .8)
    cat_enemy_max = wave_number * 2
    cat_enemy_min = wave_number
    if enemy_total == 0:
        wave_number += 1
    if wave_number == 1:
        panda_enemies = 0
        fox_enemies = 0
        cat_enemies = 5
    if wave_number == 2:
        panda_enemies = 0
        fox_enemies = 0
        cat_enemies = random.randint(8, 12)
    if wave_number == 3:
        panda_enemies = 0
        fox_enemies = 5
        cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)
    if wave_number == 4:
        panda_enemies = 1
        fox_enemies = 7
        cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)
    if wave_number >= 5:
        panda_enemies = random.randint(panda_enemy_min, panda_enemy_max)
        fox_enemies = random.randint(fox_enemy_min, fox_enemy_max)
        cat_enemies = random.randint(cat_enemy_min, cat_enemy_max)

    print(panda_enemies, fox_enemies, cat_enemies)

