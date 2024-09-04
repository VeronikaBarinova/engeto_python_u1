"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Barinova
email: veronika.barina@gmail.com
discord: veronikabarinova_30716 (not use too much)
"""
from task_template import TEXTS
import math

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

stats = {
    "words": 0,
    "titlecase": 0,
    "uppercase": 0,
    "lowercase": 0,
    "numeric": 0,
    "sum": 0,
    "word_lengths": {}
}

def login(users, text_length) -> str:
    username = input("username: ")
    password = input("password: ")
    if users.get(username) == password:
        print("-" * 40)
        print(f"Welcome to the app, {username}")
        print(f"We have {text_length} texts to be analyzed.")
        print("-" * 40)
        return username
    else:
        print("unregistered user, terminating the program..")
        exit(-1)

def get_text_choice() -> int:
    text_size:int = len(TEXTS)
    choice = input(f"Enter a number btw. 1 and {text_size} to select: ")
    if not choice.isnumeric() or int(choice) not in range(1, text_size + 1):
        print("Invalid choice, terminating the program..")
        exit(-1)
    return int(choice)
    

def analyze_text(text:str, stats: dict) -> dict:
    words = text.split()
    stats["words"] = len(words)
    words = [word.strip(".,") for word in words]
    for word in words:
        if word.istitle():
            stats["titlecase"] += 1
        if word.isupper() and word.isalpha():
            stats["uppercase"] += 1
        if word.islower() and word.isalpha():
            stats["lowercase"] += 1
        if word.isnumeric():
            stats["numeric"] += 1
            stats["sum"] += int(word)
    
    word_histogram = {}
    for word in words:
        word_histogram[len(word)] = word_histogram.get(len(word), 0) + 1

    stats["word_lengths"] = word_histogram
    return stats

def dump_stats(stats) -> None:
    max_length = max(stats["word_lengths"].values())

    print("-" * 40)
    print(f"There are {stats['words']} words in the selected text.")
    print(f"There are {stats['titlecase']} titlecase words.")
    print(f"There are {stats['uppercase']} uppercase words.")
    print(f"There are {stats['lowercase']} lowercase words.")
    print(f"There are {stats['numeric']} numeric strings.")
    print(f"The sum of all numbers {stats['sum']}")    
    print("-" * 40)
    print(f"LEN | {'OCCURENCES':<{max_length}} | NR.")
    print("-" * 40)

    for length, occurences in sorted(stats["word_lengths"].items()):        
        print(f"{length:3} | {'*' * occurences:<{max_length}} | {occurences}")

    
if __name__ == "__main__":
    user = login(users, len(TEXTS))
    choice = get_text_choice()
    stats = analyze_text(TEXTS[choice-1], stats) 
    dump_stats(stats)