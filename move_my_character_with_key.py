from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

running = True

background = load_image("TUK_GROUND.png")

character = load_image("animation_sheet.png")
character_dir = "UNMOVE"
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
coordinate = ((((3,47), (61, 104), (119, 162)), (500 - 6 - 1, 500 - 62 - 1)),
              (((1, 50), (63, 110), (121, 167), (176, 223), (228, 285), (292, 341), (350, 396), (412, 459), (470, 517), (518, 574)), (500 - 444 - 1, 500 - 499 - 1)))

frame = 0

def character_motion(dir):

    global frame, x, y

    if dir == "UNMOVE":
        character.clip_draw(coordinate[0][0][frame][0], coordinate[0][1][1], (coordinate[0][0][frame][1] - coordinate[0][0][frame][0]), (coordinate[0][1][0] - coordinate[0][1][1]), x, y)
        frame = (frame + 1) % 3
    elif dir == "RIGHT":
        print("right")
        #character.clip_draw(coordinate[1][0][frame][0], coordinate[1][1][1], ())
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
    delay(0.05)

close_canvas()