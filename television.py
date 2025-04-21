import re

def bucket_of(said):
    # Convert the input string to lowercase for case-insensitive matching
    lower_said = said.lower()

    # Define the trigger words/phrases
    water_triggers = ["water", "wet", "wash"]
    slime_triggers = ["i don't know", "slime"]

    # Flags to track if triggers were found
    found_water = False
    found_slime = False

    # Check for water triggers (any form)
    # Using 'in' checks for substrings, covering variations like "watering", "washed" etc.
    for trigger in water_triggers:
        if trigger in lower_said:
            found_water = True
            break # Found one, no need to check others

    # Check for slime triggers
    for trigger in slime_triggers:
        if trigger in lower_said:
            found_slime = True
            break # Found one, no need to check others

    # Determine the outcome based on the flags
    if found_water and found_slime:
        return "sludge"
    elif found_water:
        return "water"
    elif found_slime:
        return "slime"
    else:
        return "air"
