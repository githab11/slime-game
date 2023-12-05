import random
import math
import time
from colorama import Fore, Style
import pickle








# Realm of Legends - Patch Notes - Version 1.5, New Shop Items!!

# - Added 2 New Shop Items!
# - Crit Scroll And Dodge Scroll!
# - Removed herobrine.



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
StrengthRingOwned = False
StrengthRingDamage = 2
StrengthRingCost = 15

HealingPotionAmount = 0
HealingPotionCost = 7
HealingPotionHealth = 20

from colorama import Fore, Style
min_damage_changer = 2
max_damage_changer = 2
player_health_changer = 10


def save_game():
    game_state = {
        'player_level': player_level,
        'player_xp': player_xp,
        'player_next_level_xp': player_next_level_xp,
        'player_health': player_health,
        'player_maxhealth': player_maxhealth,
        'min_sword_dmg': min_sword_dmg,
        'max_sword_dmg': max_sword_dmg,
        'additive_dmg': additive_dmg,
        'coins': coins,
        'alive': alive,
        'advancing': advancing,
        'StrengthRingOwned': StrengthRingOwned,
        'StrengthRingDamage': StrengthRingDamage,
        'StrengthRingCost': StrengthRingCost,
        'HealingPotionAmount': HealingPotionAmount,
        'HealingPotionCost': HealingPotionCost,
        'HealingPotionHealth': HealingPotionHealth,
        'CritScroll': CritScroll,
        'CritScrollChance': CritScrollChance,
        'CritScrollCost': CritScrollCost,
        'DodgeScrollOwned': DodgeScrollOwned,
        'DodgeScrollChance': DodgeScrollChance,
        'DodgeScrollCost': DodgeScrollCost,
        'achievements': achievements
    }

    with open('savegame.pkl', 'wb') as file:
        pickle.dump(game_state, file)
    print("Game saved successfully.")

# Function to load the game state
def load_game():
    global player_level, player_xp, player_next_level_xp, player_health, player_maxhealth, min_sword_dmg, max_sword_dmg, additive_dmg, coins, alive, advancing, StrengthRingOwned, StrengthRingDamage, StrengthRingCost, HealingPotionAmount, HealingPotionCost, HealingPotionHealth, CritScroll, CritScrollChance, CritScrollCost, DodgeScrollOwned, DodgeScrollChance, DodgeScrollCost, achievements

    try:
        with open('savegame.pkl', 'rb') as file:
            game_state = pickle.load(file)

        player_level = game_state['player_level']
        player_xp = game_state['player_xp']
        player_next_level_xp = game_state['player_next_level_xp']
        player_health = game_state['player_health']
        player_maxhealth = game_state['player_maxhealth']
        min_sword_dmg = game_state['min_sword_dmg']
        max_sword_dmg = game_state['max_sword_dmg']
        additive_dmg = game_state['additive_dmg']
        coins = game_state['coins']
        alive = game_state['alive']
        advancing = game_state['advancing']
        StrengthRingOwned = game_state['StrengthRingOwned']
        StrengthRingDamage = game_state['StrengthRingDamage']
        StrengthRingCost = game_state['StrengthRingCost']
        HealingPotionAmount = game_state['HealingPotionAmount']
        HealingPotionCost = game_state['HealingPotionCost']
        HealingPotionHealth = game_state['HealingPotionHealth']
        CritScroll = game_state['CritScroll']
        CritScrollChance = game_state['CritScrollChance']
        CritScrollCost = game_state['CritScrollCost']
        DodgeScrollOwned = game_state['DodgeScrollOwned']
        DodgeScrollChance = game_state['DodgeScrollChance']
        DodgeScrollCost = game_state['DodgeScrollCost']
        achievements = game_state['achievements']

        print("Game loaded successfully.")
    except FileNotFoundError:
        print("No saved game found.")




# Player stats
print(Fore.CYAN + "Welcome to Realm of Legends! Hopy you enjoy!")

player_name = input("What is your name?: ")
print(Fore.LIGHTCYAN_EX + "Here are the classes you can play!")
time.sleep(1)
print(Fore.LIGHTGREEN_EX + "Commoner, regular stats")
time.sleep(0.4)
print(Fore.BLUE + "Tank: More HP less damage")
time.sleep(0.4)
print(Fore.LIGHTWHITE_EX + "Glass Cannon, more damage less hp")
time.sleep(0.4)
class_input = input(Fore.RED + "What class would you like to play?: ")

