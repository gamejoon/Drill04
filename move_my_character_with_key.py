from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("animation_sheet.png")
background = load_image("TUK_GROUND.png")

running = True

def character_motion():
    pass

def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        

while running:
    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    update_canvas()
    delay(0.01)

close_canvas()