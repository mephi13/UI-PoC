from blessed import Terminal
from randomart import draw, drunkenwalk
from hashlib import md5
from datetime import datetime
from random import randbytes


user = {
    "username": "mephi",
}

profile = True

bob = {
    "username":"bob",
    "key": "",
    "hash_of_key": "",
    "art": ""
}


def bprint(*args, **kwargs):
    print(*args, **kwargs, end='')

term = Terminal()

def main():
    print(term.clear)

    bob["key"] = randbytes(123)
    bob["hash_of_key"] = md5(bob["key"])
    bob["art"] = draw(drunkenwalk(bob["hash_of_key"].digest()), "1234567891")
    

    with term.location(0,0):
        bprint('-' * (term.width))

    with term.location(0,2):
        bprint('-' * (term.width))

    with term.location(term.width-50, 1):
        login_text = term.rjust("logged in as " + term.green_underline(user["username"]), 50)
        print(login_text, end = '')

    with term.location(0, 1):
        print(term.underline_red("cans") + " secure messenger", end = '')

    with term.location(0,term.height - 5):
        bprint('-' * (term.width))
    with term.location(0,term.height):
        bprint('-' * (term.width))

    for i in range(3, term.height- 5):
        with term.location(term.width-13, i):
            bprint("|")

    with term.location(term.width-12, 3):
        bprint(term.green("*") + " " +  term.orange_underline("System") + " ")

    with term.location(term.width-12, 4):
        bprint(term.green("*") + " " +  term.pink("bob") + " ")

    with term.location(term.width-12, 6):
        bprint(term.red("#") + " " +  term.blue("someone") + " ")

    with term.location(term.width-12, 5):
        bprint(term.red("#") + " " +  term.pink("mum") + " ")

    with term.location(term.width-12, 7):
        bprint(term.red("#") + " " +  term.lightblue("dad") + " ")

    with term.location(term.width - 2, 6):
        bprint(term.yellow("✉"))

    with term.location(term.width - 2, 5):
        bprint(term.red_bold("✉"))

    if profile:
        with term.location(0,2 + 6):
            bprint('-' * (term.width - 13))
        with term.location(0,3):
            bprint(term.pink(bob["art"])) 
        with term.location(11,3):
            bprint(f"Username: {term.pink(bob['username'])}")
        with term.location(11,4):
            bprint(f"Added: {datetime(2022,3,6,13,56,34).strftime('%x %X')}")
        with term.location(11,5):
            bprint(f"Color: {term.pink('pink')}")
        with term.location(11,6):
            bprint(f"Messages exchanged: 51")
        with term.location(11,7):
            bprint(f"Public key: {bob['hash_of_key'].hexdigest()}")

    print(term.move_y(term.height - 3), end='')
    bprint(term.green_underline(user["username"]) + term.gray(">"))    

    messages = [
        (user["username"], f"don't know... let's try:", datetime(2022, 3 ,21, 11, 36 ,15)),
        (bob["username"], f"Okay that's { term.lightgreen_bold('cool') }, but do we have markdown support?", datetime(2022, 3 ,21, 11, 35 ,43)),
        (user["username"], term.blue_underline("https://www.youtube.com/watch?v=dQw4w9WgXcQ"), datetime(2022, 3 ,21, 11, 34 ,42)),
        (user["username"], "Observe", datetime(2022, 3 ,21, 11, 34 ,35)),
        (bob["username"], "No way dude", datetime(2022, 3 ,21, 11, 34 ,1)),
        (user["username"], "You know we can posts links here?", datetime(2022, 3 ,21, 11, 33 ,53)),
        (bob["username"], "What do you want", datetime(2022, 3 ,21, 11, 32 ,29)),
        (user["username"], "Hi", datetime(2022, 3 ,21, 11, 31 ,59)), 
        (bob["username"], "Hello", datetime(2022, 3 ,21, 11, 31 ,52)),
        ("System", term.orange("Connection to ") + term.pink("bob") + term.orange(" established"), datetime(2022, 3 ,21, 11, 25 ,49)),
        ("System", term.orange("Welcome to ") + term.red_underline("cans") + term.orange("! Have fun messaging securely"), datetime(2022, 3 ,21, 10, 15 ,39))
        ]

    for i, mes in enumerate(messages):
        with term.location(0, term.height - 6 - i):
            #message = ""
            message = term.gray(mes[2].strftime("[%H:%M]"))
            if mes[0] == user["username"]:
                message += (term.gray("[")  + term.green(mes[0]) + term.gray("]>") + mes[1])
            elif mes[0] == 'System':
                message += (term.gray("[")  + term.orange_underline(mes[0]) + term.gray("]>") + mes[1])
            else:
                message += (term.gray("[")  + term.pink(mes[0]) + term.gray("]>") + mes[1])
            print(message)
        #with term.location(term.width - 14 - 20, term.height - 6 - i):
        #    bprint(term.rjust(term.gray(mes[2].strftime("%H:%M:%S")), 20))

inp = ""
while 1:
    if inp == "/p":
        profile = not profile
    main()
    inp = ""
    with term.location(len(user["username"]) + 1, term.height - 3):
            inp = input()
            print(term.clear_eol)