if class_input[0].lower() == 'c':
    print(Fore.LIGHTGREEN_EX + "You have selected the Commoner")
    crit_chance = 10
    dodge_chance = 10
    player_health = 40
    min_sword_dmg = 10
    max_sword_dmg = 12

elif class_input[0].lower() == 'g':
    print(Fore.LIGHTWHITE_EX + "You have selected the Glass Cannon")
    crit_chance = 15
    dodge_chance = 5
    player_health = 35
    min_sword_dmg = 14
    max_sword_dmg = 15
    # ?

elif class_input[0].lower() == 't':
    print(Fore.BLUE + "You have selected Tank")
    crit_chance = 5
    dodge_chance = 15
    player_health = 50
    min_sword_dmg = 8
    max_sword_dmg = 12

elif class_input[0].lower() == ',':
    print(Fore.RED + "Welcome Jack!")
    crit_chance = 100
    dodge_chance = 100
    player_health = 10000
    min_sword_dmg = 10000
    max_sword_dmg = 10000


# Crit scroll
StrengthRingOwned = False
StrengthRingDamage = 2
StrengthRingCost = 15

HealingPotionAmount = 0
HealingPotionCost = 7
HealingPotionHealth = 20

CritScroll = False
CritScrollChance = 5
CritScrollCost = 50

DodgeScrollOwned = False
DodgeScrollChance = 5
DodgeScrollCost = 40






# Achievement system
achievements = {
    # Early Game
    'First Victory': False,
    'Goblin Slayer': False,
    'Damn Bandits!': False,
    # Mid Game
    'Skeleton Killer': False,
    'Game Win Get': False,
    'Survivor': False,
    # Late Game
    'Dragon Conqueror': False,
    'Firey Death Killer': False,
    'Strength Ring Get': False,
    'Master Swordsman': False,

}
def show_achievements():
    print(Fore.YELLOW + "Achievements:")
    for achievement, unlocked in achievements.items():
        status = "Unlocked" if unlocked else "Locked"
        print(Fore.RESET + f"{achievement}: {status}")

def unlock_achievement(achievement_name):
    if not achievements[achievement_name]:
        achievements[achievement_name] = True
        print(Fore.GREEN + f"Achievement Unlocked: {achievement_name}")
        show_achievements()

# el goblino
def set_goblin():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Goblin"
    enemy_coins = random.randint(3, 6)
    enemy_health = 50
    enemy_attack_min = 3
    enemy_attack_max = 8
    exp = 20
# el bandito
def set_bandit():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Bandit"
    enemy_coins = random.randint(3, 6)
    enemy_health = 60
    enemy_attack_min = 5
    enemy_attack_max = 10
    exp = 25



# Skeleton!
def set_skeleton():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Skeleton"
    enemy_coins = random.randint(5, 8)
    enemy_health = 50 + 10
    enemy_attack_min = 7
    enemy_attack_max = 11
    exp = 30

def set_skeleton_warrior():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Skeleton Warrior"
    enemy_coins = random.randint(6, 10)
    enemy_health = 50 + 10
    enemy_attack_min = 8
    enemy_attack_max = 12
    exp = 35

# New fire dragon!!
def set_fire_dragon():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Fire Dragon"
    enemy_coins = random.randint(20, 30)
    enemy_health = 85
    enemy_attack_min = 12
    enemy_attack_max = 16
    exp = 60

# Adjusted dragon stats
def set_dragon():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dragon"
    enemy_coins = random.randint(15, 25)
    enemy_health = 80
    enemy_attack_min = 10
    enemy_attack_max = 15
    exp = 50
def set_strong_dark_knight():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dark Knight"
    enemy_coins = random.randint(15, 20)
    enemy_health = 80
    enemy_attack_min = 18
    enemy_attack_max = 20
    exp = 80
def set_dark_knight():
    global enemy_name, enemy_coins, enemy_health, enemy_attack_min, enemy_attack_max, exp
    enemy_name = "Dark Knight"
    enemy_coins = random.randint(10, 15)
    enemy_health = 90
    enemy_attack_min = 15
    enemy_attack_max = 17
    exp = 50

