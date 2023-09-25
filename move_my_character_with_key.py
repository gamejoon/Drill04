from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

running = True

background = load_image("TUK_GROUND.png")

character = load_image("animation_sheet.png")
character_dir = "UNMOVE"
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
coordinate = (((3, 47, 437, 493), (61, 104, 437, 493), (119, 162, 437, 493)),
              ((1, 50, 2, 55), (63, 110, 2, 55), (121, 167, 2, 55), (176, 223, 0, 53), (228, 285, 0, 53), (292, 341, 2, 55), (350, 396, 2, 55), (412, 459, 6, 55), (470, 517, 2, 53), (518, 574, 0, 53)),
              ((1, 57, 124, 178), (60, 107, 127, 178), (116, 163, 131, 180), (176, 223, 127, 180), (234, 284, 127, 180), (289, 346, 124, 178), (349, 396, 124, 178), (408, 453, 129, 180), (467, 514, 129, 180), (523, 572, 127, 180)))

frame = 0
acceleration = [0, 0]

def character_motion(dir):

    global frame, x, y

    if dir == "UNMOVE":
        character.clip_draw(coordinate[0][frame][0], coordinate[0][frame][2], (coordinate[0][frame][1] - coordinate[0][frame][0]), (coordinate[0][frame][3] - coordinate[0][frame][2]), x, y)
        frame = (frame + 1) % 3
    elif dir == "RIGHT":
        character.clip_draw(coordinate[1][frame][0], coordinate[1][frame][2], (coordinate[1][frame][1] - coordinate[1][frame][0]), (coordinate[1][frame][3] - coordinate[1][frame][2]), x, y)
        frame = (frame + 1) % 10
    elif dir == "LEFT":
        print("left")
        character.clip_draw(coordinate[2][frame][0], coordinate[2][frame][2], (coordinate[2][frame][1] - coordinate[2][frame][0]), (coordinate[2][frame][3] - coordinate[2][frame][2]), x, y)
        frame = (frame + 1) % 10
    elif dir == "UP":
        print("up")
    elif dir == "DOWN":
        print("down")

def handle_events():

    global running, character_dir, frame, acceleration

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                character_dir = "RIGHT"
                acceleration[0] = 10
            elif event.key == SDLK_LEFT:
                character_dir = "LEFT"
                acceleration[0] = -10
            elif event.key == SDLK_UP:
                character_dir = "UP"
            elif event.key == SDLK_DOWN:
                character_dir = "DOWN"
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                character_dir = "UNMOVE"
                frame = 0
                acceleration[0] = 0
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                character_dir = "UNMOVE"
                frame = 0
                acceleration[1] = 0

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

    character_motion(character_dir)
    update_canvas()
    delay(0.05)

close_canvas()