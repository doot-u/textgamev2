class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None
        self.item = None

    #method that sets description of the cave
    def set_description(self, cave_description):
        self.description = cave_description

    #method that gets description of the cave
    def get_description(self):
        return self.description
    
    #method that gets name of the cave
    def get_name(self):
        return self.name

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character
    
    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    #method that describes the current cave
    def describe(self):
        print(self.description)

    #method that links the caves to each other with a direction
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link
    
    #method that prints the caves connected to current and direction
    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)
    
    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self