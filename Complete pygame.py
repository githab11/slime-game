import random
import math

# Player stats
player_name = input("What is your name?: ")
player_level: int = 1
player_xp = 0
player_next_level_xp = 100
player_health = 75
player_maxhealth = 75
min_sword_dmg = 7
max_sword_dmg = 13
additive_dmg = 0
coins = 0
alive = True
advancing = 0

# Enemy Starting stats
enemy_name = "Goblin"
enemy_coins = random.randint(3, 6)
enemy_health = 40
enemy_attack_min = 5
enemy_attack_max = 10

# Function to reroll sword damage
def reroll_dmg():
    global min_sword_dmg, max_sword_dmg
    min_sword_dmg = random.randint(5, 10)
    max_sword_dmg = random.randint(min_sword_dmg, 15)

# Function to set goblin stats
def set_goblin():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max
    enemy_name = "Goblin"
    enemy_coins = random.randint(3, 6)
    enemy_health = 40
    enemy_attack_min = 5
    enemy_attack_max = 10
    Goblin_test = 20

# Skeleton Starting Stats
def set_skeleton():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max
    enemy_name = "Skeleton"
    enemy_coins = random.randint(5, 8)
    enemy_health = 50
    enemy_attack_min = 8
    enemy_attack_max = 15
    Skeleton_test = 40

# Function to gain XP
def gain_xp(amount):
    global player_xp, player_level, player_next_level_xp, min_sword_dmg, max_sword_dmg
    player_xp += amount
    print(f"You have gained: {amount} XP!")
    print(f"{player_xp}/{player_next_level_xp}")

    while player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = math.floor(player_next_level_xp * 1.2)
        print(f"{player_name} has leveled up to level {player_level}")
        levelupinput = input("Upgrade sword damage (2) or health (10)? : ")
        if levelupinput.lower().startswith('s'):
            global max_sword_dmg  # Add this line
            min_sword_dmg += 2
            max_sword_dmg += 2
            print(f"You have: {min_sword_dmg}-{max_sword_dmg} Damage!")
        elif levelupinput.lower().startswith('h'):
            player_health += 10
            player_maxhealth = player_health
            print(f"You have: {player_health} Health!")

def print_values():
    print(f"{player_name} Level: {player_level} XP: {player_xp}/{player_next_level_xp} Coins: {coins} Damage: {min_sword_dmg}-{max_sword_dmg}")

def fight():
    global player_level, player_name, player_health, enemy_health, enemy_attack_max, enemy_attack_min, enemy_name, alive, coins, xp_gained

    print(f"You have encountered a {enemy_name}!")
    print(f"The {enemy_name} has {enemy_health} health and deals {enemy_attack_min} <-> {enemy_attack_max} damage!")

    while player_health > 0 and enemy_health > 0:
        enemy_attack = input(f"Would you like to attack the {enemy_name}?: ")
        actualdmg = 0

        if enemy_attack.lower().startswith('y'):
            # Initialize the random vars
            player_misschance = random.randint(1, 10)
            enemy_misschance = random.randint(1, 10)
            player_critchance = random.randint(1, 10)
            enemy_critchance = random.randint(1, 10)

            if player_critchance == 10 and player_misschance != 10:
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg) * 1.5
                print(f"You've attacked {enemy_name} for: {plractualdmg} With a CRIT!")
            elif player_misschance != 10:
                plractualdmg = random.randint(min_sword_dmg, max_sword_dmg)
                print(f"You've attacked {enemy_name} for: {plractualdmg}")
            else:
                print(f"The {enemy_name} has dodged!")

            if enemy_critchance == 10 and enemy_misschance != 10:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max) * 1.5
                print(f"The {enemy_name} has attacked you for: {actualdmg} With a CRIT!")
            elif enemy_misschance != 10:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max)
                print(f"The {enemy_name} has attacked you for: {actualdmg}")
            else:
                print(f"{player_name} has dodged!")

            # Update enemy's health
            if enemy_misschance != 10:
                enemy_health -= plractualdmg

            if enemy_health <= 0:
                print(f"The {enemy_name} has been defeated!")
                print(f"You have been healed to: {player_maxhealth}!")
                player_health = player_maxhealth
                coins += enemy_coins
                print(f"The {enemy_name} has dropped {enemy_coins} coins, you now have {coins} coins!")

                # Define xp_gained here
                xp_gained = 20  # You can adjust the XP gain as needed
                gain_xp(xp_gained)

        elif enemy_attack.lower().startswith('n'):
            runningchance = random.randint(1, 10)
            if runningchance == 9:
                actualdmg = random.randint(enemy_attack_min, enemy_attack_max)
                print("You have failed to run away!")
                print(f"The {enemy_name} has attacked you for: {actualdmg}")
            else:
                print("You have run away from the enemy!")
                break  # End the fight if you run away

        if actualdmg > 0:
            # Update player's health only if an attack occurred
            player_health -= actualdmg

        print(f"The {enemy_name} has {enemy_health} health left!")
        print(f"You have {player_health} health left!")

while alive and player_health > 0:
    if advancing == 0:
        fight()
        set_goblin()
        if player_level >= 5:
            advancinginput = input("Would you like to advance to the next area?:")
            print_values()
            if advancinginput[0].lower() == 'y':
                advancing = 1
                set_skeleton()
            elif advancinginput[0].lower() == 'n':
                advancing = 0
    if advancing == 1:
        fight()

# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")
