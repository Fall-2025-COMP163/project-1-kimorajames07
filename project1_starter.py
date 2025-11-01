"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kimora James
Date: October 2025

AI Usage:
AI assistance used for logic verification and test alignment (no code copied directly).
"""

import os #imports os module

def calculate_stats(character_class, level):
    """Calculates base stats based on class and level."""
    if character_class is None:
        return (0, 0, 0)
    cls = character_class.lower() # makes the name lowercase
    if cls == "warrior":          #checks the class to assign different stats
        strength = 10 + level * 3
        magic = 2 + level
        health = 100 + level * 10
    elif cls == "mage":
        strength = 3 + level
        magic = 15 + level * 3
        health = 80 + level * 5
    elif cls == "rogue":
        strength = 7 + level * 2
        magic = 7 + level * 2
        health = 70 + level * 5
    elif cls == "cleric":
        strength = 6 + level * 2
        magic = 12 + level * 2
        health = 90 + level * 8
    else:
        strength = 5 + level
        magic = 5 + level
        health = 50 + level * 5
    return (strength, magic, health) #returns those numbers and sends a tuple back to who called the function 


def create_character(name, character_class): # new function
    """Creates a new character dictionary with calculated stats."""
    if name is None or name == "" or character_class is None: #if none it's invalid
        return None
    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character #returns dictionary
#starts at level 1 and calls the previous function to get stats 

def save_character(character, filename): #if no character or filename is given, don't save
    """Saves character to a text file in the required format."""
    if character is None or filename is None or filename == "":
        return False

    # Check if directory exists
    parts = filename.split("/") #seperates file name via "/" if its lengrth is more than one than you join it at the last indeex
    if len(parts) > 1:
        directory = "/".join(parts[:-1])
        if directory != "" and not os.path.exists(directory):
            return False

    file = open(filename, "w") #opens and creates file for writting(overwrites)
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True #closes the file and checks the text format and the true return value


def load_character(filename): #recreates the character dictionary
    """Loads a character from a text file and returns a dictionary."""
    if not os.path.exists(filename): #if file doesn't exist
        return None

    file = open(filename, "r") #opens file for reading and reads all the lines into a list, string
    lines = file.readlines()
    file.close() #closes

    char = {}                # goes throuugh each line , removes newlines, and splits into key and parts
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key, value = parts
            if key == "Character Name":
                char["name"] = value
            elif key == "Class":
                char["class"] = value
            elif key == "Level":
                char["level"] = int(value)
            elif key == "Strength":
                char["strength"] = int(value)
            elif key == "Magic":
                char["magic"] = int(value)
            elif key == "Health":
                char["health"] = int(value)
            elif key == "Gold":
                char["gold"] = int(value)
    return char #returns itb& its the same dictionary


def display_character(character):
    """Prints formatted character info.""" #printing
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    return None


def level_up(character):
    """Increases level and recalculates stats."""
    character["level"] = character["level"] + 1
    s, m, h = calculate_stats(character["class"], character["level"])
    character["strength"] = s
    character["magic"] = m
    character["health"] = h
    return None


# Optional test block
if __name__ == "__main__":
    char = create_character("TestHero", "Warrior") #runs when you run the file directly
    display_character(char)
    save_character(char, "testhero.txt")
    loaded = load_character("testhero.txt")
    print("\nLoaded:")
    display_character(loaded)
    level_up(loaded)
    print("\nAfter level up:")
    display_character(loaded)
