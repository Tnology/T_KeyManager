import json
import secrets

version = "2.0.1"


def create_file_data():
    choice_number = 0
    while choice_number == 0:
        auto_generate_key = input("How would you like new keys to be made (can be changed later with the \'settings\' command)?\n1: Generate one for me\n2: Ask me every time\n3: Manually enter a key each time\n> ")
        if auto_generate_key == "1":
            with open("keys.json", "w+") as __file:
                __file.write("{\"settingsautogeneratekey\": \"yes\"}")
                __file.close()
                print("Done!")
                choice_number += 1
        elif auto_generate_key == "2":
            with open("keys.json", "w+") as __file:
                __file.write("{\"settingsautogeneratekey\": \"ask\"}")
                __file.close()
                print("Done!")
                choice_number += 1
        elif auto_generate_key == "3":
            with open("keys.json", "w+") as __file:
                __file.write("{\"settingsautogeneratekey\": \"no\"}")
                __file.close()
                print("Done!")
                choice_number += 1
        else:
            print("Invalid Option, please choose again.")


try:
    with open("keys.json", "r+") as file:
        if len(file.readlines()) == 0:
            print("It looks like there is currently no file data!")
            create_file_data()
            data = json.load(file)
        elif len(file.readlines()) != 0:
            print("File Data Detected! Continuing!")
            data = json.load(file)
except FileNotFoundError:
    create_file_data()
    data = json.load(file)


def create_key(key_data):
    with open("keys.json", "w+") as __file:
        data.update({user_id: key_data})
        json.dump(data, __file)
        file.close()
        print("Done!")


def find_key():
    _user_id = input("Please enter a User ID: ")
    with open("keys.json", "r") as __file:
        _found_number = 0
        _found_line = 0
        for data_key in data:
            if _user_id in data_key and len(data_key) == len(_user_id):
                _found_line = 1
                _found_key = data.get(data_key)
        if _found_line == 1:
            print(_found_key)
        else:
            print("User not found!")


def find_user():
    key_id = input("Please enter a Key: ")
    with open("keys.json", "r") as __file:
        try:
            found_key = list(data.keys())[list(data.values()).index(key_id)]
            found_line = 1
        except ValueError:
            found_line = 0
        if found_line == 1:
            print(found_key)
        else:
            print("Key not found!")


def edit_key():
    key_id = input("Please enter a Key: ")
    with open("keys.json", "r") as __file:
        __data = json.load(__file)
        try:
            found_key = list(__data.keys())[list(__data.values()).index(key_id)]
            found_line = 1
        except ValueError:
            found_line = 0
    if found_line == 1:
        _key_update = input("Please enter a new key: ")
        with open("keys.json", "w+") as __file:
            __data.update({found_key: _key_update})
            json.dump(__data, __file)
        print("Key updated!")
    else:
        print("Key not found!")


def delete_key():
    _user_id = input("Please enter a User ID: ")
    with open("keys.json", "r") as __file:
        __data = json.load(__file)
    with open("keys.json", "w+") as __file:
        try:
            __override_confirmation = input("WARNING: Are you sure you want to delete this key for the user '" + _user_id + "'? This action is permanent and the key will be unrecoverable. (Y/N) > ")
            if __override_confirmation.casefold() == "y":
                del __data[_user_id]
                json.dump(__data, __file)
                print("Done!")
            elif __override_confirmation.casefold() == "n":
                print("Operation cancelled!")
                json.dump(__data, __file)
            else:
                print("Invalid option!")
                json.dump(__data, __file)
        except KeyError:
            print("User ID not found!")
            json.dump(__data, __file)


while True:
    command = input("Please enter a command: ")
    if command.casefold() == "help":
        print("Available Commands: newkey, findkey, finduser, delkey, editkey, settings, help")
    elif command.casefold() == "newkey":
        user_id = input("Please enter a User ID: ")
        with open("keys.json", "r") as _file:
            data = json.load(_file)
        if user_id in data:
            override_confirmation = input("WARNING: A key already exists for this User ID! Would you like to continue? (Y/N) > ")
            if override_confirmation.casefold() == "y":
                if "yes" in data.get("settingsautogeneratekey"):
                    create_key(secrets.token_hex(16))
                elif "ask" in data.get("settingsautogeneratekey"):
                    ask_to_generate = input("Would you like to generate this key automatically or input the key manually?\n1: Generate Automatically\n2: Input Manually\n> ")
                    if ask_to_generate == "1":
                        create_key(secrets.token_hex(16))
                    elif ask_to_generate == "2":
                        key_update = input("Please enter a new key: ")
                        create_key(key_update)
                    else:
                        print("Invalid Option!")
                elif "no" in data.get("settingsautogeneratekey"):
                    key_update = input("Please enter a new key: ")
                    create_key(key_update)
                else:
                    create_file_data()
            elif override_confirmation.casefold() == "n":
                print("Operation cancelled!")
            else:
                print("Invalid option!")
        else:
            if "yes" in data.get("settingsautogeneratekey"):
                create_key(secrets.token_hex(16))
            elif "ask" in data.get("settingsautogeneratekey"):
                ask_to_generate = input("Would you like to generate this key automatically or input the key manually?\n1: Generate Automatically\n2: Input Manually\n> ")
                if ask_to_generate == "1":
                    create_key(secrets.token_hex(16))
                elif ask_to_generate == "2":
                    key_update = input("Please enter a new key: ")
                    create_key(key_update)
                else:
                    print("Invalid Option!")
            elif "no" in data.get("settingsautogeneratekey"):
                key_update = input("Please enter a new key: ")
                create_key(key_update)
            else:
                create_file_data()
    elif command.casefold() == "findkey":
        find_key()
    elif command.casefold() == "finduser":
        find_user()
    elif command.casefold() == "editkey":
        edit_key()
    elif command.casefold() == "deletekey" or command.casefold() == "delkey":
        delete_key()
    elif command.casefold() == "settings":
        settings_choice = input("Please enter an option:\nautogeneratekey, exit\n> ")
        if settings_choice == "autogeneratekey":
            create_file_data()
        elif settings_choice == "exit":
            print("Done!")
        else:
            print("Invalid option!")
    elif command.casefold() == "exit":
        exit()
    else:
        print("Invalid command!")
