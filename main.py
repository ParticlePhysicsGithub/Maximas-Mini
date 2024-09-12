import colorama
from colorama import Fore, Style, Back
import shelve
import platform
import subprocess
import random
import statistics
import datetime

colorama.init(autoreset=True)

# Initialize username
username = "nil"
temp_sysraise = 0
currcol = "white"
credits = 10
user_biotext = "...write your bio..."
user_defcolor = Fore.WHITE

whitelist = ["quit", "help", "clear", "specs", "time"]

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

    nocreds = False
    
    ee_mcp_n = 0

    multip = 1

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
                    print(color_map['yellow'] + f"🪙  {credits} ✖️  {multip}")
                else:
                    credits = 999999999
                    multip = 1
                com = input(color_map[currcol] +
                            f"maximas mini | {username} | > " +
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
            

            elif init_arg == "time":
                print(color_map[currcol] + f"⌚ the time is {str(datetime.datetime.now().time())}")


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
            elif com != "quit":
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
