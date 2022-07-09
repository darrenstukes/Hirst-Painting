import colorgram
import turtle as turtle_module
import random
#
# rgb_colors =[]
# colors = colorgram.extract('image.jpg',30)
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list=[(229, 223, 226), (217, 227, 220), (195, 172, 121), (222, 227, 232), (157, 97, 59), (185, 159, 52), (9, 53, 77), (125, 37, 25), (55, 33, 27), (110, 69, 85), (118, 162, 175), (27, 118, 164), (74, 35, 43), (85, 138, 67), (10, 62, 44), (71, 153, 130), (121, 35, 40), (182, 98, 82), (207, 202, 146), (144, 176, 161), (178, 150, 156), (176, 202, 188), (217, 179, 172), (22, 77, 93), (33, 79, 62), (95, 143, 150), (160, 111, 117), (214, 178, 183), (168, 202, 212)]

# 10 x 10 , 20 in size 50 paces
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=101


for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen=turtle_module.Screen()
screen.exitonclick()