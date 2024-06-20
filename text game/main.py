from cave import Cave
from character import Enemy
from item import Item

#describing the cavern
cavern = Cave("cavern")
cavern.set_description("You're in a damp and dirty cave")

#describing the dungeon
dungeon = Cave("dungeon")
dungeon.set_description("You're in a large cave with a rack against the wall")

#describing the grotto
grotto = Cave("grotto")
grotto.set_description("You're in a small cave with ancient graffiti")

#linking each part of the cave to each other
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")
dungeon.link_cave(cavern, "north")
enemy1 = Enemy("Stirling", "A being made from pure light.")
enemy1.set_conversation("WHAT")
enemy1.set_weakness("camera")
dungeon.set_character(enemy1)

camera = Item("camera")
camera.set_description("A monster's worst nightmare")
grotto.set_item(camera)
torch = Item("torch")
torch.set_description("A light for the end of the tunnel")
dungeon.set_item(torch)
bag = []

current_cave = cavern

end = False

#beginning message
print("Hello, world!")
print("Your objective is to defeat the evil monsters that lurk in these caves.")
print("Say a direction to move, say 'take' to take an item, and say 'fight' to fight a monster.")

#main game loop
while end == False:
    print("\n")
    current_cave.describe()
    inhabitant = current_cave.get_character()
    item = current_cave.get_item()
    current_cave.get_details()

    if inhabitant is not None:
        inhabitant.describe()

    if item is not None:
        item.describe()    

    command = input(">")

    if command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
            
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("what will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with) == True:
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("You cleared the dungeon of all the enemies. You win!")
                        end = True
                else:
                    print("You lost.")
                    print("You're dead now.")
                    end = True
            else:
                print("You dont have a " + fight_with)
    
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I highly advise against it.")
            else:
                inhabitant.pat()
        else:
            print("There's no one here to pat. :(")
    
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)

    else:
        current_cave = current_cave.move(command)