from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("animation_sheet.png")
background = load_image("TUK_GROUND.png")

running = True
character_dir = "UNMOVE"

def character_motion(dir):
    if dir == "UNMOVE":
        print("unmove")
    elif dir == "RIGHT":
        print("right")
    elif dir == "LEFT":
        print("left")
    elif dir == "UP":
        print("up")
    elif dir == "DOWN":
        print("down")

def handle_events():

    global running, character_dir

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                character_dir = "RIGHT"
            elif event.key == SDLK_LEFT:
                character_dir = "LEFT"
            elif event.key == SDLK_UP:
                character_dir = "UP"
            elif event.key == SDLK_DOWN:
                character_dir = "DOWN"
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT or event.key == SDLK_UP or event.key == SDLK_DOWN:
                character_dir = "UNMOVE"

while running:
    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    character_motion(character_dir)
    update_canvas()
    delay(0.01)

close_canvas()