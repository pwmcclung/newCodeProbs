class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()  

    def how_many(self, new_listeners):
        new_listener_count = 0
        for listener in new_listeners:
            lower_listener = listener.lower() 
            if lower_listener not in self.listeners:
                new_listener_count += 1
                self.listeners.add(lower_listener)
        return new_listener_count