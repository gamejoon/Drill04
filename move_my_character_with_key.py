from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("animation_sheet.png")
background = load_image("TUK_GROUND.png")


running = True

def character_motion():
    pass

def handle_events():
    pass

while running:
    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    update_canvas()
    delay(0.01)