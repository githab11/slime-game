import random
import math

# Patch Notes - Version 0.8, Class Update!:

# - Classes have been added

# - Class 1: Commoner - Base Stats
# - Class 2: Glass Cannon - Higher Damage, Less HP
# - Class 3: Tank - Higher HP Less Damage
# I cant use the code without these var things right here? I might just have to init vars before putting them in an if statment.

player_level = 1
player_xp = 0
player_next_level_xp = 100
player_health = 25
player_maxhealth = 60
min_sword_dmg = 10
max_sword_dmg = 15
additive_dmg = 0
coins = 0
alive = True
advancing = 0


# Player stats
player_name = input("What is your name?: ")
print("Here are the classes you can play!")
print("The Commoner, regular stats")
print("The Tank: More HP less damage")
print("The Glass Cannon, more damage less hp")

class_input = input("What class would you like to play?: ")

if class_input[0].lower() == 'C':
    print("You have selected the Commoner")
    player_level = 1
    player_xp = 0
    player_next_level_xp = 100
    player_health = 25
    player_maxhealth = 60
    min_sword_dmg = 10
    max_sword_dmg = 15
    additive_dmg = 0
    coins = 0
    alive = True
    advancing = 0
elif class_input[0].lower() == 'G':
    print("You have selected the Glass Cannon")
    player_level = 1
    player_xp = 0
    player_next_level_xp = 100
    player_health = 25
    player_maxhealth = 25
    min_sword_dmg = 12
    max_sword_dmg = 14
    additive_dmg = 0
    coins = 0
    alive = True
    advancing = 0
elif class_input[0].lower() == 'T':
    print("You have selected Tank")
    player_level = 1
    player_xp = 0
    player_next_level_xp = 100
    player_health = 25
    player_maxhealth = 80
    min_sword_dmg = 6
    max_sword_dmg = 10
    additive_dmg = 0
    coins = 0
    alive = True
    advancing = 0
elif class_input.lower() == 'jack':
    print("Welcome Jack!")
    player_level = 1
    player_xp = 0
    player_next_level_xp = 100
    player_health = 10000
    player_maxhealth = 10000
    min_sword_dmg = 10000
    max_sword_dmg = 10000
    additive_dmg = 0
    coins = 1000
    alive = True
    advancing = 0



# Starting goblin stats
enemy_name = "Goblin"
enemy_coins = random.randint(3, 6)
enemy_health = 50
enemy_attack_min = 5
enemy_attack_max = 10
exp = 20

# Add these lines right after defining player_maxhealth
crit_chance = 10  # Initial crit chance
dodge_chance = 10  # Initial dodge chance

# Adjusted enemy stats
def set_goblin():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Goblin"
    enemy_coins = random.randint(3, 6)
    enemy_health = 20  # Adjusted enemy health
    enemy_attack_min = 4
    enemy_attack_max = 9

def set_skeleton():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Skeleton"
    enemy_coins = random.randint(5, 8)
    enemy_health = 30
    enemy_attack_min = 5
    enemy_attack_max = 10

def set_dragon():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dragon"
    enemy_coins = random.randint(15, 25)
    enemy_health = 80
    enemy_attack_min = 10
    enemy_attack_max = 20



# Function to gain XP
def gain_xp(amount):
    global player_xp, player_level, player_next_level_xp, min_sword_dmg, max_sword_dmg, player_health, crit_chance, dodge_chance
    player_xp += amount
    print(f"You have gained: {amount} XP!")
    print(f"{player_xp}/{player_next_level_xp}")

    while player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = math.floor(player_next_level_xp * 1.2)  # Adjusted XP required for leveling up
        print(f"{player_name} has leveled up to level {player_level}")
        if player_level == 3:
            power_up_input = input(f"You have reached level {player_level}!, would you like to increase your crit chance or your dodge chance?: ")
            if power_up_input.lower().startswith('c'):
                crit_chance -= 1
            elif power_up_input.lower().startswith('d'):
                dodge_chance -= 1

        valid_input = False
        while not valid_input:
            level_up_input = input("Upgrade sword damage (2) or health (10)? : ")  # Adjusted upgrade values

            if level_up_input.lower().startswith('s'):
                min_sword_dmg += 2  # Increased sword damage upgrade
                max_sword_dmg += 2  # Increased sword damage upgrade
                print(f"You have: {min_sword_dmg}-{max_sword_dmg} Damage!")
                valid_input = True
            elif level_up_input.lower().startswith('h'):
                player_health += 10  # Increased health upgrade
                player_maxhealth = player_health
                print(f"You have: {player_health} Health!")
                valid_input = True
            else:
                print("Invalid input. Please enter 's' to upgrade sword damage or 'h' to upgrade health.")

    print_values()

