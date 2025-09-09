# Mad Libs Story Generator
# This program asks the user for words and builds a fun story.
# Extra creative additions: user can enter a friend's name and a superpower,
# which are included in the story to make it unique and personalized.

print("Please enter the following words to build your story:")

adjective = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb: ")
exclamation = input("Exclamation: ").capitalize()
verb2 = input("Verb: ")
verb3 = input("Verb: ")
color = input("Color: ")   
place = input("Place: ")   

# Creative additions
superpower = input("Superpower (e.g., flying, invisibility): ")  # <-- creative addition
friend_name = input("Name of a friend: ")  # <-- creative addition

# Build the story
story = (
    f"\nThe other day, I was really in trouble. It all started when I saw a very {adjective} {animal}.\n"
    f"It {verb1} down the hallway. \"{exclamation}!\" I yelled.\n"
    f"But all I could think to do was to {verb2} over and over.\n"
    f"Miraculously, that caused it to stop, but not before it tried to {verb3} "
    f"right in front of my family.\n"
    f"Then, my best friend {friend_name} appeared and used their {superpower} powers "
    f"to help save the day.\n"
    f"In the end, the {color} {animal} ran away and disappeared into {place}.\n"
)

# Output the story
print("\nYour story is:\n")
print(story)