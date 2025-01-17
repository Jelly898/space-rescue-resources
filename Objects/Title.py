from GameFrame import RoomObject
import pygame

class Title(RoomObject):



    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        #Set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)

        #Register for key events
        self.handle_key_events = True

    def key_pressed(self, key):
        """
        If the key pressed is space the game will start
        """

        if key[pygame.K_SPACE]:
            self.room.running = False