def fight():
    global exp, player_level, player_name, player_health, enemy_health, enemy_attack_max, enemy_attack_min, enemy_name, alive, coins, xp_gained, crit_chance, dodge_chance

    print(f"You have encountered a {enemy_name}!")
    print(f"The {enemy_name} has {enemy_health} health and deals {enemy_attack_min} <-> {enemy_attack_max} damage!")

    plr_actual_dmg = 0  # Initialize plr_actual_dmg
    actual_dmg = 0  # Initialize actual_dmg

    while player_health > 0 and enemy_health > 0:
        enemy_attack = input(f"Would you like to attack the {enemy_name}?: ")

        if enemy_attack.lower().startswith('y'):
            # Initialize the random vars
            dodge_chance_player = random.randint(1, dodge_chance)
            crit_chance_player = random.randint(1, crit_chance)

            if crit_chance_player == crit_chance and dodge_chance_player != dodge_chance:
                plr_actual_dmg = random.randint(min_sword_dmg, max_sword_dmg) * 1.5
                print(f"You've attacked {enemy_name} for: {plr_actual_dmg} With a CRIT!")
            elif dodge_chance_player != dodge_chance:
                plr_actual_dmg = random.randint(min_sword_dmg, max_sword_dmg)
                print(f"You've attacked {enemy_name} for: {plr_actual_dmg}")
            else:
                print(f"The {enemy_name} has dodged!")

            if crit_chance_player == crit_chance - 1 and dodge_chance_player != dodge_chance - 1:
                actual_dmg = random.randint(enemy_attack_min, enemy_attack_max) * 1.5
                print(f"The {enemy_name} has attacked you for: {actual_dmg} With a CRIT!")
            elif dodge_chance_player != dodge_chance - 1:
                actual_dmg = random.randint(enemy_attack_min, enemy_attack_max)
                print(f"The {enemy_name} has attacked you for: {actual_dmg}")
            else:
                print(f"{player_name} has dodged!")

            # Update enemy's health
            if dodge_chance_player != dodge_chance:
                enemy_health -= plr_actual_dmg

            if enemy_health <= 0:
                print(f"The {enemy_name} has been defeated!")
                print(f"You have been healed to: {player_maxhealth}!")
                player_health = player_maxhealth
                coins += enemy_coins
                print(f"The {enemy_name} has dropped {enemy_coins} coins, you now have {coins} coins!")

                xp_gained = exp
                gain_xp(xp_gained)

        elif enemy_attack.lower().startswith('n'):
            running_chance = random.randint(1, 10)
            if running_chance == 9:
                actual_dmg = random.randint(enemy_attack_min, enemy_attack_max)
                print("You have failed to run away!")
                print(f"The {enemy_name} has attacked you for: {actual_dmg}")
            else:
                print("You have run away from the enemy!")
                print(f"You have been healed for {player_maxhealth}!")
                player_health = player_maxhealth
                break  # End the fight

        if actual_dmg > 0:
            player_health -= actual_dmg

        print(f"The {enemy_name} has {enemy_health} health left!")
        print(f"You have {player_health} health left!")

# Game loop, had to rewrite this
advance = 0

while player_health > 0:
    if advance == 0:
        set_goblin()
        fight()
        if player_level >= 5:
            going_up = input("Would you like to level up?: ")
            if going_up.lower().startswith('y'):
                advance = 1
    elif advance == 1:
        set_skeleton()
        fight()
        if player_level >= 10:
            going_up1 = input("Would you like to level up?: ")
            if going_up1.lower().startswith('y'):
                advance = 2
    elif advance == 2:
        set_dragon()
        fight()

# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")
