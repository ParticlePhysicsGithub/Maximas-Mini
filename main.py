import colorama
from colorama import Fore, Style, Back
import shelve
import platform
import subprocess
import random

colorama.init(autoreset=True)

# Initialize username
username = "nil"
temp_sysraise = 0
currcol = "white"
credits = 10

whitelist = ["quit", "help", "clear", "specs"]

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
    global username, temp_sysraise, currcol, whitelist, credits
    com = ""

    ee_mcp_n = 0

    multip = 1

    print(
        color_map[currcol] +
        f"Welcome to Maximas Mini!\nType help for help.\nAlso, you need 1 credit per command (this goes up).\nTo get credits, type mon [number 1 to 3].\nIf credits reach zero, then a dice will be rolled for how many credits you get.\nYou can also type quit to quit.\nNote: Errors also take credits.\nThere is no oh-no-you-messed-up coin return system. (unless it is a bug)"
    )

    # Open the shelve database
    with shelve.open('user_data') as db:
        # Load username if it exists in the database
        if 'username' in db:
            username = db['username']

    credits = 10

    while com != "quit":

        if username == "morecreditsplease" and ee_mcp_n == 0:

            credits += 99999999
            ee_mcp_n = 1

        if credits > 0:

            try:
                print(color_map['yellow'] + f"🪙  {credits} ✖️  {multip}")
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
                print(
                    Fore.LIGHTGREEN_EX +
                    "  - math [expression]: Evaluates a mathematical expression. Example: `math 2 + 3 * 4`."
                )
                print(Fore.LIGHTGREEN_EX +
                      "  - help: Displays this help message.")
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
