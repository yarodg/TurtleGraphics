import turtle as t
import random

tim = t.Turtle()

task = {
    "triangle": "3",
    "square": "4",
    "pentagon": "5",
    "hexagon": "6",
    "heptagon": "7",
    "octagon": "8",
    "nonagon": "9",
    "decagon": "10",
}

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for shape in task:
    angle = 360 / int(task[shape])
    color = random.choice(colors)
    tim.color(color)

    for _ in range(int(task[shape])):
        tim.forward(100)
        tim.right(angle)
