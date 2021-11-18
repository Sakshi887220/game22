"""Snake, classic arcade game.
"""

from turtle import *
from random import randrange
from base import vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
# Idea -  we will maintain a list of vectors .lenght of the snake is the number of elements in the list. 
# Last element of the list is head of the snake.
# To move the snake what we will do is append the predicted next position of head in list and delete the last position of the snake.
# Now we find what will be the position of head in the next timeframe is equal to the food we can simply ignore the deletion part of above statment
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        goto(head.x, head.y)
        dot(15 ,"Red")
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Mark the complete body of the snake with black dots.
    for body in snake:
        goto(body.x , body.y)
        dot(10)

    # As the last element of the snake list is head Mark it with a different color mark it with red dot.
    goto(snake[-1].x , snake[-1].y)
    dot(10,"Blue")

    # Go to the position of the food and make a Green dot there marking the food.
    goto(food.x,food.y)
    dot(10,"Green")
    update()
    # move function will be called after every 50 ms
    ontimer(move, 100)
#Setup screen with dimension 420*420
setup(420, 420)

#Hides the turtle
hideturtle()

#Delays animation if turned on
tracer(False)
# Listen to the events like onscreenclick or onkey
listen()

# As we tap the right key,left key etc.. onkey function corresponding to that key will be called.
# As we know that in the onkey function we just need to pass the reference of the function change and not the function. 
onkey(lambda : change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
up()
move()
done()
