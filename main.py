import colorama
from colorama import Fore, Style, Back
import shelve
import platform
import subprocess
import random
import statistics
import datetime
import time
import sys
import keyboard

colorama.init(autoreset=True)

# Initialize username
username = "nil"
temp_sysraise = 0
currcol = "white"
credits = 10
user_biotext = "...write your bio..."
user_defcolor = Fore.WHITE

whitelist = ["quit", "help", "clear", "specs", "time", "solve", "cyoadv", "combine", "screensaver"]

color_map = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "black": Fore.BLACK,
    "lightred": Fore.LIGHTRED_EX,
    "lightgreen": Fore.LIGHTGREEN_EX,
    "lightblue": Fore.LIGHTBLUE_EX,
    "lightyellow": Fore.LIGHTYELLOW_EX,
    "lightcyan": Fore.LIGHTCYAN_EX,
    "lightmagenta": Fore.LIGHTMAGENTA_EX,
    "lightwhite": Fore.LIGHTWHITE_EX,
}


def mainloop():
    global username, temp_sysraise, currcol, whitelist, credits, user_biotext, user_defcolor
    com = ""

    iindex = 1

    nocreds = False
    
    ee_mcp_n = 0

    multip = 1

    icode = ""
    print(
        color_map[currcol] +
        f"Welcome to Maximas Mini!\nType help for help.\nAlso, you need 1 credit per command (this goes up, and you can type 'udo nocreds' to disable it.).\nTo get credits, type mon [number 1 to 3].\nIf credits reach zero, then a dice will be rolled for how many credits you get.\nYou can also type quit to quit.\nNote: Errors also take credits.\nThere is no oh-no-you-messed-up coin return system. (unless it is a bug)"
    )

    # Open the shelve database
    with shelve.open('user_data') as db:
        # Load username if it exists in the database
        if 'username' in db and 'bio' in db and 'defcol' in db:
            username = db['username']
            user_biotext = db['bio']
            currcol = color_map.keys[db['defcol']]

    credits = 10

    while com != "quit":

        if username == "morecreditsplease" and ee_mcp_n == 0:

            credits += 99999999
            ee_mcp_n = 1

        if credits > 0:

            try:
                if nocreds == False:
                    print(color_map['yellow'] + f"🪙  {credits} {color_map['magenta'] + f'✖️  {multip}'}")
                else:
                    credits = 999999999
                    multip = 1
                com = input(color_map[currcol] +
                            f"maximas mini v0.0.3c 957L | {datetime.datetime.now().date()} | {username} | > " +
                            color_map[currcol])
                credits -= 1 * multip
                multip += 1

            except KeyError:
                print(
                    Fore.RED +
                    f"🌸 maximas says: hey, that color is not available! (spec: invalid color ({currcol}, {color_map.get(first_arg, 'nil')}); raised by: udo)"
                )
                currcol = "white"
                continue
            temp_sysraise = 0
            if com.strip() == "":
                credits += 1
                multip -= 1
                continue

            args = com.split()
            init_arg = args[0]

            first_arg = args[1] if len(args) > 1 else ""
            sec_arg = args[2] if len(args) > 2 else ""
            tri_arg = args[3] if len(args) > 3 else ""
            firstelse_args = args[1:]
            else_args = args[2:] if len(args) > 2 else []

            if len(firstelse_args
                   ) == 0 and temp_sysraise != 1 and com not in whitelist:
                temp_sysraise = 1
                print(
                    Fore.RED +
                    f"🌸 maximas says: hey, you gave an improper input! (spec: no args given; raised by: {com})"
                )

            if init_arg == "do":
                try:
                    
                    iindex = int(first_arg)

                    if iindex > 100:
                        print(Fore.RED + "🌸 maximas says: too large repitition count!")
                        iindex = 1
                except Exception as e:
                    print(Fore.RED + f"🌸 maximas says: unexpected error: {e}")

            i = 0
            for i in range(iindex):
                i += 1
                

                if temp_sysraise == 1:
                    temp_sysraise = 0
                    continue

                elif init_arg == "mon":
                    try:
                        c = random.randint(1, 3)
                        if int(first_arg) == c:
                            credits += 5
                            print(
                                Fore.RED +
                                "🌸 maximas says: hey, you were lucky! (spec: u rich now; raised by: mon)"
                            )
                        else:
                            print(
                                Fore.RED +
                                f"🌸 maximas says: hey, you weren't lucky enough! (spec: u broke now {c}; raised by: mon)"
                            )
                    except ValueError:
                        print(
                            Fore.RED +
                            "🌸 maximas says: hey, you gave an improper input! (spec: invalid number; raised by: mon)"
                        )
                

                
                elif init_arg == "screensaver":
                    import os
                    try:
                        timei = 100000
                        total_time = timei

                        if platform.system() == "Windows":
                            os.system('cls')
                        else:
                            os.system('clear')
                        
                        txt = color_map[random.choice(['red', 'green','yellow', 'blue', 'magenta', "cyan", 'lightred', 'lightgreen','lightyellow', 'lightblue', 'lightmagenta', "lightcyan"])] + "█"
                        
                        start_time = time.time()
                        elapsed_time = 0
                        
                        while elapsed_time <= total_time:
                            if keyboard.is_pressed('tab'):  # Check if Enter key is pressed
                                print("Stopping...")
                                break
                            
                            

                            txt += color_map[random.choice(['red', 'green','yellow', 'blue', 'magenta', "cyan", 'lightred', 'lightgreen','lightyellow', 'lightblue', 'lightmagenta', "lightcyan"])] + "█"
                            print(txt)
                            time.sleep(0.001)
                            
                            elapsed_time = time.time() - start_time

                    except Exception as e:
                        print(color_map['red'] + f"🌸 maximas says: unexpected error as {e}")
                elif init_arg == "load":
                    xx = random.choice(list(color_map.keys()))
                    def print_progress_bar(i, timei, xx):
                        # Calculate block counts
                        total_blocks = 120
                        progress_blocks = round((i / timei) * total_blocks)
                        remaining_blocks = total_blocks - progress_blocks

                        # Construct the progress bar
                        bar = (
                            f"{Fore.BLACK + '█'}"
                            f"{color_map[xx] + ('█' * progress_blocks)}"
                            f"{Fore.WHITE + ('█' * remaining_blocks)}"
                            f"{Fore.BLACK + '█'}"
                        )
                        
                        # Print progress bar and remaining time on the same line
                        sys.stdout.write(f"\r{bar} {timei - i} ms remaining")
                        sys.stdout.flush()

                    try:
                        timei = int(first_arg)

                        total_time = timei  
                        for elapsed_time in range(0, total_time + 1):
                            print_progress_bar(elapsed_time, total_time, xx)
                            time.sleep(0.001)  
                        
                        # Print final state after the loop ends
                        print(f"\r{Fore.BLACK + '█' * 120} {Fore.GREEN + 'Complete!                   '}")

                    except Exception as e:
                        print(Fore.RED + f"🌸 maximas says: unexpected error as {e}")


                elif init_arg == "echo":
                    try:
                        tcolor = color_map.get(first_arg.lower(), Back.BLACK)
                        color = color_map.get(first_arg.lower(), Fore.WHITE)
                        if tcolor != color:
                            print(
                                Fore.RED +
                                f"🌸 maximas says: hey, that color is not available! (spec: invalid color ({first_arg.lower()}, {color_map.get(first_arg.lower(), 'nil')}); raised by: echo)"
                            )
                            continue
                        print((color_map[currcol] + "🌴 out: ") + color +
                            " ".join(else_args))
                    except KeyError:
                        print(
                            Fore.RED +
                            f"🌸 maximas says: hey, that color is not available! (spec: invalid color ({first_arg.lower()}); raised by: echo)"
                        )

                elif init_arg == "specs":
                    print(Fore.LIGHTGREEN_EX + "🪨  here are the available specs:")
                    print(Fore.LIGHTGREEN_EX + "  - platform.architecture(): " +
                        Fore.WHITE + str(platform.architecture()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.machine(): " +
                        Fore.WHITE + str(platform.machine()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.node(): " +
                        Fore.WHITE + str(platform.node()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.platform(): " +
                        Fore.WHITE + str(platform.platform()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.processor(): " +
                        Fore.WHITE + str(platform.processor()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.python_build(): " +
                        Fore.WHITE + str(platform.python_build()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.python_compiler(): " +
                        Fore.WHITE + str(platform.python_compiler()))
                    print(Fore.LIGHTGREEN_EX +
                        "  - platform.python_implementation(): " + Fore.WHITE +
                        str(platform.python_implementation()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.python_version(): " +
                        Fore.WHITE + str(platform.python_version()))
                    print(Fore.LIGHTGREEN_EX +
                        "  - platform.python_version_tuple(): " + Fore.WHITE +
                        str(platform.python_version_tuple()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.release(): " +
                        Fore.WHITE + str(platform.release()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.system(): " +
                        Fore.WHITE + str(platform.system()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.uname(): " +
                        Fore.WHITE + str(platform.uname()))
                    print(Fore.LIGHTGREEN_EX + "  - platform.version(): " +
                        Fore.WHITE + str(platform.version()))
                    
                elif init_arg == "eni":
                    def number_fact(number):
                        facts = {
                            1: "1 is the multiplicative identity, meaning any number multiplied by 1 remains unchanged.",
                            2: "2 is the smallest and only even prime number.",
                            3: "3 is the first odd prime number and the second Fibonacci number.",
                            4: "4 is the only number with the same number of letters as its value in English.",
                            5: "A starfish typically has 5 arms.",
                            6: "6 is the smallest perfect number, meaning it's equal to the sum of its divisors (1 + 2 + 3).",
                            7: "There are 7 continents in the world.",
                            8: "A byte consists of 8 bits in computing.",
                            9: "9 is the highest single-digit number and a square number (3 x 3).",
                            10: "10 is the basis of the decimal system, the most widely used number system in the world.",
                            11: "11 is the first palindromic prime number.",
                            12: "12 is the number of months in a year.",
                            13: "Friday the 13th is considered unlucky in many cultures.",
                            14: "14 is the number of lines in a sonnet.",
                            15: "15 is a triangular number, which is the sum of the numbers 1 through 5.",
                            16: "16 is the number of ounces in a pound.",
                            17: "17 is the age at which many countries allow individuals to obtain a driver’s license.",
                            18: "18 is the legal age of adulthood in many countries.",
                            19: "19 is the atomic number of potassium.",
                            20: "20 is the number of fingers and toes most humans have.",
                            21: "21 is the legal drinking age in the United States.",
                            22: "22 is a palindromic number, meaning it reads the same forward and backward.",
                            23: "23 is famous for Michael Jordan, who wore this number for most of his basketball career.",
                            24: "24 is the number of hours in a day.",
                            25: "Christmas is celebrated on December 25th.",
                            26: "There are 26 letters in the English alphabet.",
                            27: "27 is the atomic number of cobalt.",
                            28: "28 is the number of days in February in common years.",
                            29: "29 is the number of days in February in a leap year.",
                            30: "30 is the minimum age for a person to become a U.S. senator.",
                            31: "31 is the maximum number of days any month can have.",
                            32: "32 is the freezing point of water in degrees Fahrenheit.",
                            33: "33 is the atomic number of arsenic.",
                            34: "34 is the ninth number in the Fibonacci sequence.",
                            35: "35 is the minimum age for a person to become U.S. president.",
                            36: "36 is a perfect square (6 x 6).",
                            37: "37 is the atomic number of rubidium.",
                            38: "38 is the number of surviving plays written by William Shakespeare.",
                            39: "39 is the atomic number of yttrium.",
                            40: "40 is traditionally the number of hours in a workweek.",
                            41: "41 is a prime number and the atomic number of niobium.",
                            42: "42 is the answer to life, the universe, and everything in Douglas Adams' book *The Hitchhiker's Guide to the Galaxy*.",
                            43: "43 is the atomic number of technetium, the first element to be artificially produced.",
                            44: "44 is the number of U.S. Presidents before Barack Obama, the 44th.",
                            45: "45 is the speed (in RPM) of a single vinyl record.",
                            46: "46 is the atomic number of palladium.",
                            47: "47 is the atomic number of silver.",
                            48: "48 is the number of contiguous states in the United States.",
                            49: "49 is a perfect square (7 x 7).",
                            50: "50 is the number of stars on the U.S. flag.",
                            51: "Area 51 is a famous U.S. military base that has sparked numerous conspiracy theories.",
                            52: "There are 52 cards in a standard deck of playing cards.",
                            53: "53 is the atomic number of iodine.",
                            54: "54 is the atomic number of xenon.",
                            55: "55 is the speed limit (in miles per hour) in many parts of the United States.",
                            56: "56 is the number of signers of the U.S. Declaration of Independence.",
                            57: "57 varieties of products were advertised by the Heinz Company.",
                            58: "58 is the atomic number of cerium.",
                            59: "59 is the number of days Queen Elizabeth II ruled longer than Queen Victoria, making her the longest-reigning British monarch.",
                            60: "There are 60 seconds in a minute.",
                            61: "61 is the atomic number of promethium.",
                            62: "62 is the atomic number of samarium.",
                            63: "63 is the number of chromosomes in a donkey.",
                            64: "64 is the number of squares on a chessboard.",
                            65: "65 is the traditional retirement age in many countries.",
                            66: "Route 66 is a famous highway in the United States.",
                            67: "67 is the atomic number of holmium.",
                            68: "68 is the number of moons discovered orbiting Jupiter so far.",
                            69: "69 is the atomic number of thulium.",
                            70: "70 is the number of years in a typical human lifespan according to the Bible.",
                            71: "71 is the atomic number of lutetium.",
                            72: "72 is the number of names of God according to Kabbalah.",
                            73: "73 is Sheldon Cooper's favorite number from *The Big Bang Theory*.",
                            74: "74 is the atomic number of tungsten.",
                            75: "75 is the diamond wedding anniversary.",
                            76: "76 is the atomic number of osmium.",
                            77: "77 is the atomic number of iridium.",
                            78: "78 is the number of cards in a standard Tarot deck.",
                            79: "79 is the atomic number of gold.",
                            80: "Around the World in 80 Days is a famous novel by Jules Verne.",
                            81: "81 is a perfect square (9 x 9).",
                            82: "82 is the atomic number of lead.",
                            83: "83 is the atomic number of bismuth.",
                            84: "84 is the atomic number of polonium.",
                            85: "85 is the atomic number of astatine.",
                            86: "86 is the atomic number of radon.",
                            87: "87 is the atomic number of francium.",
                            88: "88 is the number of keys on a standard piano.",
                            89: "89 is the atomic number of actinium.",
                            90: "90 is the atomic number of thorium.",
                            91: "91 is the atomic number of protactinium.",
                            92: "92 is the atomic number of uranium.",
                            93: "93 is the atomic number of neptunium.",
                            94: "94 is the atomic number of plutonium.",
                            95: "95 is the atomic number of americium.",
                            96: "96 is the atomic number of curium.",
                            97: "97 is the atomic number of berkelium.",
                            98: "98 is the atomic number of californium.",
                            99: "99 is the atomic number of einsteinium.",
                            100: "100 is the basis for percentage calculations (percent means 'per 100')."
                        }

                        return facts[number]

                        
                    
                    try:
                        print(f"Fact about {first_arg}: {number_fact(int(first_arg))}")
                    except Exception as e:
                        print(
                                Fore.RED +
                                f"🌸 maximas says: hey, you gave an improper input! (spec: {e}; raised by: eni)"
                        )
                elif init_arg == "combine":
                    # Initial elements and their combinations
                    elements = [
                        "water", "fire", "earth", "air", "steam", "wind", "lava", "lake", "cloud", "mud", "pressure", 
                        "brick", "volcano", "ocean", "hydrothermal-vent", "continent", "planet", "sand", "glass", 
                        "time", "life", "stone", "plant", "tree", "geyser", "desert", "lightning", "storm", "rain", 
                        "hurricane", "mountain", "cave", "forest", "jungle", "tsunami", "earthquake", "meteor", 
                        "crystal", "obsidian", "magma", "coral", "reef", "flower", "fruit", "animal", "bird", "fish", 
                        "reptile", "mammal", "human", "sun", "moon", "star", "galaxy"
                    ]

                    combines = {
                        "steam": ["water", "fire"],
                        "wind": ["air", "air"],
                        "lava": ["fire", "earth"],
                        "cloud": ["steam", "water"],
                        "lake": ["water", "water"],
                        "mud": ["water", "earth"],
                        "pressure": ["steam", "earth"],
                        "brick": ["mud", "fire"],
                        "volcano": ["earth", "lava"],
                        "ocean": ["lake", "lake"],
                        "hydrothermal-vent": ["ocean", "volcano"],
                        "continent": ["earth", "earth"],
                        "planet": ["continent", "ocean"],
                        "sand": ["earth", "wind"],
                        "glass": ["sand", "fire"],
                        "time": ["sand", "glass"],
                        "life": ["time", "hydrothermal-vent"],
                        "stone": ["lava", "water"],
                        "plant": ["life", "earth"],
                        "tree": ["plant", "time"],
                        "geyser": ["steam", "pressure"],
                        "desert": ["sand", "wind"],
                        "lightning": ["air", "fire"],
                        "storm": ["wind", "cloud"],
                        "rain": ["cloud", "pressure"],
                        "hurricane": ["ocean", "storm"],
                        "mountain": ["earth", "pressure"],
                        "cave": ["earth", "stone"],
                        "forest": ["tree", "plant"],
                        "jungle": ["forest", "rain"],
                        "tsunami": ["ocean", "earthquake"],
                        "earthquake": ["earth", "pressure"],
                        "meteor": ["planet", "fire"],
                        "crystal": ["pressure", "sand"],
                        "obsidian": ["lava", "water"],
                        "magma": ["lava", "pressure"],
                        "coral": ["plant", "ocean"],
                        "reef": ["coral", "ocean"],
                        "flower": ["plant", "time"],
                        "fruit": ["plant", "life"],
                        "animal": ["life", "earth"],
                        "bird": ["air", "animal"],
                        "fish": ["animal", "water"],
                        "reptile": ["animal", "fire"],
                        "mammal": ["animal", "life"],
                        "human": ["mammal", "time"],
                        "sun": ["star", "planet"],
                        "moon": ["planet", "meteor"],
                        "star": ["lava", "lava"],
                        "galaxy": ["star", "time"]
                    }


                    # Available elements initially
                    avail_elements = ["water", "fire", "earth", "air"]

                    def combine_elements(input_elements):
                        sorted_input = sorted(input_elements)
                        for key, value in combines.items():
                            if sorted_input == sorted(value):
                                if key not in avail_elements:
                                    avail_elements.append(key)
                                return f"combination of {' + '.join(input_elements)} creates {key}."
                        return "no valid combination found."

                    # Main function to interact with the user
                    def element_combiner():
                        print(f"available elements: {', '.join(avail_elements)}")
                        
                        while True:
                            if sorted(avail_elements) == sorted(elements):
                                print("congratulations! you've unlocked all elements. you win!")
                                break

                            try:
                                eX = input("\ngive two elements to combine (or type 'exit' to quit): ").strip().lower()
                                if eX == "exit":
                                    break
                                
                                eR = eX.split()

                                if len(eR) != 2:
                                    print(Fore.RED + "🌸 maximas says: Please input exactly two elements.")
                                    continue

                                if eR[0] not in avail_elements or eR[1] not in avail_elements:
                                    print(Fore.RED +f"🌸 maximas says: both elements must be from the available list: {', '.join(avail_elements)}")
                                    continue

                                result = combine_elements([eR[0], eR[1]])
                                print(result)
                                
                                print(f"updated available elements: {', '.join(avail_elements)}")

                            except Exception as e:
                                print(Fore.RED +f"🌸 maximas says: an error occurred: {e}")

                    element_combiner()


                elif init_arg == "udo":
                    try:
                        if first_arg == "callme":
                            username = " ".join(else_args[0:])

                            # Update the username in the database
                            with shelve.open('user_data') as db:
                                db['username'] = username
                        elif first_arg == "color":
                            currcol = sec_arg
                        elif first_arg == "nocreds":
                            if nocreds == False:
                                nocreds = True
                            elif nocreds == True:
                                nocreds = False
                                credits = 10
                                multip = 1
                        else:
                            print(
                                Fore.RED +
                                "🌸 maximas says: hey, you gave an improper input! (spec: invalid or no args given; raised by: udo)"
                            )
                    except KeyError:
                        print(
                            Fore.RED +
                            f"🌸 maximas says: hey, that color is not available! (spec: invalid color ({sec_arg}); raised by: udo)"
                        )
                elif init_arg == "invoke":
                    subprocess.run(firstelse_args, shell=True)
                elif init_arg == "help":
                    print(Fore.LIGHTGREEN_EX +
                        "🪨  here are the available commands:")
                    print(
                        Fore.LIGHTGREEN_EX +
                        "  - echo [color] [message]: Prints the message with the specified color. The color must be one of the available colors: "
                        + Fore.WHITE + ", ".join(color_map.keys()) +
                        Fore.LIGHTGREEN_EX + ".")
                    print(
                        Fore.LIGHTGREEN_EX +
                        "  - udo callme [name]: Sets your username to the given name. Example: `udo callme John Doe`."
                    )
                    print(
                        Fore.LIGHTGREEN_EX +
                        "  - udo color [color]: Sets the output color to the given color. Example: `udo color blue`."
                    )
                    print(Fore.LIGHTGREEN_EX +
                        "  - clear: Clears the terminal screen.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - udo nocreds: Toggles if the credit system is being used.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - invoke [com]: Runs a shell command. Only works in Windows.")
                    
                    print(Fore.LIGHTGREEN_EX +
                        "  - lock [key]: Locks the terminal.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - tnttest [g]: Shows the force of a tnt blast. (radii)")
                    print(Fore.LIGHTGREEN_EX +
                        "  - cyoadv: A little choose your own adventure game.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - solve: Makes you solve a math problem.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - dare [easy|medium|hard|extreme]: Gives a dare.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - notes [see|make] [name] [text]: Makes or views notes.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - eni [number]: Gives a fact about a number 1-100.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - combine: Starts an element combination game")
                    print(Fore.LIGHTGREEN_EX +
                        "  - load [time]: Starts a timer that locks the terminal for the input time.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - sortlist [gtrlst|lslst] [nodupli|yesdupli] [numbers]: Sorts a list of numbers.\n"
                        "     * gtrlst: Sorts numbers in ascending order (small to large).\n"
                        "     * lslst: Sorts numbers in descending order (large to small).\n"
                        "     * nodupli: Removes duplicate numbers from the list before sorting.\n"
                        "     * yesdupli: Keeps duplicate numbers in the list during sorting.\n"
                        "     Example: `sortlist gtrlst nodupli 5 2 3 2 4` will return `2 3 4 5`.\n"
                        "     Example: `sortlist lslst yesdupli 5 2 3 2 4` will return `5 4 3 2 2`."
                    )
                    print(
                        Fore.LIGHTGREEN_EX +
                        "  - math [expression]: Evaluates a mathematical expression. Example: `math 2 + 3 * 4`."
                    )
                    print(Fore.LIGHTGREEN_EX +
                        "  - help: Displays this help message.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - rand [a] [b]: Picks a random number from a to b.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - do [1-100]: Repeats a command n times.")
                    print(Fore.LIGHTGREEN_EX + "  - quit: Exits the program.")
                    print(Fore.LIGHTGREEN_EX +
                        "  - specs: Shows findable system specs.")
                elif init_arg == "clear":
                    # Clear the terminal using os.system('clear') or os.system('cls')
                    import os
                    if platform.system() == "Windows":
                        os.system('cls')
                    else:
                        os.system('clear')
                elif init_arg == "cyoadv":
                    resp = ""

                    def askuser(storybef1, storybef2, opt, opt2):
                        # Ask the user for input and validate it
                        resp = input(f"{storybef1} {opt} {storybef2} {opt2}?: ")
                        
                        if resp == opt or resp == opt2:
                            return resp
                        else:
                            # If invalid input, ask again
                            print("Invalid choice. Please choose a valid option.")
                            return askuser(storybef1, storybef2, opt, opt2)

                    

                    if askuser("You wake up in a field. Do you go", "or", "right", "left") == "right":
                        if askuser("You go right. You see a car. Do you", "or do you", "take it", "leave it") == "take it":
                            if askuser("You drive on a path for a while, and end up in a city. Do you", "or do you", "continue going", "stop somewhere") == "continue going":
                                if askuser("You see a building labeled 'erebakatta.' You go inside, where they tell you that you are on the planet Kadai. Do you", "or do you", "stay", "leave") == "stay":
                                    if askuser("They offer you a mysterious device that grants you knowledge of the entire planet. Do you", "or do you", "accept it", "decline it") == "accept it":
                                        if askuser("You begin exploring Kadai. Do you first explore the cities or the wilderness?", "or do you", "cities", "wilderness") == "cities":
                                            print("You explore the vast cities of Kadai, learning advanced technology and gaining allies.")
                                            print("After years of integrating yourself into their society, you rise to a position of great power, shaping the future of the planet.")
                                            print("Your name becomes legend as the one who brought harmony to Kadai.")
                                            print("ENDING: Galactic Ambassador.")
                                        else:
                                            print("You venture into the wilderness, encountering strange creatures and ancient ruins. You discover forgotten technologies.")
                                            print("But over time, the wilderness consumes you, and you realize that some mysteries are too dangerous to uncover.")
                                            print("Eventually, you disappear, your fate unknown to the rest of the world.")
                                            print("ENDING: Lost Wanderer.")
                                    else:
                                        if askuser("They seem disappointed. Do you stay in the city or leave?", "or do you", "stay", "leave") == "stay":
                                            print("You stay in the city, but without the device, you struggle to find your place.")
                                            print("Eventually, you settle into an ordinary life, but a feeling of missed opportunities haunts you.")
                                            print("ENDING: Ordinary Life.")
                                        else:
                                            print("You leave the building, but the city is vast and overwhelming. Without guidance, you become lost in the endless maze of streets.")
                                            print("ENDING: Lost in the City.")
                                else:
                                    if askuser("You leave the building, but something feels off. Do you explore the city or head back to the field?", "or do you", "explore", "return") == "explore":
                                        if askuser("You explore the city and notice people watching you. Do you confront them or ignore it?", "or do you", "confront", "ignore") == "confront":
                                            print("You confront one of them and discover they aren’t human. Realizing the danger, you try to escape, but it’s too late.")
                                            print("You disappear, never to be seen again.")
                                            print("ENDING: Vanished.")
                                        else:
                                            print("You try to ignore the strange behavior, but soon you find yourself being followed everywhere you go.")
                                            print("Eventually, you are cornered, and the truth is revealed—you were the target all along.")
                                            print("ENDING: Trapped in Kadai.")
                                    else:
                                        print("You decide to return to the field, but the path back is not as it was. The landscape shifts and warps around you.")
                                        print("Eventually, you find yourself back in the field, as if nothing had happened. Was it all a dream?")
                                        print("ENDING: Full Circle.")
                            else:
                                if askuser("You stop at a café in the city. A stranger offers to guide you through Kadai. Do you", "or do you", "trust them", "refuse") == "trust them":
                                    if askuser("The stranger takes you to an underground base. Do you investigate further or escape?", "or do you", "investigate", "escape") == "investigate":
                                        print("You investigate and discover a secret society aiming to overthrow the government of Kadai.")
                                        print("With the knowledge you gain, you become a key figure in the rebellion, but the fight is dangerous and full of risks.")
                                        print("You either win or lose the battle for Kadai's future.")
                                        print("ENDING: Revolutionary Leader.")
                                    else:
                                        print("You choose to escape, realizing the situation is too dangerous. As you flee, you find a hidden exit leading back to the field.")
                                        print("You take one last look at the strange city before leaving, never to return.")
                                        print("ENDING: Escaped.")
                                else:
                                    print("You refuse the stranger's offer, continuing to wander the streets alone. Eventually, you find yourself lost.")
                                    print("Without any guidance or resources, you fade into the background, forgotten by the world.")
                                    print("ENDING: Forgotten.")
                        else:
                            if askuser("You decide not to take the car. As you walk down the road, you find a small village. Do you", "or do you", "enter", "keep walking") == "enter":
                                if askuser("The villagers are friendly, but there’s something strange about the place. Do you", "or do you", "investigate", "ignore it") == "investigate":
                                    if askuser("You uncover dark secrets. Do you confront the villagers or try to escape?", "or do you", "confront", "escape") == "confront":
                                        print("You confront the villagers and discover they are part of a government experiment. Before you can escape, you are captured and made part of the experiment.")
                                        print("ENDING: Experiment Subject.")
                                    else:
                                        print("You try to escape, but the villagers are watching. You don’t make it far before you are caught.")
                                        print("ENDING: Captured in the Village.")
                                else:
                                    print("You decide to ignore your suspicions and stay in the village. Life is peaceful, but you never shake the feeling that something is wrong.")
                                    print("ENDING: Village Life.")
                            else:
                                print("You keep walking down the road, eventually reaching a new city. But the road was long, and you feel like a different person.")
                                print("The adventure changes you, but your journey has just begun.")
                                print("ENDING: Endless Traveler.")
                    else:
                        if askuser("You turn left and find yourself in a dense forest. Do you", "or do you", "enter the forest", "stay on the road") == "enter the forest":
                            if askuser("You come across an ancient temple. Do you", "or do you", "go inside", "turn back") == "go inside":
                                if askuser("Inside, you find a portal. Do you go through it or leave?", "or do you", "go through", "leave") == "go through":
                                    print("You step through the portal and find yourself in another dimension, where new adventures await.")
                                    print("ENDING: Dimensional Wanderer.")
                                else:
                                    print("You decide not to enter the portal. As you turn back, the forest begins to change, and soon you find yourself lost forever.")
                                    print("ENDING: Lost in the Forest.")
                            else:
                                print("You decide not to enter the temple and continue walking. However, strange things begin to happen, as if the forest itself is alive.")
                                print("Eventually, you are lost forever in the labyrinthine woods.")
                                print("ENDING: Lost in the Forest.")
                        else:
                            if askuser("You stay on the road and encounter a mysterious figure. Do you", "or do you", "talk to them", "avoid them") == "talk to them":
                                if askuser("The figure offers to show you something powerful. Do you accept or refuse?", "or do you", "accept", "refuse") == "accept":
                                    print("The figure takes you to a hidden location, where they reveal the truth of the world you are in. Your perspective changes forever.")
                                    print("ENDING: Enlightened Traveler.")
                                else:
                                    print("You refuse the offer and continue walking. The figure disappears, and soon the road takes you back to where you began.")
                                    print("ENDING: Full Circle.")
                            else:
                                print("You avoid the figure and continue walking. The road takes you to a new city, but something feels off. The adventure is far from over.")
                                print("ENDING: Mysterious Journey.")




                elif init_arg == "lock":
                    # Clear the terminal using os.system('clear') or os.system('cls')
                    import os
                    if platform.system() == "Windows":
                        os.system('cls')
                    else:
                        os.system('clear')

                    while icode != first_arg:
                        icode = input(color_map[currcol] + "Maximas is locked. Type the lock key to unlock: ")
                        if icode != first_arg:
                            print(color_map[currcol] + "Incorrect code.")

                    if platform.system() == "Windows":
                        os.system('cls')
                    else:
                        os.system('clear')
                elif init_arg == "tnttest":
                    def calculate_blast_radius(mass_g):
                        # Convert mass from grams to kilograms
                        mass_kg = mass_g / 1000.0
                        
                        # Proportional constant (adjustable based on empirical data)
                        k = 0.5
                        
                        # Calculate blast radius
                        radius = k * (mass_kg ** (1/3))
                        return radius

                    # Example usage:
                    mass = float(first_arg)
                    radius = calculate_blast_radius(mass)
                    print(f"💥 the estimated blast radius for {mass} grams of TNT is approximately {radius:.2f} meters.")
                elif init_arg == "solve":
                    # Generate two random numbers between 1 and 100
                    num1 = random.randint(1, 100)
                    num2 = random.randint(1, 100)
                    
                    # Randomly choose an operation: +, -, *, or /
                    operation = random.choice(['+', '-', '*', '/'])
                    
                    # Create the math problem based on the chosen operation
                    if operation == '+':
                        correct_answer = num1 + num2
                        question = f"{num1} + {num2}"
                    elif operation == '-':
                        correct_answer = num1 - num2
                        question = f"{num1} - {num2}"
                    elif operation == '*':
                        correct_answer = num1 * num2
                        question = f"{num1} * {num2}"
                    else:  # For division, ensure no division by zero
                        num2 = random.randint(1, 10)  # Limit the divisor to a smaller number for simplicity
                        correct_answer = round(num1 / num2, 2)  # Round the result to 2 decimal places
                        question = f"{num1} / {num2}"

                    # Ask the user for their answer
                    user_answer = input(color_map[currcol] + f"solve: {question} = ")

                    # Check if the user's answer is correct
                    try:
                        if float(user_answer) == correct_answer:
                            print(color_map[currcol] +"🌸 maximas says: correct!")
                        else:
                            print(color_map[currcol] +f"🌸 maximas says: incorrect. The correct answer is {correct_answer}.")
                    except ValueError:
                        print(color_map['red'] + "🌸 maximas says: invalid input. Please enter a number.")
                elif init_arg == "rand":
                    try:
                        first_arg = int(first_arg)
                        sec_arg = int(sec_arg)
                        print(color_map[currcol] + f"🌙 Result: {random.randint(first_arg, sec_arg)}")
                    except ValueError:
                        print(Fore.RED + "🌸 maximas says: hey, you gave an improper input! (spec: non-integer values; raised by: rand)")
                elif init_arg == "sortlist":
                    try:
                        # Ensure there are at least two arguments (sort type and dupli flag)
                        if len(firstelse_args) < 3:
                            print(Fore.RED + "🌸 maximas says: hey, you gave an improper input! (spec: missing arguments; raised by: sortlist)")
                            continue

                        # Extract sorting type (gtrlst/lslst) and duplication flag (nodupli/yesdupli)
                        sort_type = firstelse_args[0]
                        dupli_flag = firstelse_args[1]

                        # Remaining arguments are the numbers
                        number_args = firstelse_args[2:]

                        # Validate numbers
                        numbers = []
                        for arg in number_args:
                            try:
                                numbers.append(int(arg))
                            except ValueError:
                                print(Fore.RED + f"🌸 maximas says: hey, you gave an improper input! (spec: invalid number '{arg}'; raised by: sortlist)")
                                continue

                        # Handle duplicates based on flag
                        if dupli_flag == "nodupli":
                            numbers = list(set(numbers))  # Remove duplicates
                        elif dupli_flag != "yesdupli":
                            print(Fore.RED + "🌸 maximas says: hey, you gave an improper input! (spec: invalid flag, use 'nodupli' or 'yesdupli'; raised by: sortlist)")
                            continue

                        # Sort numbers
                        if sort_type == "gtrlst":
                            sorted_list = sorted(numbers)  # Ascending order
                        elif sort_type == "lslst":
                            sorted_list = sorted(numbers, reverse=True)  # Descending order
                        else:
                            print(Fore.RED + "🌸 maximas says: hey, you gave an improper input! (spec: invalid sort type, use 'gtrlst' or 'lslst'; raised by: sortlist)")
                            continue

                        # Display sorted list
                        print(Fore.LIGHTGREEN_EX + "🔢 Sorted list: " + Fore.WHITE + " ".join(map(str, sorted_list)))

                        # Calculate and display statistics
                        if len(numbers) > 0:
                            mean_value = statistics.mean(numbers)
                            median_value = statistics.median(numbers)
                            range_value = max(numbers) - min(numbers)
                            try:
                                mode_value = statistics.mode(numbers)
                            except statistics.StatisticsError:
                                mode_value = "No unique mode"

                            print(Fore.LIGHTCYAN_EX + f"📊 Mean: {mean_value}")
                            print(Fore.LIGHTCYAN_EX + f"📊 Median: {median_value}")
                            print(Fore.LIGHTCYAN_EX + f"📊 Range: {range_value}")
                            print(Fore.LIGHTCYAN_EX + f"📊 Mode: {mode_value}")
                        else:
                            print(Fore.RED + "🌸 maximas says: hey, the list is empty after processing; raised by: sortlist")

                    except Exception as e:
                        print(Fore.RED + f"🌸 maximas says: Unexpected error: {e}; raised by: sortlist")
                elif init_arg == "notes":
                    if first_arg == "see":
                        with shelve.open('notes') as db:
                            try:
                                print(color_map[currcol] + db[sec_arg])
                            except KeyError:
                                print(Fore.RED + f"🌸 maximas says: note '{sec_arg}' not found.")
                    elif first_arg == "make":
                        with shelve.open('notes') as db:
                            db[sec_arg] = ' '.join(else_args[1:])
                            print(color_map[currcol] + f"🌸 maximas says: note '{sec_arg}' created.")
                elif init_arg == "dare":
                    category = first_arg.strip().lower()
                    
                    
                    dares = {
                        "easy": [
                            "Dance to a song for 1 minute.",
                            "Try a new food or snack.",
                            "Sing your favorite song out loud.",
                            "Do 10 jumping jacks.",
                            "Speak in an accent for the next 10 minutes.",
                            "Post a positive comment on a social media post.",
                            "Do a random act of kindness for someone.",
                            "Try a new exercise for 5 minutes."
                        ],
                        "medium": [
                            "Call a friend and sing Happy Birthday to them.",
                            "Post an embarrassing photo on social media (only if you're comfortable with it).",
                            "Try a new hobby or craft project for 30 minutes.",
                            "Read a random page from a book aloud to someone.",
                            "Send a message to an old friend and reconnect.",
                            "Wear a funny outfit for the next hour.",
                            "Cook a meal using a recipe you’ve never tried before.",
                            "Take a 30-minute walk in a new part of town."
                        ],
                        "hard": [
                            "Perform a short skit or monologue in front of a group.",
                            "Wear your clothes backward for the rest of the day.",
                            "Take a cold shower for 2 minutes.",
                            "Try a complex recipe you’ve never made before.",
                            "Write and perform a short poem or rap.",
                            "Spend an hour doing a physical activity you dislike.",
                            "Organize a small event or gathering for friends or family.",
                            "Try a new sport or physical challenge."
                        ],
                        "extreme": [
                            "Do a public speech or presentation on a random topic.",
                            "Spend 24 hours without using any electronic devices.",
                            "Run or walk a 5k (or equivalent distance) without stopping.",
                            "Volunteer for a cause you’re unfamiliar with for a day.",
                            "Try a daring adventure activity like skydiving or bungee jumping (if available).",
                            "Commit to a week-long challenge like a diet or fitness goal.",
                            "Participate in a local competition or event.",
                            "Take a solo trip to a new city or country."
                        ]
                    }
                    
                    if category not in dares:
                        return "🌸 maximas says: invalid category. Please choose from 'easy', 'medium', 'hard', or 'extreme'."
                    
                    print(color_map[currcol] + random.choice(dares[category]))

                
                    
                elif init_arg == "math":
                    
                    if len(firstelse_args) > 0:
                        try:
                            # Evaluate the expression
                            result = eval(" ".join(firstelse_args))

                            print((color_map[currcol] + "🔢 result: ") +
                                (Fore.WHITE + str(result)))

                        except ZeroDivisionError:
                            print(
                                Fore.RED +
                                "🌸 maximas says: hey, you can't divide by zero! (spec: division by zero; raised by: math)"
                            )
                        except (SyntaxError, NameError, TypeError) as e:
                            print(
                                Fore.RED +
                                f"🌸 maximas says: hey, you gave an improper input! (spec: {e}; raised by: math)"
                            )
                elif com != "quit" and init_arg != "do":
                    temp_sysraise = 1
                    print(
                        Fore.RED +
                        "🌸 maximas says: hey, you gave an improper input! (spec: invalid command; raised by: sys)"
                )

        else:
            # If credits reach zero, roll a dice for credits
            credits = random.randint(multip, multip + 7)
            print(
                Fore.RED +
                f"🌸 maximas says: you're out of credits! Rolling for credits... ({credits})"
            )


mainloop()
