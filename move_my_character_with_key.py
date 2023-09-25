from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

running = True

background = load_image("TUK_GROUND.png")

character = load_image("animation_sheet.png")
character_dir = {"DOWN_UNMOVE" : 0, "DOWN" : 1, "UP_UNMOVE" : 2, "UP" : 3, "RIGHT_UNMOVE" : 4, "RIGHT" : 5, "LEFT_UNMOVE" : 6, "LEFT" : 7}
dir = character_dir["DOWN_UNMOVE"]
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

coordinate = (((3, 47, 437, 493), (61, 104, 437, 493), (119, 162, 437, 493)),
              ((5, 49, 187, 243), (63, 107, 192, 245), (121, 165, 187, 245), (179, 223, 187, 245), (236, 281, 187, 245), (294, 339, 187, 243), (352, 396, 192, 245), (410, 454, 187, 245), (467, 512, 187, 245), (525, 569, 187, 245)),
              ((5, 49, 312, 363), (5, 49, 312, 363), (5, 49, 312, 363)), # 똑같은 그림 3개
              ((5, 49, 66, 120), (63, 107, 66, 120), (121, 165, 66, 125), (179, 223, 66, 125), (237, 281, 66, 125), (294, 339, 66, 120), (352, 396, 66, 120), (410, 454, 66, 125), (468, 512, 64, 122), (526, 570, 66, 125)),
              ((5, 47, 249, 303), (61, 102, 249, 303), (120, 163, 249, 303)),
              ((1, 50, 2, 55), (63, 110, 2, 55), (121, 167, 2, 55), (176, 223, 0, 53), (228, 285, 0, 53), (292, 341, 2, 55), (350, 396, 2, 55), (412, 459, 6, 55), (470, 517, 2, 53), (518, 574, 0, 53)),
              ((8, 49, 374, 428), (65, 107, 374, 428), (124, 165, 374, 428)),
              ((1, 57, 124, 178), (60, 107, 127, 178), (116, 163, 131, 180), (176, 223, 127, 180), (234, 284, 127, 180), (289, 346, 124, 178), (349, 396, 124, 178), (408, 453, 129, 180), (467, 514, 129, 180), (523, 572, 127, 180)))

frame = 0
acceleration = [0, 0]

def character_motion():

    global frame, x, y

    character.clip_draw(coordinate[dir][frame][0], coordinate[dir][frame][2], (coordinate[dir][frame][1] - coordinate[dir][frame][0]), (coordinate[dir][frame][3] - coordinate[dir][frame][2]), x, y)
    frame = (frame + 1) % len(coordinate[dir])
    
def handle_events():

    global running, dir, frame, acceleration

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_UP:
                dir = character_dir["UP"]
                acceleration[1] = 10
            elif event.key == SDLK_DOWN:
                dir = character_dir["DOWN"]
                acceleration[1] = -10
            elif event.key == SDLK_RIGHT:
                dir = character_dir["RIGHT"]
                acceleration[0] = 10
            elif event.key == SDLK_LEFT:
                dir = character_dir["LEFT"]
                acceleration[0] = -10
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP:
                dir = character_dir["UP_UNMOVE"]
                frame = 0
                acceleration[1] = 0
            elif event.key == SDLK_DOWN:
                dir = character_dir["DOWN_UNMOVE"]
                frame = 0
                acceleration[1] = 0
            elif event.key == SDLK_RIGHT:
                dir = character_dir["RIGHT_UNMOVE"]
                frame = 0
                acceleration[0] = 0
            elif event.key == SDLK_LEFT:
                dir = character_dir["LEFT_UNMOVE"]
                frame = 0
                acceleration[0] = 0

while running:
    clear_canvas()
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_events()
    x += acceleration[0]
    y += acceleration[1]

    if x + 23 > TUK_WIDTH - 1:
        x = TUK_WIDTH - 1 - 23
    elif x - 23 < 0:
        x = 0 + 23
    elif y + 27 > TUK_HEIGHT - 1:
        y = TUK_HEIGHT - 1 - 27 
    elif y - 27 < 0:
        y = 0 + 27

    character_motion()
    update_canvas()
    delay(0.05)

close_canvas()