def openshop():
    global coins, player_health, player_maxhealth, min_sword_dmg, max_sword_dmg, StrengthRingOwned, HealingPotionAmount, DodgeScrollOwned, dodge_chance, CritScroll, CritScrollCost, CritScrollChance, crit_chance
    save_game()
    print(Fore.YELLOW + "Welcome to my shop!")
    viewing = input(Fore.LIGHTCYAN_EX + "Would you like to enter?: ")

    if viewing[0].lower() == 'y':
        print(Fore.WHITE + "Here are the items.")
        print(Fore.YELLOW + f"You have {coins} coins!")
        print(Fore.LIGHTRED_EX + f"Strength Ring, Will increase damage by {StrengthRingDamage}. Cost: {StrengthRingCost} coins.")
        print(Fore.RED + f"Healing Potion, Will heal you for {HealingPotionHealth}. Cost: {HealingPotionCost} coins.")
        print(Fore.LIGHTYELLOW_EX + f"Dodge Scroll, Will increase dodge chance by {DodgeScrollChance}%. Cost: {DodgeScrollCost} coins.")
        print(Fore.LIGHTGREEN_EX + f"Crit Scroll, Will increase crit chance by {CritScrollChance}%. Cost {CritScrollCost} coins.")

        shopinp = input("What would you like to buy?: ")

        if shopinp[0].lower() == 's' and not StrengthRingOwned:
            if coins >= StrengthRingCost:
                print(Fore.CYAN + "Thank you for shopping!")
                StrengthRingOwned = True
                unlock_achievement('Strength Ring Get')
                min_sword_dmg += StrengthRingDamage
                max_sword_dmg += StrengthRingDamage
                coins -= StrengthRingCost
                print(Fore.RED + f"You now have {min_sword_dmg}-{max_sword_dmg} Damage!")
            else:
                print(Fore.LIGHTRED_EX + "You don't have enough coins to buy the Strength Ring.")
        elif shopinp[0].lower() == 'h':
            amount = input(Fore.RED + "How many Healing Potions would you like to buy?: ")

            if amount.isdigit() and int(amount) > 0:
                total_cost = int(amount) * HealingPotionCost

                if coins >= total_cost:
                    print(Fore.YELLOW + "Thank you for shopping!")
                    HealingPotionAmount += int(amount)
                    coins -= total_cost
                    print(Fore.RESET + f"You now have {HealingPotionAmount} Healing Potions.")
                else:
                    print(Fore.RESET + "You don't have enough coins to buy the specified number of Healing Potions.")
            else:
                print(Fore.RESET + "Invalid input. Please enter a valid number greater than 0 for the Healing Potion quantity.")

        elif shopinp[0].lower() == 'd' and not DodgeScrollOwned:
            if coins >= DodgeScrollCost:
                print(Fore.CYAN + "Thank you for shopping!")
                DodgeScrollOwned = True
                dodge_chance += DodgeScrollChance
                coins -= DodgeScrollCost
                print(Fore.LIGHTYELLOW_EX + f"You now have {dodge_chance}% Dodge Chance!")
            elif shopinp[0].lower() == 'c' and not CritScroll:
                if coins >= CritScrollCost:
                    print(Fore.LIGHTRED_EX + "Thank you for shopping!")
                    CritScroll = True
                    crit_chance += CritScrollChance
                    coins -= DodgeScrollCost
                    prin(Fore.LIGHTYELLOW_EX + f"You now have {crit_chance}% Crit Chance!")
                elif coins <= CritScrollChance:
                    print("You dont have enough coins!")

            else:
                print(Fore.LIGHTRED_EX + "You don't have enough coins to buy the Dodge Scroll.")

        elif shopinp[0].lower() == 'h':
            amount = input(Fore.RED + "How many Healing Potions would you like to buy?: ")

            if amount.isdigit() and int(amount) > 0:
                total_cost = int(amount) * HealingPotionCost

                if coins >= total_cost:
                    print(Fore.YELLOW + "Thank you for shopping!")
                    HealingPotionAmount += int(amount)
                    coins -= total_cost
                    print(Fore.RESET + f"You now have {HealingPotionAmount} Healing Potions.")
                else:
                    print(Fore.RESET + "You don't have enough coins to buy the specified number of Healing Potions.")
            else:
                print(Fore.RESET + "Invalid input. Please enter a valid number greater than 0 for the Healing Potion quantity.")




