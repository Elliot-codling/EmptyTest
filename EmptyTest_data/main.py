#CREATED BY ELLIOT CODLING
import pygame, os

print("hello this is a change. :)")
file_dir = os.getcwd() # get the current directory
pygame.font.init()

from engine import game_engine_004 as game_engine

# create window ---------------------------------
w, h = 780, 780
window = game_engine.update.define("Empty Test", w, h)

#borders to stop moving off screen
left_border = 40
right_border = w - 40
top_border = 40
bottom_border = h - 40
# -----------------------------------------------
#create variable stuff
clock = pygame.time.Clock()
gameplay = True
vel = 10

#background
display = []
#object_head_texture = pygame.image.load("{}/textures/object_head.png".format(file_dir))
#object_head = game_engine.properties_object(name, object_head_texture, x, y, width, height, alpha)
#dispay += [object_head]

#display sprites
display_sprite = []

#foreground
foreground = []

#text_foreground
text_foreground = []


# main game function --------------------------------------------------------------
def main_game(object_head, vel):
    #EXAMPLES  
    if keys[pygame.K_LEFT]:
        object_head = game_engine.player.left(object_head, vel, left_border)
    elif keys[pygame.K_RIGHT]:
        object_head = game_engine.player.right(object_head, vel, right_border)
# ---------------------------------------------------------------------------------

# main game loop ------------------------------------------------------------------
run = True
while run:
    # keyboard and exit button, main code -----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if not gameplay:
        run = False
    else:
        main_game(object_head, vel)

    #exit
    if keys[pygame.K_ESCAPE]:
        run = False

    #game_engine.update.list_debug(display, display_sprite, foreground, text_foreground, clock)     #uncomment to debug
    # update screen
    game_engine.update.window(window, display, display_sprite, foreground, text_foreground, clock, False)     #update the window
    clock.tick(60)  #limit to 60 fps

pygame.quit()
