import random
import math



# Patch Notes - Version 9.01, Forgot to add shop into the game



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

if class_input[0].lower() == 'c':
    print("You have selected the Commoner")
    crit_chance = 10
    dodge_chance = 10
    player_health = 40
    min_sword_dmg = 12
    max_sword_dmg = 18
    # ?
    StrengthRingOwned = False
    StrengthRingDamage = 2
    StrengthRingCost = 15

    HealingPotionAmount = 0
    HealingPotionCost = 7
    HealingPotionHealth = 20
elif class_input[0].lower() == 'g':
    print("You have selected the Glass Cannon")
    crit_chance = 8
    dodge_chance = 12
    player_health = 30
    min_sword_dmg = 14
    max_sword_dmg = 16
    # ?
    StrengthRingOwned = False
    StrengthRingDamage = 2
    StrengthRingCost = 15

    HealingPotionAmount = 0
    HealingPotionCost = 7
    HealingPotionHealth = 20
elif class_input[0].lower() == 't':
    print("You have selected Tank")
    crit_chance = 12
    dodge_chance = 8
    player_health = 50
    min_sword_dmg = 8
    max_sword_dmg = 12
    # ?
    StrengthRingOwned = False
    StrengthRingDamage = 2
    StrengthRingCost = 15

    HealingPotionAmount = 0
    HealingPotionCost = 7
    HealingPotionHealth = 20
elif class_input.lower() == 'jack':
    print("Welcome Jack!")
    crit_chance = 10
    dodge_chance = 10
    player_health = 10000
    min_sword_dmg = 10000
    max_sword_dmg = 10000
    # ?
    StrengthRingOwned = False
    StrengthRingDamage = 2
    StrengthRingCost = 15

    HealingPotionAmount = 0
    HealingPotionCost = 7
    HealingPotionHealth = 20






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


# Starting goblin stats
enemy_name = "Goblin"
enemy_coins = random.randint(3, 6)
enemy_health = 40
enemy_attack_min = 3
enemy_attack_max = 8
exp = 20
# I LOVE BALANCING!!!!!!!!!!!!!
def set_goblin():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Goblin"
    enemy_coins = random.randint(3, 6)
    enemy_health = 40
    enemy_attack_min = 3
    enemy_attack_max = 8
    exp = 20

# Adjusted skeleton stats
def set_skeleton():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Skeleton"
    enemy_coins = random.randint(5, 8)
    enemy_health = 50
    enemy_attack_min = 7
    enemy_attack_max = 11
    exp = 40

# Adjusted dragon stats
def set_dragon():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dragon"
    enemy_coins = random.randint(15, 25)
    enemy_health = 80
    enemy_attack_min = 8
    enemy_attack_max = 15
    exp = 100

def openshop():
    global coins, player_health, player_maxhealth, min_sword_dmg, max_sword_dmg, StrengthRingOwned, HealingPotionAmount

    print("Welcome to my shop!")
    viewing = input("Would you like to enter?: ")

    if viewing[0].lower() == 'y':
        print("Here are the items.")
        print(f"Strength Ring, Will increase damage by {StrengthRingDamage}. Cost: {StrengthRingCost} coins.")
        print(f"Healing Potion, Will heal you for {HealingPotionHealth}. Cost: {HealingPotionCost} coins.")

        shopinp = input("What would you like to buy?: ")

        if shopinp[0].lower() == 's' and not StrengthRingOwned:
            if coins >= StrengthRingCost:
                print("Thank you for shopping!")
                StrengthRingOwned = True
                min_sword_dmg += StrengthRingDamage
                max_sword_dmg += StrengthRingDamage
                coins -= StrengthRingCost
                print(f"You now have {min_sword_dmg}-{max_sword_dmg} Damage!")
            else:
                print("You don't have enough coins to buy the Strength Ring.")

        elif shopinp[0].lower() == 'h':
            amount = input("How many Healing Potions would you like to buy?: ")

            if amount.isdigit() and int(amount) > 0:
                total_cost = int(amount) * HealingPotionCost

                if coins >= total_cost:
                    print("Thank you for shopping!")
                    HealingPotionAmount += int(amount)
                    coins -= total_cost
                    print(f"You now have {HealingPotionAmount} Healing Potions.")
                else:
                    print("You don't have enough coins to buy the specified number of Healing Potions.")
            else:
                print("Invalid input. Please enter a valid number greater than 0 for the Healing Potion quantity.")




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


def fight():
    global HealingPotionHealth, HealingPotionAmount, player_level, player_name, player_health, enemy_health, enemy_attack_max, enemy_attack_min, enemy_name, alive, coins, xp_gained, crit_chance, dodge_chance

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
        elif enemy_attack.lower().startswith('h'):
            if HealingPotionAmount > 0:

                print("You have chosen to heal!")
                print(f"You have healed for: {HealingPotionHealth}")
                player_health += HealingPotionAmount
                HealingPotionAmount =- 1
                input(f"You now have {HealingPotionAmount}")
                pass

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
        if player_level >= 3:
            going_up = input("Would you like to level up?: ")

            if going_up.lower().startswith('y'):
                advance = 1
                openshop()
    elif advance == 1:
        set_skeleton()
        fight()
        if player_level >= 5:
            going_up1 = input("Would you like to level up?: ")
            if going_up1.lower().startswith('y'):
                advance = 2
                openshop()
    elif advance == 2:
        set_dragon()
        fight()

# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")
