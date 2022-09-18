#  Copyright (c) 2022.

class animation_no_collision:

    def __init__(self, screen, resource):
        self.screen = screen
        # get preloaded Animation images as list
        self.animation = resource.load_animation
        # decides index of self.animation
        self.frame = 0

    def draw(self, pos=(0, 0)):
        if self.frame < len(self.animation):
            self.screen.blit(self.animation[self.frame], pos)
        if self.frame >= len(self.animation):
            self.frame = -1

    def tick(self):
        self.frame += 1
