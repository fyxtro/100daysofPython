from colorama import Fore

print('''
*******************************************************************************
███████ ██   ██ ██████  ██       ██████  ███████ ██ ██    ██ 
██       ██ ██  ██   ██ ██      ██    ██ ██      ██ ██    ██ 
█████     ███   ██████  ██      ██    ██ ███████ ██ ██    ██ 
██       ██ ██  ██      ██      ██    ██      ██ ██  ██  ██  
███████ ██   ██ ██      ███████  ██████  ███████ ██   ████   
*******************************************************************************
''')
print("Welcome to explosiv.")
print("""You wake up in a room with no light. After a few seconds a light turns on. 
You look around the room but to your surprise you see no door to this room. Only a table and a chair.
On top of the table, a bomb with 3 closed panels. Next to the bomb are wirecutters.
When you sit down on the chair 1 of the panels opens up on the bomb. Thats when you hear a loud voice through the room.
""")
print(f"{Fore.RED}YOU MUST DEFUSE THE BOMB.{Fore.RESET}")

def boom():
    print("""
██████   ██████   ██████  ███    ███ 
██   ██ ██    ██ ██    ██ ████  ████ 
██████  ██    ██ ██    ██ ██ ████ ██ 
██   ██ ██    ██ ██    ██ ██  ██  ██ 
██████   ██████   ██████  ██      ██ 
    """)
    print("There was no room for mistakes here, the bomb exploded")

def doom():
    print("You decided it was best to not cut the wire. You put down the wirecutters and stare out in front of you as you await your inevitable doom.")
    print("That's when you hear a sudden bang and everything goes white. Then you wake up in your bed. This was just a dream...")
    print("""
██████   █████  ██████      ███████ ███    ██ ██████  ██ ███    ██  ██████  
██   ██ ██   ██ ██   ██     ██      ████   ██ ██   ██ ██ ████   ██ ██       
██████  ███████ ██   ██     █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███ 
██   ██ ██   ██ ██   ██     ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██ 
██████  ██   ██ ██████      ███████ ██   ████ ██████  ██ ██   ████  ██████  
    """)

def win():
    print("You did it! You defused the bomb! Suddenly a door appears behind you. You go through it and wake up in your bed. This was just a dream...")
    print("""
 ██████   ██████   ██████  ██████      ███████ ███    ██ ██████  ██ ███    ██  ██████  
██       ██    ██ ██    ██ ██   ██     ██      ████   ██ ██   ██ ██ ████   ██ ██       
██   ███ ██    ██ ██    ██ ██   ██     █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███ 
██    ██ ██    ██ ██    ██ ██   ██     ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██ 
 ██████   ██████   ██████  ██████      ███████ ██   ████ ██████  ██ ██   ████  ██████  
    """)

choice1 = input(f"You see 2 wires sticking out, a {Fore.MAGENTA}purple{Fore.RESET} one and a {Fore.BLUE}blue{Fore.RESET} one, you must decide which wire to cut: {Fore.MAGENTA}purple{Fore.RESET} or {Fore.BLUE}blue{Fore.RESET} ").lower()
if choice1 == "blue":
    choice2 = input(f"A second panel on the bomb opens and you find 2 more wires. A {Fore.GREEN}green{Fore.RESET} one and a {Fore.YELLOW}yellow{Fore.RESET} one. Which one will you cut? ").lower()
    if choice2 == "green":
        print(f"The last panels opens up. There is only 1 wire visible. The wire is {Fore.RED}RED{Fore.RESET} and it is bigger than the others. Somehow you start to doubt whether you should cut this wire.")
        choice3 = input("Will you cut it? [y/n] ").lower()
        if choice3 == "y" or "yes":
            win()
        elif choice3 == "n" or "no":
            doom()
    else:
        boom()
else:
    boom()
