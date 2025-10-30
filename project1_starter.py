"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Kimora James
Date: October 2025

AI Usage:
AI assistance used for logic verification and test alignment (no code copied directly).
"""

import os

def calculate_stats(character_class, level):
    """Calculates base stats based on class and level."""
    if character_class is None:
        return (0, 0, 0)
    cls = character_class.lower()
    if cls == "warrior":
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
    return (strength, magic, health)


def create_character(name, character_class):
    """Creates a new character dictionary with calculated stats."""
    if name is None or name == "" or character_class is None:
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
    return character


def save_character(character, filename):
    """Saves character to a text file in the required format."""
    if character is None or filename is None or filename == "":
        return False

    # Check if directory exists
    parts = filename.split("/")
    if len(parts) > 1:
        directory = "/".join(parts[:-1])
        if directory != "" and not os.path.exists(directory):
            return False

    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True


def load_character(filename):
    """Loads a character from a text file and returns a dictionary."""
    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    char = {}
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
    return char


def display_character(character):
    """Prints formatted character info."""
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
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "testhero.txt")
    loaded = load_character("testhero.txt")
    print("\nLoaded:")
    display_character(loaded)
    level_up(loaded)
    print("\nAfter level up:")
    display_character(loaded)