# Function to gain XP
def gain_xp(amount):
    global player_xp, player_level, player_next_level_xp, min_sword_dmg, max_sword_dmg, player_health, crit_chance, dodge_chance
    player_xp += amount
    print(Fore.CYAN + f"You have gained: {amount} XP!")
    print(Fore.CYAN + f"{player_xp}/{player_next_level_xp}")

    while player_xp >= player_next_level_xp:
        player_level += 1
        player_xp -= player_next_level_xp
        player_next_level_xp = math.floor(player_next_level_xp * 1.2)

        crit_chance += 1
        dodge_chance += 1

        # Additional enhancements at specific levels
        if player_level == 3:
            power_up_input = input(Fore.LIGHTRED_EX + f"You have reached level {player_level}!, would you like to increase your crit chance or your dodge chance?: ")
            if power_up_input.lower().startswith('c'):
                crit_chance += 1
            elif power_up_input.lower().startswith('d'):
                dodge_chance += 1

        valid_input = False
        while not valid_input:
            print(f"You're now level {player_level}")
            level_up_input = input(Fore.RED + f"Upgrade sword damage ({min_damage_changer}) or health ({player_health_changer})? : ")

            if level_up_input.lower().startswith('s'):
                min_sword_dmg += min_damage_changer
                max_sword_dmg += max_damage_changer
                print(Fore.RED + f"You have: {min_sword_dmg}-{max_sword_dmg} Damage!")
                valid_input = True
            elif level_up_input.lower().startswith('h'):
                player_health += player_health_changer
                player_maxhealth = player_health
                print(Fore.RED + f"You have: {player_health} Health!")
                valid_input = True
            else:
                print(Fore.RED + "Invalid input. Please enter 's' to upgrade sword damage or 'h' to upgrade health.")

        # Check for achievements when leveling up
        if player_level == 1:
            unlock_achievement('First Level')
        if player_level == 5:
            unlock_achievement('Master Swordsman')
        elif player_level == 10:
            unlock_achievement('Survivor')



def fight():
    global HealingPotionHealth, HealingPotionAmount, player_level, player_name, player_health, enemy_health, enemy_attack_max, enemy_attack_min, enemy_name, alive, coins, xp_gained, crit_chance, dodge_chance

    print(Fore.LIGHTMAGENTA_EX + f"You have encountered a {enemy_name}!")
    print(Fore.MAGENTA + f"You can heal if you have healing potions, you have {HealingPotionAmount}")
    print(Fore.LIGHTGREEN_EX + f"The {enemy_name} has {enemy_health} health and deals {enemy_attack_min} <-> {enemy_attack_max} damage!")

    while player_health > 0 and enemy_health > 0:
        enemy_attack = input(Fore.LIGHTGREEN_EX + f"Would you like to attack the {enemy_name}?: ")

        if enemy_attack.lower().startswith('y'):
            enemy_dodge = random.randint(1, 10)
            enemy_crit = random.randint(1, 10)

            plr_actual_dmg = random.randint(min_sword_dmg, max_sword_dmg)

            # Check player's dodge chance
            if enemy_dodge == 1:
                print(Fore.BLACK + f"The {enemy_name} has dodged!")
            else:
                # Check player's crit chance
                if random.randint(1, 100) <= crit_chance:
                    plr_actual_dmg *= 1.5
                    print(Fore.MAGENTA + f"You've attacked {enemy_name} for: {plr_actual_dmg} With a CRIT!")
                elif random.randint(1, 100) <= dodge_chance:
                    print(Fore.BLUE +   f"You have Dodged!")
                else:
                    print(Fore.RED + f"You've attacked {enemy_name} for: {plr_actual_dmg}")

                # Update enemy's health
                enemy_health -= plr_actual_dmg

            if enemy_health <= 0:
                print(Fore.LIGHTBLUE_EX + f"The {enemy_name} has been defeated!")
                print(Fore.LIGHTMAGENTA_EX + f"You have been healed to: {player_maxhealth}!")
                player_health = player_maxhealth
                coins += enemy_coins
                print(Fore.YELLOW + f"The {enemy_name} has dropped {enemy_coins} coins, you now have {coins} coins!")
                save_game()

                xp_gained = exp
                gain_xp(xp_gained)

                # Check for achievements when defeating an enemy
                if not achievements['First Victory']:
                    unlock_achievement('First Victory')
                if enemy_name == 'Goblin':
                    unlock_achievement('Goblin Slayer')
                elif enemy_name == 'Bandit':
                    unlock_achievement('Damn Bandits!')
                elif enemy_name == 'Dragon':
                    unlock_achievement('Dragon Conqueror')
                elif enemy_name == 'Fire Dragon':
                    unlock_achievement("Firey Death Killer")
                elif enemy_name == 'Skeleton' or 'Skeleton Warrior':
                    unlock_achievement('Skeleton Killer')

        elif enemy_attack.lower().startswith('n'):
            running_chance = random.randint(1, 10)
            if running_chance == 9:
                print(Fore.BLACK + "You have failed to run away!")
                actual_dmg = random.randint(enemy_attack_min, enemy_attack_max)
                print(Fore.LIGHTRED_EX + f"The {enemy_name} has attacked you for: {actual_dmg}")
            else:
                print(Fore.LIGHTWHITE_EX + "You have run away from the enemy!")
                print(Fore.RED + f"You have been healed for {player_maxhealth}!")
                player_health = player_maxhealth
                break  # End the fight
        elif enemy_attack.lower().startswith('h'):
            if HealingPotionAmount > 0:
                print("You have chosen to heal!")
                print(f"You have healed for: {HealingPotionHealth}")
                player_health += HealingPotionHealth
                HealingPotionAmount -= 1
                print(f"You now have {HealingPotionAmount} Healing Potions.")

        # Update player's health
        if random.randint(1, 100) > dodge_chance:
            actual_dmg = random.randint(enemy_attack_min, enemy_attack_max)

            # Check player's dodge chance
            if random.randint(1, 100) <= dodge_chance:
                print(Fore.BLACK + f"{player_name} has dodged!")
            else:
                print(Fore.LIGHTRED_EX + f"The {enemy_name} has attacked you for: {actual_dmg}")

                # Update player's health
                player_health -= actual_dmg

        print(Fore.RED + f"The {enemy_name} has {enemy_health} health left!")
        print(Fore.LIGHTRED_EX + f"You have {player_health} health left!")





