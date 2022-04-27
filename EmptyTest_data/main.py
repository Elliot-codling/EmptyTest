#CREATED BY ELLIOT CODLING
import pygame, os, sys



file_dir = os.getcwd() # get the current directory
pygame.font.init()
#import the engine path file
sys.path.append("{}/EmptyTest_data/engine".format(file_dir))
import game_engine_004 as game_engine

# create window ---------------------------------
w, h = 780, 780
window = game_engine.update.define("Snake Game", w, h)

left_border = 40
right_border = w - 40
top_border = 40
bottom_border = h - 40
# -----------------------------------------------

#create variable stuff
clock = pygame.time.Clock()
gameplay = True
direction = ""      #set player direction should be constant moving in
points = 0      #score
snake_body_count = 0    #amount of snake bodies
angle = 0       #angle of the player to know how much to rotate the player
offset = 0      #when to change the index to find next lowest ID in snake_body
vel = 10


#background
display = []
background_texture = pygame.image.load("{}/EmptyTest_data/textures/background.png".format(file_dir))
background_texture = background_texture.convert()

background = game_engine.properties_object("background", background_texture, 40, 40, 704, 704, False)
display += [background]

#display sprites
display_sprite = []
snake_head_texture = pygame.image.load("{}/EmptyTest_data/textures/snake_head.png".format(file_dir))
snake_head = game_engine.properties_object("snake_head", snake_head_texture, 40, 40, 18, 18, False)

snake_body_texture = pygame.image.load("{}/EmptyTest_data/textures/snake_body.png".format(file_dir))
snake_body = game_engine.properties_object("snake_body", snake_body_texture, 0, 0, 16, 16, False)

apple_texture = pygame.image.load("{}/EmptyTest_data/textures/apple.png".format(file_dir))
apple = game_engine.properties_object("apple", apple_texture, 0, 0, 18, 18, True)

display_sprite += [snake_head]

#foreground
foreground = []

grass_top_texture = pygame.image.load("{}/EmptyTest_data/textures/grass_top.png".format(file_dir))
grass_top = game_engine.properties_object("grass_top", grass_top_texture, 0, 0, 780, 40, False)

grass_bottom_texture = pygame.image.load("{}/EmptyTest_data/textures/grass_bottom.png".format(file_dir))
grass_bottom = game_engine.properties_object("grass_bottom", grass_bottom_texture, 0, 742, 780, 40, False)

grass_left_texture = pygame.image.load("{}/EmptyTest_data/textures/grass_left.png".format(file_dir))
grass_left = game_engine.properties_object("grass_left", grass_left_texture, 0, 0, 40, 780, False)

grass_right_texture = pygame.image.load("{}/EmptyTest_data/textures/grass_right.png".format(file_dir))
grass_right = game_engine.properties_object("grass_right", grass_right_texture, 742, 0, 40, 780, False)

foreground += [grass_top]
foreground += [grass_bottom]
foreground += [grass_left]
foreground += [grass_right]


#text_foreground
text_foreground = []
font = pygame.font.SysFont(None, 30)
score_text_texture = font.render("Score: 0", True, pygame.Color("Yellow"))
score_text = game_engine.properties_text("score", score_text_texture, 20, 20)
text_foreground += [score_text]

# main game function --------------------------------------------------------------
def main_game(snake_head, vel):
    if keys[pygame.K_LEFT]:
        snake_head = game_engine.player.left(snake_head, vel, left_border)
    elif keys[pygame.K_RIGHT]:
        snake_head = game_engine.player.right(snake_head, vel, right_border)
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
        main_game(snake_head, vel)

    #exit
    if keys[pygame.K_ESCAPE]:
        run = False

    #game_engine.update.list_debug(display, display_sprite, foreground, text_foreground, clock)
    # -----------------------------------------------------------------
    # update screen
    
    game_engine.update.window(window, display, display_sprite, foreground, text_foreground, clock, True)     #update the window
    clock.tick(10)  #limit to 10 fps

pygame.quit()