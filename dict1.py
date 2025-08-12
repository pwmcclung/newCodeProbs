class Dictionary():
    def __init__(self):
        # Use a dictionary to store word-definition pairs.
        self.entries = {}

    def newentry(self, word, definition):
        # Add the word and definition to the dictionary.
        self.entries[word] = definition

    def look(self, key):
        # Check if the key (word) exists in the dictionary.
        if key in self.entries:
            # Return the definition if found.
            return self.entries[key]
        else:
            # Return the specified message if not found.
            return "Can't find entry for " + key