# Game loop, had to rewrite this
advance = 0

while player_health > 0:
    if advance == 0:
        walking1 = random.randint(1, 5)
        if walking1 <= 4:
            goblinbandit = random.randint(1, 4)
            if goblinbandit != 4:
                set_goblin()
                fight()
            elif goblinbandit == 4:
                set_bandit()
                fight()
        elif walking1 == 5:
            openshop()

        if player_level >= 3 and not advance:
            going_up = input(Fore.MAGENTA + "Would you like to level up?: ")
            if going_up.lower().startswith('y'):
                advance = 1

    elif advance == 1:
        walking2 = random.randint(1, 5)
        if walking2 <= 4:
            skeleton_or_warrior = random.randint(1, 4)
            if skeleton_or_warrior != 4:
                set_skeleton()
                fight()
            elif skeleton_or_warrior == 4:
                set_skeleton_warrior()
                fight()
        elif walking2 == 5:
            openshop()

        if player_level >= 5 and not advance:
            going_up1 = input(Fore.MAGENTA + "Would you like to level up?: ")
            if going_up1.lower().startswith('y'):
                advance = 2
                min_damage_changer = 3
                max_damage_changer = 3
                player_health_changer = 20

    elif advance == 2:
        walking3 = random.randint(1, 5)
        if walking3 <= 4:
            fireorregular = random.randint(1, 4)
            if fireorregular != 4:
                set_dragon()
                fight()
            elif fireorregular == 4:
                set_fire_dragon()
                fight()
        elif walking3 == 5:
            openshop()

        if player_level >= 10 and not advance:
            going_up2 = input(Fore.MAGENTA + "Would you like to level up?: ")
            if going_up2.lower().startswith('y'):
                advance = 3
            elif advance == 3:
                walking4 = random.randint(1, 5)
                if walking4 <= 4:
                    dark_knight_chance = random.randint(1, 4)
                    if dark_knight_chance != 4:
                        set_dark_knight()
                        fight()
                    elif dark_knight_chance == 4:
                        set_strong_dark_knight()
                        fight()
                elif walking4 == 5:
                    openshop()

    # Additional conditions for advancing beyond stage 2, if needed

# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")

if achievements['Dragon Conqueror'] and achievements['Firey Death Killer']:
    unlock_achievement('Game Win Get')







# Player has died, end the game
if player_health <= 0:
    print(f"{player_name} has been defeated. Game over.")

if achievements['Dragon Conqueror'] and achievements['Firey Death Killer']:

    unlock_achievement('Game Win Get')
