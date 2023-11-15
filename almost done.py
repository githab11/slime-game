import random
import math

# Patch Notes - Version 0.7: Power-Up Edition

# General:
# - Adjusted game progression for a more balanced experience.
# - Revised enemy encounters for a smoother difficulty curve.

# Player Stats:
# - Increased initial sword damage to 10-15 for a more manageable early-game experience.
# - Adjusted XP required for leveling up to provide a more consistent progression.
# - Increased sword damage upgrade to +2 for more impactful scaling.
# - Health upgrade is now 60 to provide a nice difference between each enemy.

# Power-Ups:
# - Added a power-up system at level 3. Players can now choose to increase their crit chance or dodge chance.

# Enemy Stats:
# - Goblin:
#   - Health reduced to 20 for an easier early-game challenge.
#   - Adjusted attack range to 4-9 for balanced combat.

# - Skeleton:
#   - Decreased health to 30 for a progressive difficulty curve.
#   - Modified attack range to 5-10 for a fair challenge.

# - Dragon:
#   - Lowered health to 80 for a challenging late-game encounter.
#   - Adjusted attack range to 10-20 for strategic gameplay.

# Bug Fixes:
# - Corrected variable assignments in the game loop for more accurate gameplay.

# Player stats
player_name = input("What is your name?: ")

player_level: int = 1
player_xp = 0
player_next_level_xp = 100
player_health = 60
player_maxhealth = 60
min_sword_dmg = 10  # Adjusted initial sword damage
max_sword_dmg = 15  # Adjusted initial sword damage
additive_dmg = 0
coins = 0
alive = True
advancing = 0

# Enemy Starting stats
enemy_name = "Goblin"
enemy_coins = random.randint(3, 6)
enemy_health = 50
enemy_attack_min = 5
enemy_attack_max = 10
exp = 20

# Add these lines right after defining player_maxhealth
critchance = 10  # Initial crit chance
dodgechance = 10  # Initial dodge chance

# Function to reroll sword damage
def reroll_dmg():
    global min_sword_dmg, max_sword_dmg
    min_sword_dmg = random.randint(10, 15)  # Rerolled damage
    max_sword_dmg = random.randint(min_sword_dmg, 20)  # Rerolled damage

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

def print_values():
    print(f"{player_name} Level: {player_level} XP: {player_xp}/{player_next_level_xp} Coins: {coins} Damage: {min_sword_dmg}-{max_sword_dmg}")

# Function to gain XP
def gain_xp(amount):
    global player_xp, player_level, player_next_level_xp, min_sword_dmg, max_sword_dmg, player_health, critchance, dodgechance
    player_xp += amount
    print(f"You have gained: {amount} XP!")
    print(f"{player_xp}/{player_next_level_xp}")

    while player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = math.floor(player_next_level_xp * 1.2)  # Adjusted XP required for leveling up
        print(f"{player_name} has leveled up to level {player_level}")
        if player_level == 3:
            powerupinput = input(f"You have reached level {player_level}!, would you like to increase your crit chance or your dodge chance?: ")
            if powerupinput[0].lower() == 'c':
                critchance -= 1
            elif powerupinput[0].lower() == 'd':
                dodgechance -= 1

        valid_input = False
        while not valid_input:
            levelupinput = input("Upgrade sword damage (2) or health (10)? : ")  # Adjusted upgrade values

            if levelupinput.lower().startswith('s'):
                min_sword_dmg += 2  # Increased sword damage upgrade
                max_sword_dmg += 2  # Increased sword damage upgrade
                print(f"You have: {min_sword_dmg}-{max_sword_dmg} Damage!")
                valid_input = True
            elif levelupinput.lower().startswith('h'):
                player_health += 10  # Increased health upgrade
                player_maxhealth = player_health
                print(f"You have: {player_health} Health!")
                valid_input = True
            else:
                print("Invalid input. Please enter 's' to upgrade sword damage or 'h' to upgrade health.")

    print_values()

def fight():
    global exp, player_level, player_name, player_health, enemy_health, enemy_attack_max, enemy_attack_min, enemy_name, alive, coins, xp_gained

    print(f"You have encountered a {enemy_name}!")
    print(f"The {enemy_name} has {enemy_health} health and deals {enemy_attack_min} <-> {enemy_attack_max} damage!")

    plractualdmg = 0  # Initialize plractualdmg
    actualdmg = 0  # Initialize actualdmg

    while player_health > 0 and enemy_health > 0:
        enemy_attack = input(f"Would you like to attack the {enemy_name}?: ")

        if enemy_attack.lower().startswith('y'):
            # Initialize the random vars
            dodge_chance = random.randint(1, 10)
            crit_chance = random.randint(1, 10)
            dodge_chance_player = random.randint(1, dodgechance)
            crit_chance_player = random.randint(1, critchance)


            if crit_chance == random.randint(1, crit_chance) and dodge_chance != random.randint(1, dodgechance):
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg) * 1.7
                print(f"You've attacked {enemy_name} for: {plractualdmg} With a CRIT!")
            elif dodge_chance != 10:
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg)
                print(f"You've attacked {enemy_name} for: {plractualdmg}")
            else:
                print(f"The {enemy_name} has dodged!")

            if crit_chance == 9 and dodge_chance != 9:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max) * 1.4
                print(f"The {enemy_name} has attacked you for: {actualdmg} With a CRIT!")
            elif dodge_chance != 9:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max)
                print(f"The {enemy_name} has attacked you for: {actualdmg}")
            else:
                print(f"{player_name} has dodged!")

            # Update enemy's health
            if dodge_chance != 10:
                enemy_health -= plractualdmg

            if enemy_health <= 0:
                print(f"The {enemy_name} has been defeated!")
                print(f"You have been healed to: {player_maxhealth}!")
                player_health = player_maxhealth
                coins += enemy_coins
                print(f"The {enemy_name} has dropped {enemy_coins} coins, you now have {coins} coins!")

                xp_gained = exp
                gain_xp(xp_gained)

        elif enemy_attack.lower().startswith('n'):
            runningchance = random.randint(1, 10)
            if runningchance == 9:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max)
                print("You have failed to run away!")
                print(f"The {enemy_name} has attacked you for: {actualdmg}")
            else:
                print("You have run away from the enemy!")
                print(f"You have been healed for {player_maxhealth}!")
                player_health == player_maxhealth
                break  # End the fight

        if actualdmg > 0:
            player_health -= actualdmg

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
