import turtle
from database import AccountDB
from account import PlayerAccount
from Gamster import Player


while True:
    print("Hello!, Welcome to the Maze Runner Game.")
    print("1. Register")
    print("2. Login")
    print("3. Find Username")
    print("4. Change Username")
    print("5. Change Password")
    print("6. Logout")
    choice = int(input("Enter choice: "))
    db = AccountDB("Maze Runner Game")
    if choice == 1:
        register_email = input("Type your email: ")
        register_username = input("Type your username: ")
        register_password = input("Type your password: ")
        PlayerAccount(register_email, register_username, register_password, db)
        print("Please login your account.")
        login_email = input("Type you email account: ")
        login_password = input("Type your password: ")
        if db.login(login_email, login_password):
            set_up = turtle.Screen()
            set_up.bgpic("MazeRunnerGame.gif")
            start = set_up.textinput(title="Welcome to the Maze Runner Game!", prompt="Are you ready to start!")
            set_up.clear()
            from setup_maze import setup_maze, player_move, levels, exit
            if start[0].lower() == "y":
                for i in range(len(levels)):
                    setup_maze(levels[i])
                    while exit != []:
                        player_move()
                        Player(turtle).num_level += 1
                        set_up.update()
                    set_up.clear()
                set_up.bye()
                print("Please logout your account.")
                logout_email = input("Type your email account: ")
                logout_password = input("Type your password: ")
                if db.logout(logout_email, logout_password):
                    print("Thank you see you next time!")
                    break
            if start[0].lower() == "n":
                set_up.bye()
                print("Please logout your account.")
                logout_email = input("Type your email account: ")
                logout_password = input("Type your password: ")
                if db.logout(logout_email, logout_password):
                    print("Thank you see you next time!")
                    break
    if choice == 2:
        login_email = input("Type your email account: ")
        login_password = input("Type your password: ")
        if db.login(login_email, login_password):
            set_up = turtle.Screen()
            set_up.bgpic("MazeRunnerGame.gif")
            start = set_up.textinput(title="Welcome to the Maze Runner Game!", prompt="Are you ready to start!")
            set_up.clear()
            from setup_maze import setup_maze, player_move, levels, exit
            if start[0].lower() == "y":
                for i in range(len(levels)):
                    setup_maze(levels[i])
                    while exit != []:
                        player_move()
                        set_up.update()
                    set_up.clear()
                set_up.bye()
                print("Please logout your account.")
                logout_email = input("Type your email account: ")
                logout_password = input("Type your password: ")
                if db.logout(logout_email, logout_password):
                    print("Thank you see you next time!")
                    break
            if start[0].lower() == "n":
                set_up.bye()
                print("Please logout your account.")
                logout_email = input("Type your email account: ")
                logout_password = input("Type your password: ")
                if db.logout(logout_email, logout_password):
                    print("Thank you see you next time!")
                    break
    if choice == 3:
        find_email = input("Type your email account: ")
        find_username = input("Type your username account: ")
        db.find_username(find_email, find_username)
    if choice == 4:
        cu_email = input("Type your email account: ")
        cu_username = input("Type your username account: ")
        cu_password = input("Type your password account: ")
        cu_new_username = input("Type your new username: ")
        db.change_username(cu_email, cu_username, cu_password, cu_new_username)
    if choice == 5:
        cp_email = input("Type your email account: ")
        cp_username = input("Type your username account: ")
        cp_password = input("Type your password account: ")
        cp_new_password = input("Type your new password: ")
        db.change_password(cp_email, cp_username, cp_password, cp_new_password)
    if choice == 6:
        logout_email = input("Type your email account: ")
        logout_password = input("Type your password: ")
        db.logout(logout_email, logout_password)
        break
