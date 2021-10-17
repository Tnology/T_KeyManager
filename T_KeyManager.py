import json
import secrets

check_number = 0

version = "1.5.2"

try:
    file = open("keys.json", "r+")
except FileNotFoundError:
    file = open("keys.json", "x")
    file.close()
    file = open("keys.json", "r+")

if len(file.readlines()) == 0:
    file.write("{\"placeholderusername1\": \"pleasedonotremovethese!\", \"settingsautogeneratekey\": \"yes\"}")
    print("It looks like no file data has been detected! We will generate file data for you!\n")
    choice_number = 0
    while choice_number == 0:
        auto_generate_key = input("How would you like new keys to be made (can be changed later with the \'settings\' command)?\n1: Generate one for me\n2: Ask me every time\n3: Manually enter a key each time\n> ")
        if auto_generate_key == "1":
            file.seek(0)
            data = json.load(file)
            data.update({"settingsautogeneratekey": "yes"})
            file.close()
            file = open("keys.json", "w")
            file.truncate(0)
            file.close()
            file = open("keys.json", "r+")
            json.dump(data, file)
            file.close()
            print("Done!")
            file = open("keys.json", "r+")
            choice_number += 1
        elif auto_generate_key == "2":
            file.seek(0)
            data = json.load(file)
            data.update({"settingsautogeneratekey": "ask"})
            file.close()
            file = open("keys.json", "w")
            file.truncate(0)
            file.close()
            file = open("keys.json", "r+")
            json.dump(data, file)
            file.close()
            print("Done!")
            file = open("keys.json", "r+")
            choice_number += 1
        elif auto_generate_key == "3":
            file.seek(0)
            data = json.load(file)
            data.update({"settingsautogeneratekey": "no"})
            file.close()
            file = open("keys.json", "w")
            file.truncate(0)
            file.close()
            file = open("keys.json", "r+")
            json.dump(data, file)
            file.close()
            print("Done!")
            file = open("keys.json", "r+")
            choice_number += 1
        else:
            print("Invalid Option, please choose again.")
else:
    print("File Data Detected! Continuing!")

file.seek(0)

data = json.load(file)

