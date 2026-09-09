import json
import webbrowser


def load_custom_commands():

    try:
        with open("config.json", "r", encoding="utf-8") as file:
            config = json.load(file)

        return config.get("custom_commands", {})

    except FileNotFoundError:
        return {}


def execute_custom_command(command):

    custom_commands = load_custom_commands()

    for key, url in custom_commands.items():

        if key.lower() in command.lower():

            webbrowser.open(url)

            return True

    return False 