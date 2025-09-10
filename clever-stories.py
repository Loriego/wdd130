import random

def get_input(prompt):
    """Helper to prevent empty inputs"""
    word = ""
    while not word.strip():
        word = input(prompt)
    return word

def play_game():
    print("\n🌟 Welcome to the Creative Mad Libs Generator! 🌟")
    print("Please enter the following words to build your hilarious story:\n")

    adjective = get_input("Adjective: ")
    animal = get_input("Animal: ")
    verb1 = get_input("Verb: ")
    exclamation = get_input("Exclamation: ").capitalize()
    verb2 = get_input("Verb: ")
    verb3 = get_input("Verb: ")
    color = get_input("Color: ")
    place = get_input("Place: ")

    # Extra creative additions
    superpower = get_input("Superpower (e.g., flying, invisibility): ")
    friend_name = get_input("Name of a friend: ")
    food = get_input("Favorite food: ")
    magical_item = get_input("A magical object (e.g., wand, sword, hat): ")
    sound = get_input("A funny sound (e.g., 'boing', 'whoosh'): ")

    # Multiple story templates
    templates = [
        f"\nOne day, I saw a {adjective} {animal} that {verb1} through {place}. "
        f"\"{exclamation}!\" I shouted, as I tried to {verb2}. "
        f"Luckily, {friend_name} appeared, wielding a {magical_item}, and with their {superpower} powers "
        f"they saved me. The {color} {animal} made a loud \"{sound}\" and ran away. "
        f"We celebrated with some {food}!",

        f"\nIn the middle of {place}, a {color} {animal} suddenly appeared. "
        f"It tried to {verb3}, but I yelled \"{exclamation}!\" and {verb2} as fast as I could. "
        f"Out of nowhere, {friend_name} flew in using their {superpower} skills, "
        f"and dropped a {magical_item} that scared the animal. "
        f"It vanished with a \"{sound}\" and we ate {food} happily ever after.",

        f"\nIt was a {adjective} morning when a {animal} {verb1} past me. "
        f"Before I could react, it tried to {verb3} inside {place}! "
        f"{friend_name} appeared, holding a {magical_item}, and shouted \"{exclamation}!\". "
        f"Their {superpower} powers defeated the beast. "
        f"The {color} {animal} disappeared in a puff of smoke saying \"{sound}\". "
        f"That day, {food} became the official victory meal."
    ]

    # Randomly choose one story
    story = random.choice(templates)

    print("\n✨ Your Crazy Story ✨\n")
    print(story)
    print("\n🌟 The End 🌟\n")

# Main loop
while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("\nThanks for playing! Come back for more fun stories 🤩\n")
        break
