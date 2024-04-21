from tkinter import *
import random

game_window_width = 700
game_window_height = 700
game_speed = 50
game_space_size = 50
game_body_parts = 3
game_background_color = "#000000"
snake_color = "#00FF00"
snake_food_color = "#FF0000"


class Snake:

    def __init__(self):
        self.body_size = game_body_parts
        self.coordinates = []
        self.squares = []

        for i in range(0, game_body_parts):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + game_space_size, y + game_space_size, fill=snake_color, tags="Snake")
            self.squares.append(square)

class Food:

    def __init__(self):

        x = random.randint(0, (game_window_width / game_space_size) - 1) * game_space_size
        y = random.randint(0, (game_window_height / game_space_size) - 1) * game_space_size

        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + game_space_size, y + game_space_size, fill=snake_food_color, tags="Food")

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= game_space_size
    elif direction == "down":
        y += game_space_size
    elif direction == "left":
        x -= game_space_size
    elif direction == "right":
        x += game_space_size

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + game_space_size, y + game_space_size, fill=snake_color)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score += 1
        label.config(text="Score: {}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        del  snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(game_speed, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collisions():

    pass

def game_over():

    pass

window = Tk()
window.title("Snake")
window.resizable(False, False)

score = 0
direction = "down"

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=game_background_color, height=game_window_height, width=game_window_width)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()