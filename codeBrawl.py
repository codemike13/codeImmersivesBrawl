import subprocess
import random
import time
import sys
from termcolor import colored
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format


class codeImmersivesBrawl():
    def __init__(self):
        # self.stats = {'health': 100, "damage": 100, "weapon": "1 Stack"}
        self.weapons = [{
            'name': "Tire Iron",
            'damage': 15,
            'chance': 4
        }, {
            'name': "Bag of Rocks",
            'damage': 5,
            'chance': 3
        }, {
            'name': "Rotten Flopping Fish",
            'damage': 40,
            'chance': 10
        }, {
            'name': "Halberd",
            'damage': 20,
            'chance': 6
        }, {
            'name': "Tronald Dump",
            'damage': 5,
            'chance': 1
        }, {
            'name': "Flock of Pidgeons",
            'damage': 30,
            'chance': 10
        }]

        self.gladiators = [
            {
                'name': "Daniel The Destroyer",
                'health': 100,
                "damage": 20,
                "chance": 7,
                "weapon": "Battle Axe"
            },
            {
                'name': "Xiao the Blade Maiden",
                'health': 100,
                "damage": 10,
                "chance": 5,
                "weapon": "Karambit Knives"
            },
            {
                'name': "Hector Buck Shot Blaster",
                'health': 100,
                "damage": 30,
                "chance": 10,
                "weapon": "Shot Gun"
            },
            {
                'name': "Andrea Hidden Hands",
                'health': 100,
                "damage": 7,
                "chance": 4,
                "weapon": "ButterFly Knife"
            },
            {
                'name': "Javelin John",
                'health': 100,
                "damage": 40,
                "chance": 12,
                "weapon": "Javelin"
            },
            {
                'name': "Sung the Gunslinger",
                'health': 100,
                "damage": 10,
                "chance": 3,
                "weapon": "Colt 45"
            },
            {
                'name': "David Double Fist",
                'health': 100,
                "damage": 35,
                "chance": 15,
                "weapon": "Electric Brass Knuckles"
            },
            {
                'name': "Rashaan the Wretched ",
                'health': 100,
                "damage": 5,
                "chance": 1,
                "weapon": "Flame Thrower"
            },
            {
                'name': "Nikolay the NightShade",
                'health': 100,
                "damage": 15,
                "chance": 4,
                "weapon": "Whispering Needles"
            },
            {
                'name': "Rainer the Razor",
                'health': 100,
                "damage": 15,
                "chance": 4,
                "weapon": "Karambit Knives"
            },
        ]

    def startBattle(self):

        # print("\n\n\n\n                    Ohh Sna[p  ..... . .. . . .. A  \n")
        # time.sleep(2)
        # self.clear()
        # cmd = [
        #     "figlet -w 120 -f cybersmall 'WORMHOLE'",
        #     "figlet -w 120 -f cybermedium 'WORMHOLE'",
        #     "figlet -w 120 -f cyberlarge 'WORMHOLE'",
        #     "figlet -w 120 -f cyberlarge 'WORMHOLE'",
        #     "figlet -w 120 -f cyberlarge 'WORMHOLE'",
        #     "figlet -w 120 -f cyberlarge 'WORMHOLE'",
        #     "figlet -w 120 -f cybermedium 'WORMHOLE'",
        #     "figlet -w 120 -f cybersmall 'WORMHOLE'",
        # ]

        # for i in cmd:
        #     print('\n\n\n\n ')
        #     wormhole = subprocess.call(i, shell=True)
        #     time.sleep(.5)
        #     self.clear()
        # print(
        #     " \n\n\n\n                 .........Our Python class got suckedddddd iiiiiNNNNNNNN........."
        # )
        # time.sleep(2)
        # self.clear()

        # print(
        #     "\n\n\n\n                                    And TheeeeennnNNNNN ")
        # time.sleep(2)
        # self.clear()
        # intro = [
        #     "figlet -w 120 -f cyberlarge 'Cuh'",
        #     "figlet -w 120 -f cyberlarge 'Cuh Cuh'",
        #     'figlet -w 120 -f cyberlarge "Cuh Cuh Cuh "',
        #     'figlet -w 200 -f cybermedium "!! CODE IMMERSIVES BRAWL !!"'
        # ]
        # for i in intro:
        #     print('\n\n\n\n ')
        #     wormhole = subprocess.call(i, shell=True)
        #     time.sleep(.4)
        #     self.clear()

        # print('\n\n\n\n ')
        # end = subprocess.call(
        #     'figlet -w 200 -f cybermedium "!! CODE IMMERSIVES BRAWL !!"',
        #     shell=True)
        # time.sleep(2)
        # self.clear()

        count = 0
        for name in range(len(self.gladiators)):
            print(count, self.gladiators[name]['name'])
            count += 1
        gladiator = int(input("\nChoose your Gladiator ! : "))
        self.clear()
        champion = self.gladiators[gladiator]

        print(
            " Your Champion : {}\n -------------------\n Health: {} \n Damage : {} \n chance: {}\n Weapon : {}"
            .format(champion['name'], champion['health'], champion['damage'],
                    champion['chance'], champion['weapon']))
        time.sleep(3)
        self.clear()
        print("The Veteran gladiator ", colored('THOO', 'yellow'))
        time.sleep(1)
        print(
            "Has graced your champion 20 gold to use for battle costs, spend it wisely ...."
        )
        time.sleep(3)
        champion['loot'] = 20
        self.clear()
        battleStart = True
        while battleStart:
            print(champion['name'],
                  "the Gladiator has been cast into Battle!!")
            print("==============================\n")
            # time.sleep(.5)
            try:
                print(
                    "Prepare for Combat:\n=================\n 1 --> Armory\n 2 --> Sick Bay\n 3 --> Battle \n 4 --> Loot \n=================\nChoose wisely: ",
                    end="")

                choice = int(input(""))
            except:
                print("Not a choice Gladiator")
                time.sleep(1.3)
                self.clear()
            else:
                if choice == 1:
                    self.armory(champion)
                if choice == 2:
                    self.sickBay(champion)
                if choice == 3:
                    self.battle(champion)
                if choice == 4:
                    self.loot(champion)
                if choice == 5:
                    self.quit()

    def armory(self, champion):
        weapons = self.weapons
        self.spinner()
        self.clear()

        choice = -1
        while choice < 0 or choice > len(weapons):

            self.clear()
            print("--== WELCOME to ELVIS Arms ==--")
            print("Current weapon is : ", champion['weapon'], '\n')
            print(
                "You can select a new weapon for your Champion here in the armory"
            )
            print(
                '-----------------------------------------------------------------\n'
            )
            try:
                for i in range(len(weapons)):
                    name = colored(weapons[i]['name'], 'red')
                    print(i, " --> [[[ ", name, " ]]], Damage: ",
                          weapons[i]['damage'], ", Crit Chance: ",
                          weapons[i]['chance'])
                choice = int(input("\nSelection :"))
            except:
                print("Not an option Gladiator")
                time.sleep(1)
            else:
                champion['weapon'] = weapons[choice]['name']
                champion['damage'] = weapons[choice]['damage']
                champion['chance'] = weapons[choice]['chance']
                print(champion['name'], ' weapon has been changed to : ',
                      colored(weapons[choice]['name'], 'red'))
                time.sleep(2)
                self.clear()

    def loot(self, champion):
        self.spinner()
        self.clear()
        print("Your Gladiator has : ", champion['loot'],
              ' gold for battle expenses.')
        time.sleep(2)

    def sickBay(self, champion):
        health = champion['health']
        potions = [
            {
                'name': 'Big potion',
                'heal': 50,
                'cost': 20
            },
            {
                'name': 'Medium potion',
                'heal': 25,
                'cost': 12
            },
            {
                'name': 'Small potion',
                'heal': 10,
                'cost': 5
            },
        ]
        self.spinner()
        self.clear()
        choice = -1
        brokeAF = False

        while choice < 0 or choice > 2 or brokeAF:
            self.clear()
            print("--== WELCOME to Antonio's Apothecary ==--")
            print("Current Health: ", champion['health'])
            print(
                "Feeling woozy from too many head smacks? Or maybe your guts are hanging out.. Buy potions here to heal\n"
            )
            print(
                '-----------------------------------------------------------------\n'
            )
            try:
                for i in range(len(potions)):
                    print(i, ' --> ', potions[i]['name'], 'heals',
                          potions[i]['heal'], 'pts , cost : ',
                          potions[i]['cost'])
                print("3 --> Back to Barracks")
                choice = int(input("\nChoose your healing potion : "))
                if choice == 3:
                    print("Go with the battle Gods Gladiator")
                    time.sleep(1)
                    self.clear()
                    break
            except:
                print("Not on the list Gladiator")
                time.sleep(.5)

            if champion['loot'] - potions[choice]['cost'] < 0:
                brokeAF = True
                goldNeeded = champion['loot'] - potions[choice]['cost']
                print(
                    "You need", goldNeeded,
                    "more gold Gladiator kick rocks, or stay and buy a cheaper potion."
                )
                time.sleep(1.8)

            else:
                brokeAF = False
                champion['health'] += potions[choice]['heal']
                champion['loot'] -= potions[choice]['cost']
                print("Your champions Health is now : ", champion['health'])
                time.sleep(1)
                print("You now have", champion['loot'],
                      'gold left for battle expenses.')
                time.sleep(2)
                self.clear()

    def clear(self):
        clear = subprocess.call('clear', shell=True)

    def spinner(self):
        animation = "|/-\\"

        for i in range(12):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()

    def battle(self, champion):
        opponent = self.gladiators[random.randrange(8)] if self.gladiators[
            random.randrange(8)] != champion else self.gladiators[
                random.randrange(8)]
        fighting = True
        print('Your Opponent is :', opponent['name'])
        time.sleep(1.5)
        print('Prepare to attack!')

        hits = [
            "Thwomped", "Buttered", "Mangled", "Slapped", "Licked", "Stomped"
        ]
        while fighting:
            if champion['health'] <= 0 or opponent['health'] <= 0:
                if champion['health'] <= 0:
                    print("Your champion", champion['name'],
                          'has fallen in Battle!')
                    time.sleep(1)
                    fighting = False

                if opponent['health']:
                    print("Your champion has defeated", opponent['name'],
                          'In Battle!')
                    time.sleep(3)
                    fighting = False

            block = 5
            oppBlock = random.randint(0, 2)
            champBlock = random.randint(0, 2)
            turn = random.randint(0, 2)
            champDeath = 'red' if champion['health'] < 30 else 'yellow'
            oppDeath = 'red' if opponent['health'] < 30 else 'yellow'
            champHealth = 'green' if champion['health'] > 70 else champDeath
            oppHealth = 'green' if opponent['health'] > 70 else oppDeath

            self.clear()
            self.clear()
            print('\n')
            print(champion['name'], '\n Health: ',
                  colored(champion['health'], champHealth))
            print(
                colored('=' * int((champion['health'] * 2) / 10), champHealth))
            print(opponent['name'], '\n Health: ',
                  colored(opponent['health'], oppHealth))
            print(colored('=' * int((opponent['health'] * 2) / 10), oppHealth))
            print('\n--------------------------------')
            print("[[[[[(((    YOUR MOVE    )))]]]]]]")
            print('--------------------------------\n')
            print('1 --> Attack')
            print('2 --> Heal7')
            print('3 --> Surrender')
            if turn == 0:
                try:
                    choice = int(input("Your Move: "))
                except:
                    print("Not an option Gladiator get back in the fight!")
                    time.sleep(1.5)
                    self.clear()
                else:
                    if choice == 1:
                        if oppBlock == 1:
                            opponent['health'] -= champion['damage']
                            opponent['health'] += block
                            print("Your Opponent", colored('BLOCKED', 'red'),
                                  "took reduced damage")
                            time.sleep(1)
                            print(champion['name'], "Hit", opponent['name'],
                                  " for",
                                  colored(champion['damage'] - block,
                                          'green'), 'health points!.')
                            time.sleep(2)
                            turn = 1
                            self.clear()
                        else:
                            opponent['health'] -= champion['damage']
                            print(
                                "Your Opponent was ((",
                                colored(hits[random.randrange(len(hits))],
                                        'yellow'), ")) with your",
                                champion['weapon'])
                            time.sleep(1)
                            print(champion['name'], "Hit", opponent['name'],
                                  "for", colored(champion['damage'],
                                                 'green'), 'health points!.')
                            time.sleep(2)
                            self.clear()
                    if choice == 2:
                        if champBlock == 1:
                            print("Preparing to block reduced damage")
                            time.sleep(2)
                            self.clear()
                        else:
                            print("Cant BLOCK OHHH FU** !!!")
                            time.sleep(2)
                            self.clear()
                    if choice == 3:
                        print(
                            "Its off to the Guillitine , TWO GO IN ONE COMES OUT MUAHAHAHAHAH take them back to the WORMHOLE"
                        )
                        time.sleep(1.5)
                        fighting = False
                        self.clear()

            if turn == 1:
                self.clear()
                print('\n')
                print(champion['name'], '\n Health: ',
                      colored(champion['health'], champHealth))
                print(
                    colored('=' * int((champion['health'] * 2) / 10),
                            champHealth))
                print(opponent['name'], '\n Health: ',
                      colored(opponent['health'], oppHealth))
                print(
                    colored('=' * int((opponent['health'] * 2) / 10),
                            oppHealth))

                print('\n--------------------------------')
                print("[[[[[((( ENEMY ATTACKS )))]]]]]]")
                print('--------------------------------\n')

                if champBlock == 1:
                    champion['health'] -= opponent['damage']
                    champion['health'] += block
                    print("You ", colored('BLOCKED', 'red'),
                          "took reduced damage")
                    time.sleep(1)
                    print(opponent['name'], "Hit you for",
                          colored(opponent['damage'] - block, 'green'),
                          'health points!.')
                    time.sleep(3)
                    turn = 0
                    self.clear()
                else:
                    champion['health'] -= opponent['damage']
                    print("You got ((",
                          colored(hits[random.randrange(len(hits))], 'yellow'),
                          ")) with a ", opponent['weapon'])
                    time.sleep(1)
                    print(opponent['name'], "Hit you for",
                          colored(opponent['damage'], 'green'),
                          'health points!.')
                    time.sleep(3)
                    self.clear()


mike = codeImmersivesBrawl()

print(mike.startBattle())
