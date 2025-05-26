import os
import time
import random

card=0
anim=""
loop=True
menu=True
anim=("")
rarity=("")
pokedex=[]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
noinput=("")
#reminder= gold is only one card
golden=("")
fullart = []
legendary = []
very_rare = []
rare = []
uncommon = []
common = []

golden1=[]
fullart1 = []
legendary1 = []
very_rare1 = []
rare1 = []
uncommon1 = []
common1 = []

packet=input("""    
█████████████████████████████████████████
███                                   ███
███     -TCG Python Version 1.0.2-    ███
███                                   ███
███                                   ███
███         [ENTER] to START          ███
███                                   ███
█████████████████████████████████████████""")
clear()
time.sleep(0.5)
menu=True
while loop == True:
    clear()
    print("██L██L██L██L██L██L      ████████████████ ")
    print("██L██L██L██L██L██L      ███ ████████████████")
    print("██████████████████      ███       █████████████ ")
    print("██              ██      ███           ████████████")
    print("██              ██      ███                      ██ ")
    print("██     (-0-)    ██      ███                      ██")
    print("██   TCG PACKET ██      ███                      ██ ")
    print("██   Vol.  ?    ██      ███       Pokedex        ██ ")
    print("██              ██      ███         (-0-)        ██ ")
    print("██  popular151  ██      ███                      ██")
    print("██              ██      ███                      ██")
    print("██████████████████      ███                      ██")
    print("██████████████████      ███████████████████████████ ")
    print("")
    packet=input(""" Type out what you want to do.

    1 (number only): Packet
    2 (number only): Pokedex
                  
    (If there is no input packets will be automatically selected): """)
    if packet == "2":
        clear()
        time.sleep(0.5)
        print("--Pokedex--")
        print("")
        if not pokedex:
            print("You have no Pokemon!")
            print("Open packs to fill up the Pokedex!")
        else:
            print("Popular 151:")
            print("")
            for i in pokedex:
                golden = ["Pikachu(GOLD)"]
                fullart = ["Pikachu","Pidgey","Mew",
                        "Rapidash","Bulbasaur","Charmander",
                        "Mr Mime", "Gyrados","Exeguttor"]
                
                legendary = [
                    "Articuno", "Zapdos", "Moltres", 
                    "Mewtwo", "Mew"
                ]
                very_rare = [
                    "Charizard", "Venusaur", "Blastoise", 
                    "Alakazam", "Gengar", "Gyarados", 
                    "Dragonite", "Nidoqueen", "Nidoking", 
                    "Machamp", "Exeggutor", "Arcanine"
                ]
                rare = [
                    "Tauros", "Lapras", "Scyther", 
                    "Porygon", "Jynx", "Electabuzz", 
                    "Farfetch'd", "Mr. Mime", "Aerodactyl", 
                    "Hitmonlee", "Hitmonchan", "Chansey", 
                    "Tangela", "Kangaskhan", "Pinsir"
                ]
                uncommon = [
                    "Butterfree", "Beedrill", "Pidgeot", 
                    "Raichu", "Sandslash", "Clefable", 
                    "Vileplume", "Victreebel", "Poliwrath", 
                    "Golem", "Rapidash", "Slowbro", 
                    "Magneton", "Dewgong", "Muk", 
                    "Cloyster", "Hypno", "Weezing", 
                    "Rhydon", "Seadra", "Starmie"
                ]
                common = [
                    "Pidgey", "Rattata", "Spearow", 
                    "Caterpie", "Weedle", "Zubat", 
                    "Magikarp", "Pikachu", "Geodude", 
                    "Oddish", "Bellsprout", "Paras", 
                    "Venonat", "Diglett", "Meowth", 
                    "Psyduck", "Poliwag", "Machop", 
                    "Tentacool", "Gastly", "Krabby", 
                    "Horsea", "Goldeen", "Staryu", 
                    "Doduo", "Shellder", "Drowzee", 
                    "Voltorb", "Koffing", "Rhyhorn"
                ]
                if i in golden:
                    if i not in golden1:
                        golden1.append(i)
                elif i in fullart:
                    if i not in fullart1:
                        fullart1.append(i)
                elif i in legendary:
                    if i not in legendary1:
                        legendary1.append(i)
                elif i in very_rare:
                    if i not in very_rare1:
                        very_rare1.append(i)
                elif i in rare:
                    if i not in very_rare1:
                        very_rare1.append(i)
                elif i in common:
                    if i not in common1:
                        common1.append(i)
            print("Gold (★):")
            print(golden1)
            print("Legendary (☆☆):")
            print(legendary1)
            print("Full Art (☆): ")
            print(fullart1)
            print("Very Rare (✦✦✦): ")
            print(very_rare1)
            print("Rare (✦✦):")
            print(rare1)
            print("Common (✦):")
            print(common1)
        print("")
        noinput=input("(1/2) Press Enter to See Next Page:")
        clear()
        time.sleep(0.5)
        golden1=[]
        fullart1 = []
        legendary1 = []
        very_rare1 = []
        rare1 = []
        uncommon1 = []
        common1 = []
        if not pokedex:
            print("You have no Pokemon!")
            print("Open packs to fill up the Pokedex!")
        else:
            print("Ultimtate Revelry:")
            print("")
            for i in pokedex:
                golden=("Celebi (GOLD)")
                fullart = [  
            "Meganium", "Typhlosion", "Feraligatr", "Lugia", "Ho-Oh",  
            "Raikou", "Entei", "Suicune", "Celebi", "Tyranitar",  
            "Steelix", "Scizor", "Ampharos", "Kingdra", "Blissey"  
            ]  
                legendary = [  
                    "Raikou", "Entei", "Suicune", "Lugia", "Ho-Oh", "Celebi"  
                ]  
                very_rare = [  
                    "Tyranitar", "Dragonite", "Snorlax", "Heracross", "Skarmory",  
                    "Houndoom", "Ursaring", "Donphan", "Miltank", "Porygon2"  
                ] 
                rare = [  
                    "Crobat", "Politoed", "Espeon", "Umbreon", "Slowking",  
                    "Forretress", "Granbull", "Mantine", "Piloswine", "Octillery",  
                    "Hitmontop", "Jumpluff", "Sudowoodo", "Girafarig", "Azumarill"  
                ]  
                uncommon = [  
                    "Furret", "Noctowl", "Ledian", "Ariados", "Xatu",  
                    "Bellossom", "Quagsire", "Wobbuffet", "Sunflora", "Magcargo",  
                    "Corsola", "Delibird", "Stantler", "Smeargle"  
                ]  
                common = [  
                    "Sentret", "Hoothoot", "Ledyba", "Spinarak", "Chinchou",  
                    "Pichu", "Cleffa", "Igglybuff", "Togepi", "Natu",  
                    "Mareep", "Marill", "Hoppip", "Sunkern", "Wooper",  
                    "Yanma", "Pineco", "Dunsparce", "Snubbull", "Slugma",  
                    "Swinub", "Remoraid", "Houndour", "Phanpy", "Tyrogue",  
                    "Smoochum", "Elekid", "Magby", "Larvitar"  
                ]  
                if i in golden:
                    if i not in golden1:
                        golden1.append(i)
                elif i in fullart:
                    if i not in fullart1:
                        fullart1.append(i)
                elif i in legendary:
                    if i not in legendary1:
                        legendary1.append(i)
                elif i in very_rare:
                    if i not in very_rare1:
                        very_rare1.append(i)
                elif i in rare:
                    if i not in very_rare1:
                        very_rare1.append(i)
                elif i in common:
                    if i not in common1:
                        common1.append(i)
            print("Gold (★):")
            print(golden1)
            print("Legendary (☆☆):")
            print(legendary1)
            print("Full Art (☆): ")
            print(fullart1)
            print("Very Rare (✦✦✦): ")
            print(very_rare1)
            print("Rare (✦✦):")
            print(rare1)
            print("Common (✦):")
            print(common1)
                
        
        print("")
        noinput=input("(2/2) Press Enter to Exit Pokedex")
    else:
        clear()
        time.sleep(0.5)
        card=input("""Choose 1 packet by their corresponding number(with number keys):

        Volume 1:                Volume 2:               Volume 3:   
        1. popular151 -0-        4. ???                  7. ???
        2. ultimate revelry '✦'  5. ???                  8. ???
        3. ???                   6. ???                  9. ???
        
        ✦ Special Volume ✦
        ???
        
        
    invalid numbers will auto select [popular151]:""")
        
        #opening anim
        if card == "1" or card != "2":
            golden = ["Pikachu(GOLD)"]
            fullart = ["Pikachu","Pidgey","Mew",
                    "Rapidash","Bulbasaur","Charmander",
                    "Mr Mime", "Gyrados","Exeguttor"]
            
            legendary = [
                "Articuno", "Zapdos", "Moltres", 
                "Mewtwo", "Mew"
            ]
            very_rare = [
                "Charizard", "Venusaur", "Blastoise", 
                "Alakazam", "Gengar", "Gyarados", 
                "Dragonite", "Nidoqueen", "Nidoking", 
                "Machamp", "Exeggutor", "Arcanine"
            ]
            rare = [
                "Tauros", "Lapras", "Scyther", 
                "Porygon", "Jynx", "Electabuzz", 
                "Farfetch'd", "Mr. Mime", "Aerodactyl", 
                "Hitmonlee", "Hitmonchan", "Chansey", 
                "Tangela", "Kangaskhan", "Pinsir"
            ]
            uncommon = [
                "Butterfree", "Beedrill", "Pidgeot", 
                "Raichu", "Sandslash", "Clefable", 
                "Vileplume", "Victreebel", "Poliwrath", 
                "Golem", "Rapidash", "Slowbro", 
                "Magneton", "Dewgong", "Muk", 
                "Cloyster", "Hypno", "Weezing", 
                "Rhydon", "Seadra", "Starmie"
            ]
            common = [
                "Pidgey", "Rattata", "Spearow", 
                "Caterpie", "Weedle", "Zubat", 
                "Magikarp", "Pikachu", "Geodude", 
                "Oddish", "Bellsprout", "Paras", 
                "Venonat", "Diglett", "Meowth", 
                "Psyduck", "Poliwag", "Machop", 
                "Tentacool", "Gastly", "Krabby", 
                "Horsea", "Goldeen", "Staryu", 
                "Doduo", "Shellder", "Drowzee", 
                "Voltorb", "Koffing", "Rhyhorn"
            ]
            frames = [
        [
            "██L██L██L██L██L██L",
            "██L██L██L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██ ",
            "██L██L██L██L██L██L",
            "  L██L██L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L",
            "██L██L██L██L██L██L",
            "   ██L██L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L██",
            "██L██L██L██L██L██L",
            "     L██L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L██L",
            "  L██L██L██L██L██L",
            "      ██L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L██L██",
            "   ██L██L██L██L██L",
            "        L██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L██L██L",
            "     L██L██L██L██L",
            "         ██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "  L██L██L",
            "     L██L██L██L██L",
            "         ██L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "   ██L██L██",
            "     L██L██L██L██L",
            "           L██L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "██L██L",
            "██L██L██",
            "      ██L██L██",
            "        L██L██L██L",
            "              L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "      ██L██L██",
            "        L██L██L██L",
            "              L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "         ██L██",
            "            ██L██L",
            "              L██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "           L██L",
            "              L██L",
            "               ██L",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "              L██L",
            "               ██L",
            "                  ",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "               ██L",
            "                  ",
            "                  ",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ],
        [
            "                  ",
            "                  ",
            "                  ",
            "██████████████████",
            "██              ██",
            "██              ██",
            "██     (-0-)    ██",
            "██   TCG PACKET ██",
            "██   Vol. 1     ██",
            "██              ██",
            "██  popular151  ██",
            "██              ██",
            "██████████████████",
            "██████████████████"
        ]  
                    ]
        elif card == "2":
            golden=("Celebi (GOLD)")
            fullart = [  
        "Meganium", "Typhlosion", "Feraligatr", "Lugia", "Ho-Oh",  
        "Raikou", "Entei", "Suicune", "Celebi", "Tyranitar",  
        "Steelix", "Scizor", "Ampharos", "Kingdra", "Blissey"  
        ]  
            legendary = [  
                "Raikou", "Entei", "Suicune", "Lugia", "Ho-Oh", "Celebi"  
            ]  
            very_rare = [  
                "Tyranitar", "Dragonite", "Snorlax", "Heracross", "Skarmory",  
                "Houndoom", "Ursaring", "Donphan", "Miltank", "Porygon2"  
            ] 
            rare = [  
                "Crobat", "Politoed", "Espeon", "Umbreon", "Slowking",  
                "Forretress", "Granbull", "Mantine", "Piloswine", "Octillery",  
                "Hitmontop", "Jumpluff", "Sudowoodo", "Girafarig", "Azumarill"  
            ]  
            uncommon = [  
                "Furret", "Noctowl", "Ledian", "Ariados", "Xatu",  
                "Bellossom", "Quagsire", "Wobbuffet", "Sunflora", "Magcargo",  
                "Corsola", "Delibird", "Stantler", "Smeargle"  
            ]  
            common = [  
                "Sentret", "Hoothoot", "Ledyba", "Spinarak", "Chinchou",  
                "Pichu", "Cleffa", "Igglybuff", "Togepi", "Natu",  
                "Mareep", "Marill", "Hoppip", "Sunkern", "Wooper",  
                "Yanma", "Pineco", "Dunsparce", "Snubbull", "Slugma",  
                "Swinub", "Remoraid", "Houndour", "Phanpy", "Tyrogue",  
                "Smoochum", "Elekid", "Magby", "Larvitar"  
            ]  
            frames = [
        ["██L██L██L██L██L██L",
        "██L██L██L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],
        
        ["██ ",
        "██L██L██L██L██L██L",
        "  L██L██L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],
        
        ["██L",
        "██L██L██L██L██L██L",
        "   ██L██L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["██L██",
        "██L██L██L██L██L██L",
        "     L██L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["██L██L",
        "  L██L██L██L██L██L",
        "      ██L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["██L██L██",
        "   ██L██L██L██L██L",
        "        L██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["██L██L██L",
        "     L██L██L██L██L",
        "         ██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["  L██L██L",
        "     L██L██L██L██L",
        "         ██L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["   ██L██L██",
        "     L██L██L██L██L",
        "           L██L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["██L██L",
        "██L██L██",
        "      ██L██L██",
        "        L██L██L██L",
        "              L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["      ██L██L██",
        "        L██L██L██L",
        "              L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["         ██L██",
        "            ██L██L",
        "              L██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["           L██L",
        "              L██L",
        "               ██L",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["              L██L",
        "               ██L",
        "                  ",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["               ██L",
        "                  ",
        "                  ",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"],

        ["                  ",
        "                  ",
        "                  ",
        "██████████████████",
        "██              ██",
        "██              ██",
        "██    <'✦'>     ██",
        "██   TCG PACKET ██",
        "██   Vol. 1     ██",
        "██              ██",
        "██   ultimate   ██",
        "██   revelry    ██",
        "██████████████████",
        "██████████████████"]
                    ]

        for frame in frames:
            time.sleep(0.1)
            clear()
            for line in frame:
                print(line)

        #this applies to both anim
        clear()
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        print("████████████████████████████████████")
        time.sleep(0.5)
        clear()
        for i in range(5):
            rng=random.randint(1,100)
            if rng < 51:
                rcard = random.choice(common)
                rarity=("✦")
            else:
                rng=random.randint(1,100)
                if rng < 71:
                    rcard = random.choice(uncommon)
                    rarity=("✦✦")
                else:
                    rng=random.randint(1,100)
                    if rng < 71:
                        rcard = random.choice(very_rare)
                        anim=("vrare")
                        rarity=("✦✦✦")
                    else:
                        ng=random.randint(1,20)
                        if rng < 11:
                            rcard = random.choice(legendary)
                            anim=("legend")
                            rarity=("☆☆")
                        elif rng == 20:
                            rcard=golden
                            anim=("gold")
                            rarity=("★")
                        else:
                            rcard = random.choice(fullart)
                            anim=("fullart")
                            rarity=("☆") 
            if rcard in pokedex:
                print("")
            else:
                pokedex.append(rcard)
            if anim == ("vrare"):
                print("You got")
                time.sleep(0.5)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("███████  ███████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("███████  ███████")
                print("██████    ██████")
                print("███████  ███████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("███████  ███████")
                print("██████    ██████")
                print("█████      █████")
                print("██████    ██████")
                print("███████  ███████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("███████  ███████")
                print("██████    ██████")
                print("█████      █████")
                print("████        ████")
                print("█████      █████")
                print("██████    ██████")
                print("███████  ███████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("███████  ███████")
                print("██████    ██████")
                print("█████      █████")
                print("████        ████")
                print("███          ███")
                print("████        ████")
                print("█████      █████")
                print("██████    ██████")
                print("███████  ███████")
                time.sleep(0.2)
                clear()
                print("██████    ██████")
                print("█████      █████")
                print("████        ████")
                print("███          ███")
                print("██            ██")
                print("███          ███")
                print("████        ████")
                print("█████      █████")
                print("██████    ██████")
                time.sleep(0.2)
                clear()
                print("█████      █████")
                print("████        ████")
                print("███          ███")
                print("██            ██")
                print("█              █")
                print("██            ██")
                print("███          ███")
                print("████        ████")
                print("█████      █████")
                time.sleep(0.2)
                clear()
                print("█████      █████")
                print("████        ████")
                print("███          ███")
                print("██   SUPER    ██")
                print("█     RARE     █")
                print("██            ██")
                print("███          ███")
                print("████        ████")
                print("█████      █████")
                time.sleep(1)
                clear()
                print("█████      █████")
                print("████        ████")
                print("███          ███")
                print("█              █")
                print("   ", rcard)
                print("█      ✦✦✦     █")
                print("███          ███")
                print("████        ████")
                print("█████      █████")
                time.sleep(1)
                clear()
                print("You got", rcard)
                print("Rarity:", rarity)
            elif anim == ("legend"):
                print("You got")
                time.sleep(0.5)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("█     ████     █")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("       ██       ")
                print("████████████  ██")
                print("██      ████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("                ")
                print("████████████  ██")
                print("██      ████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("    Legendary   ")
                print("████████████  ██")
                print("██      ████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(1)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████   ☆  ██")
                print("██  ████████████")
                print("   ", rcard)
                print("████████████  ██")
                print("██   ☆  ████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(1)
                clear()
                print("You got", rcard)
                print("Rarity:", rarity)
            elif anim == ("fullart"):
                print("You got")
                time.sleep(0.5)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████████")
                print("████████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████  ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██   ███████████")
                print("██  ████████████")
                print("██  ████████████")
                print("██  ████████████")
                print("█     ████     █")
                print("████████████  ██")
                print("████████████  ██")
                print("███████████   ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("██   ███████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("       ██       ")
                print("████████████  ██")
                print("██      ████  ██")
                print("███████████   ██")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("███  ███████████")
                print("██   ███████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("                ")
                print("████████████  ██")
                print("██      ████  ██")
                print("███████████   ██")
                print("███████████  ███")
                time.sleep(0.2)
                clear()
                print("████          ██")
                print("██    ██████████")
                print("██  ████████████")
                print("██  ████      ██")
                print("██  ████████████")
                print("    Full Art   ")
                print("████████████  ██")
                print("██      ████  ██")
                print("██████████    ██")
                print("██          ████")
                time.sleep(1)
                clear()
                print("███           ██")
                print("██    ██████████")
                print("██  ████████████")
                print("██  ████  [☆] ██")
                print("██  fullart█████")
                print(" ", rcard)
                print("████████████  ██")
                print("██  [☆]  ███  ██")
                print("██████████    ██")
                print("██           ███")
            elif anim == ("golden"):
                print("You got")
                time.sleep(0.5)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("███████**███████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("████████████████")
                print("███████**███████")
                print("██████****██████")
                print("███████**███████")
                print("████████████████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("████████████████")
                print("███████**███████")
                print("██████****██████")
                print("█████******█████")
                print("██████****██████")
                print("███████**███████")
                print("████████████████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("████████████████")
                print("███████**███████")
                print("██████****██████")
                print("█████******█████")
                print("████********████")
                print("█████******█████")
                print("██████****██████")
                print("███████**███████")
                print("████████████████")
                time.sleep(0.2)
                clear()
                print("███████**███████")
                print("██████****██████")
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                print("██████****██████")
                print("███████**███████")
                time.sleep(0.2)
                clear()
                print("██████****██████")
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                print("██████****██████")
                time.sleep(0.2)
                clear()
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█**************█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█****GOLDEN****█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★★GOLDEN★★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(0.2)
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█****GOLDEN****█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★★GOLDEN★★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(0.2)
                clear()
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█****GOLDEN****█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★★GOLDEN★★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(0.2)
                clear()
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█***CONGRATS***█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★CONGRATS★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(0.2)
                clear()
                print("█████******█████")
                print("████********████")
                print("███**********███")
                print("██************██")
                print("█***CONGRATS***█")
                print("██************██")
                print("███**********███")
                print("████********████")
                print("█████******█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★CONGRATS★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(0.2)
                clear()
                print("█████★★★★★★█████")
                print("████★★★★★★★★████")
                print("███★★★★★★★★★★███")
                print("██★★★★★★★★★★★★██")
                print("█★★★★GOLDEN★★★★█")
                print("██★★★★★★★★★★★★██")
                print("███★★★★★★★★★★███")
                print("████★★★★★★★★████")
                print("█████★★★★★★█████")
                time.sleep(1)
                clear()
                print("You got", rcard)
                print("Rarity:", rarity)
            else:
                print("You got")
                time.sleep(0.5)
                clear()
                print("You got", rcard)
                print("Rarity:", rarity)
            if i < 4:
                nothing = input("Press [Enter] to see next card")
                anim=("")
                clear()
            elif i == 4:
                nothing=input("Press [Enter] to return to menu")
        clear()