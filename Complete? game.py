import random
import math

# Player stats
player_name = input("What is your name?: ")
player_level: int = 1
player_xp = 0
player_next_level_xp = 100
player_health = 75
player_maxhealth = 75
min_sword_dmg = 10
max_sword_dmg = 15
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

# Function to reroll sword damage
def reroll_dmg():
    global min_sword_dmg, max_sword_dmg
    min_sword_dmg = random.randint(5, 10)
    max_sword_dmg = random.randint(min_sword_dmg, 15)

# Function to set goblin stats

def set_goblin():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Goblin"
    enemy_coins = random.randint(3, 6)
    enemy_health = 40 + (player_level - 1) * 5
    enemy_attack_min = 5 + (player_level - 1)
    enemy_attack_max = 10 + (player_level - 1)
    exp = 20 + (player_level) * 2

# Skeleton Starting Stats
def set_skeleton():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Skeleton"
    enemy_coins = random.randint(5, 8)
    enemy_health = 50 + (player_level - 1) * 5
    enemy_attack_min = 8 + (player_level - 1)
    enemy_attack_max = 15 + (player_level - 1)
    exp = 40

def set_dragon():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dragon"
    enemy_coins = random.randint(15, 25)
    enemy_health = 120
    enemy_attack_min = 18
    enemy_attack_max = 25
    exp = 100

# Function to gain XP
def gain_xp(amount):
    global player_xp, player_level, player_next_level_xp, min_sword_dmg, max_sword_dmg, player_health
    player_xp += amount
    print(f"You have gained: {amount} XP!")
    print(f"{player_xp}/{player_next_level_xp}")

    while player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = math.floor(player_next_level_xp * 1.2)
        print(f"{player_name} has leveled up to level {player_level}")

        valid_input = False
        while not valid_input:
            levelupinput = input("Upgrade sword damage (2) or health (10)? : ")

            if levelupinput.lower().startswith('s'):
                min_sword_dmg += 2
                max_sword_dmg += 2
                print(f"You have: {min_sword_dmg}-{max_sword_dmg} Damage!")
                valid_input = True
            elif levelupinput.lower().startswith('h'):
                player_health += 10
                player_maxhealth = player_health
                print(f"You have: {player_health} Health!")
                valid_input = True
            else:
                print("Invalid input. Please enter 's' to upgrade sword damage or 'h' to upgrade health.")

    print_values()



def print_values():
    print(f"{player_name} Level: {player_level} XP: {player_xp}/{player_next_level_xp} Coins: {coins} Damage: {min_sword_dmg}-{max_sword_dmg}")

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

            if crit_chance == 10 and dodge_chance != 10:
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg) * 1.5
                print(f"You've attacked {enemy_name} for: {plractualdmg} With a CRIT!")
            elif dodge_chance != 10:
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg)
                print(f"You've attacked {enemy_name} for: {plractualdmg}")
            else:
                print(f"The {enemy_name} has dodged!")

            if crit_chance == 10 and dodge_chance != 10:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max) * 1.5
                print(f"The {enemy_name} has attacked you for: {actualdmg} With a CRIT!")
            elif dodge_chance != 10:
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
                break  # End the fight

        if actualdmg > 0:
            player_health -= actualdmg

        print(f"The {enemy_name} has {enemy_health} health left!")
        print(f"You have {player_health} health left!")







# Game loop
while alive and player_health > 0:
    if advancing == 0:
        fight()
        set_goblin()
        if player_level >= 5:
            print_values()
            advancinginput = input("Would you like to advance to the next area?:")
            if advancinginput[0].lower() == 'y':
                advancing = 1
                set_skeleton()
                fight()
                if player_level >= 10:
                    print_values()
                    advancinginput = input("Would you like to advance to the next arena?: ")
                    if advancinginput.lower() == 'y':
                        set_dragon()  # New addition: Set the dragon enemy
                        fight()

            elif advancinginput[0].lower() == 'n':
                advancing = 0
    if advancing == 1:
        fight()

# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")