while check_number == 0:
    command = input("Please enter a command: ")
    if command.lower() == "help":
        print("Available Commands: newkey, findkey, finduser, delkey, editkey, settings, help")
    elif command.lower() == "newkey":
        user_id = input("Please enter a User ID: ")
        if user_id in data:
            override_confirmation = input("WARNING: A key already exists for this User ID! Would you like to continue? (Y/N) > ")
            if override_confirmation.lower() == "y":
                if "yes" in data.get("settingsautogeneratekey"):
                    data.update({user_id: secrets.token_hex(16)})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                elif "ask" in data.get("settingsautogeneratekey"):
                    ask_to_generate = input(
                        "Would you like to generate this key automatically or input the key manually?\n1: Generate Automatically\n2: Input Manually\n> ")
                    if ask_to_generate == "1":
                        data.update({user_id: secrets.token_hex(16)})
                        file.close()
                        file = open("keys.json", "w")
                        file.truncate(0)
                        file.close()
                        file = open("keys.json", "r+")
                        json.dump(data, file)
                        file.close()
                        print("Done!")
                        file = open("keys.json", "r+")
                    elif ask_to_generate == "2":
                        key_update = input("Please enter a new key: ")
                        data.update({user_id: key_update})
                        file.close()
                        file = open("keys.json", "w")
                        file.truncate(0)
                        file.close()
                        file = open("keys.json", "r+")
                        json.dump(data, file)
                        file.close()
                        print("Done!")
                        file = open("keys.json", "r+")
                    else:
                        print("Invalid Option!")
                elif "no" in data.get("settingsautogeneratekey"):
                    key_update = input("Please enter a new key: ")
                    data.update({user_id: key_update})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                else:
                    print("Oops! It looks like you have invalid file data. We are automatically correcting your file data...")
                    auto_generate_key = input(
                        "How would you like new keys to be made (can be changed later with the \'settings\' command)?\n1: Generate one for me\n2: Ask me every time\n3: Manually enter a key each time\n> ")
                    if auto_generate_key == "1":
                        file.seek(0)
                        data = json.load(file)
                        data.update({"settingsautogeneratekey": "yes"})
                        file.close()
                        file = open("keys.json", "w")
                        file.truncate(0)
                        file.close()
                        file = open("keys.json", "r+")
                        json.dump(data, file)
                        file.close()
                        print("Done!")
                        file = open("keys.json", "r+")
                    elif auto_generate_key == "2":
                        file.seek(0)
                        data = json.load(file)
                        data.update({"settingsautogeneratekey": "ask"})
                        file.close()
                        file = open("keys.json", "w")
                        file.truncate(0)
                        file.close()
                        file = open("keys.json", "r+")
                        json.dump(data, file)
                        file.close()
                        print("Done!")
                        file = open("keys.json", "r+")
                    elif auto_generate_key == "3":
                        file.seek(0)
                        data = json.load(file)
                        data.update({"settingsautogeneratekey": "no"})
                        file.close()
                        file = open("keys.json", "w")
                        file.truncate(0)
                        file.close()
                        file = open("keys.json", "r+")
                        json.dump(data, file)
                        file.close()
                        print("Done!")
                        file = open("keys.json", "r+")
                    else:
                        print("Invalid option provided, choosing Option 1 automatically. THis can be changed with the \'settings\' command. ")
            elif override_confirmation.lower() == "n":
                print("Operation cancelled!")
            else:
                print("Invalid option!")
        else:
            if "yes" in data.get("settingsautogeneratekey"):
                data.update({user_id: secrets.token_hex(16)})
                file.close()
                file = open("keys.json", "w")
                file.truncate(0)
                file.close()
                file = open("keys.json", "r+")
                json.dump(data, file)
                file.close()
                print("Done!")
                file = open("keys.json", "r+")
            elif "ask" in data.get("settingsautogeneratekey"):
                ask_to_generate = input(
                    "Would you like to generate this key automatically or input the key manually?\n1: Generate Automatically\n2: Input Manually\n> ")
                if ask_to_generate == "1":
                    data.update({user_id: secrets.token_hex(16)})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                elif ask_to_generate == "2":
                    key_update = input("Please enter a new key: ")
                    data.update({user_id: key_update})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                else:
                    print("Invalid Option!")
            elif "no" in data.get("settingsautogeneratekey"):
                key_update = input("Please enter a new key: ")
                data.update({user_id: key_update})
                file.close()
                file = open("keys.json", "w")
                file.truncate(0)
                file.close()
                file = open("keys.json", "r+")
                json.dump(data, file)
                file.close()
                print("Done!")
                file = open("keys.json", "r+")
            else:
                print("Oops! It looks like you have invalid file data. We are automatically correcting your file data...")
                auto_generate_key = input("How would you like new keys to be made (can be changed later with the \'settings\' command)?\n1: Generate one for me\n2: Ask me every time\n3: Manually enter a key each time\n> ")
                if auto_generate_key == "1":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "yes"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                elif auto_generate_key == "2":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "ask"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                elif auto_generate_key == "3":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "no"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                else:
                    print("Invalid option provided, choosing Option 1 automatically. THis can be changed with the \'settings\' command. ")
    elif command.lower() == "findkey":
        user_id = input("Please enter a User ID: ")
        file.seek(0)
        data = json.load(file)
        dict_data = data
        found_number = 0
        found_line = 0
        for data_key in dict_data:
            if user_id in data_key and len(data_key) == len(user_id):
                found_line = 1
                found_key = data.get(data_key)
        if found_line == 1:
            print(found_key)
        else:
            print("User not found!")
        file.close()
        file = open("keys.json", "r+")
    elif command.lower() == "finduser":
        key_id = input("Please enter a Key: ")
        file.seek(0)
        data = json.load(file)
        dict_data = data
        found_number = 0
        try:
            found_key = list(data.keys())[list(data.values()).index(key_id)]
            found_line = 1
        except ValueError:
            found_line = 0
        if found_line == 1:
            print(found_key)
        else:
            print("Key not found!")
        file.close()
        file = open("keys.json", "r+")
    elif command.lower() == "editkey":
        user_id = input("Please enter a User ID: ")
        file.seek(0)
        data = json.load(file)
        dict_data = data
        found_number = 0
        found_line = 0
        for data_key in dict_data:
            if user_id in data_key and len(data_key) == len(user_id):
                found_line = 1
                found_key = data.get(data_key)
        if found_line == 1:
            key_update = input("Please enter a new key: ")
            data.update({user_id: key_update})
            file.close()
            file = open("keys.json", "w")
            file.truncate(0)
            file.close()
            file = open("keys.json", "r+")
            json.dump(data, file)
            file.close()
            print("Done!")
            file = open("keys.json", "r+")
        else:
            print("User not found!")
    elif command.lower() == "delkey":
            user_id = input("Please enter a User ID: ")
            try:
                override_confirmation = input("WARNING: Are you sure you want to delete this key for the user '" + user_id + "'? This action is permanent and the key will be unrecoverable. (Y/N) > ")
                if override_confirmation.lower() == "y":
                    del data[user_id]
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                elif override_confirmation.lower() == "n":
                    print("Operation cancelled!")
                else:
                    print("Invalid option!")
            except KeyError:
                print("User ID not found!")
    elif command.lower() == "settings":
        settings_choice = input("Please enter an option:\nautogeneratekey, exit\n> ")
        if settings_choice == "autogeneratekey":
            choice_number = 0
            while choice_number == 0:
                auto_generate_key = input("How would you like new keys to be made (can be changed later with the \'settings\' command)?\n1: Generate one for me\n2: Ask me every time\n3: Manually enter a key each time\n> ")
                if auto_generate_key == "1":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "yes"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                    choice_number += 1
                elif auto_generate_key == "2":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "ask"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                    choice_number += 1
                elif auto_generate_key == "3":
                    file.seek(0)
                    data = json.load(file)
                    data.update({"settingsautogeneratekey": "no"})
                    file.close()
                    file = open("keys.json", "w")
                    file.truncate(0)
                    file.close()
                    file = open("keys.json", "r+")
                    json.dump(data, file)
                    file.close()
                    print("Done!")
                    file = open("keys.json", "r+")
                    choice_number += 1
                else:
                    print("Invalid Option, please choose again.")
        elif settings_choice == "exit":
            print("Done!")
        else:
            print("Invalid Option!")
    elif command.lower() == "close":
        file.close()
        exit()
    else:
        print("Invalid command!")
