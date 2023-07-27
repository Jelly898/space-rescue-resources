from GameFrame import RoomObject, Globals
import pygame

class Ship(RoomObject):
    """
    A class for the player's avitar (the Ship)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the Ship object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Ship.png")
        self.set_image(image,100,100)

        #Register events
        self.handle_key_events = True

    def key_pressed(self, key):
        """
        Responds to key press up and down
        """

        if key[pygame.K_w]:
            self.y_speed -= 10
        elif key[pygame.K_s]:
            self.y_speed += 10

    def keep_in_room(self):
        #Keeps ship in room


        if self.y < 0:
            self.y = 0
        elif self.y + self.height> Globals.SCREEN_HEIGHT:
            self.y = Globals.SCREEN_HEIGHT - self.height

    def step(self):
        #Determines what happens to the ship  on each click of the game clock


        self.keep_in_room()