import json


class AccountDB:
    def __init__(self, game):
        """Create game in __init__."""
        self.game = game


    def register(self, game_account):
        """Create game account in new_data to input the data in this function
        and create the condition if number of character = 0 will print Do not let any fields empty else ask a question
        if player want to save the account it's will save the data in file data.json."""
        new_data = {game_account.email: {
                "username": game_account.username,
                "password": game_account.password
            }
        }
        if len(game_account.username) == 0 or len(game_account.password) == 0 or len(game_account.email) == 0:
            print("Do not let any fields empty")
        else:
            is_ok = input(f"Game: Maze Runner Game\nUsername: {game_account.username}"
                          f"\nPassword: {game_account.password}\nis it ok to save? ")
            if is_ok[0].lower() == "y":
                try:
                    with open("data.json", "r") as data_file:
                        data_account = json.load(data_file)
                except FileNotFoundError:
                    with open("data.json", "w") as data_file:
                        json.dump(new_data, data_file, indent=4)
                else:
                    data_account.update(new_data)
                    with open("data.json", "w") as data_file:
                        json.dump(data_account, data_file, indent=4)

    def change_username(self, email, username, password, new_username):
        """Create the function that can change the username if email in the data.json file and correct username
        and password the username can be change in the data.json file."""
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if email in data:
                if data[email]["username"] == username:
                    if data[email]["password"] == password:
                        data[email]["username"] = new_username
                        print(f'Username changed successfully.Changed {username} to {new_username}.')
                        data.update(data)
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                    else:
                        print(f"Your password: {password} is wrong.Please try again.")
                else:
                    print(f'Your username: {username} is wrong.Please try again.')
            else:
                print(f'You have entered you email incorrectly.Please check your email and try again.')
        except KeyError:
            print(f'No data for this account.')

    def change_password(self, email, username, password, new_password):
        """Create the function that can change the password if email in the data.json file and correct username
        and password the password can be change in the data.json file."""
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if email in data:
                if data[email]["username"] == username:
                    if data[email]["password"] == password:
                        data[email]["password"] = new_password
                        print(f'Username changed successfully.Changed {password} to {new_password}.')
                        data.update(data)
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                    else:
                        print(f"Your password: {password} is wrong.Please try again.")
                else:
                    print(f'Your username: {username} is wrong.Please try again.')
            else:
                print(f'You have entered your email incorrectly.Please check your email and try again.')
        except KeyError:
            print(f'No data for this account.')


    def find_username(self, email, username):
        """Create the function that can find the username if email in data.json and correct username that will show the
        account exists in the system."""
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                if email in data:
                    if data[email]["username"] == username:
                        print(f'This user account exists in the system.')
                    else:
                        print(f'You have entered your username incorrectly.Please check your username and try again.')
                else:
                    print(f'No details for email: {email} exists.'
                          f'Please check your email or register this account first.')
        except FileNotFoundError:
            print('This account information is not available.')

    def login(self, email, password):
        """Create the function that can login the account in this function before play game."""
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if email in data:
                if data[email]["password"] == password:
                    login = input("Do you want to login? ")
                    if login[0].lower() == "y":
                        print("Login successfully.")
                        data[email].update({"status": "online"})
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                            return True
                else:
                    print(f"Your password: {password} is wrong.Please try again.")
            else:
                print(f'No details for email: {email} exists.'
                      f'Please check your email or register this account first.')
        except FileNotFoundError:
            print("You have entered your email account incorrectly.Please check your email account and try again.")

    def logout(self, email, password):
        """Create the function that can logout after the game has end."""
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if email in data:
                if data[email]["password"] == password:
                    logout = input("Do you want to logout? ")
                    if logout[0].lower() == "y":
                        print("Logout successfully.")
                        data[email].update({"status": "offline"})
                        with open("data.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                    else:
                        print("It's okay, I'll wait for you again.")
                else:
                    print(f"Your password: {password} is wrong.Please try again.")
            else:
                print(f'No details for email: {email} exists.Please check your email and try again.')
        except FileNotFoundError:
            print("You have entered your email account incorrectly.Please check your email account ang try again.")




    def __repr__(self):
        """
        The object representation can be changed by implementing the __repr__ method,which is required to a string.
        """
        return f'AccountDB(Game="{self.game}")'


