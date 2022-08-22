from PIL import Image
from math import sqrt
from copy import copy
from tkinter import colorchooser

Fcolor = colorchooser.askcolor()[0]
Scolor = colorchooser.askcolor()[0]

width = 1500

def gradient_creator (color_1,color_2) :
    im = Image.new("RGBA",(width,255),(255,255,255))

    starting_color = copy(color_1)

    color_vector = [color_2[f]-color_1[f] for f in range(3)]
    color_vector_magnitude = sqrt(sum([f**2 for f in color_vector]))
    color_unit_vector = [(f/width) for f in color_vector]
    color_gradient_list = [color_1]

    for i in range(1,width-1) :
        starting_color = [starting_color[n]+color_unit_vector[n] for n in range(3)]
        color_gradient_list.append(starting_color)
    color_gradient_list.append(color_2)
    print(color_vector)
    print(color_vector_magnitude)
    print(color_unit_vector)
    print(len(color_gradient_list))
    
    for i in range(width) :
        for x in range(255) :
            im.putpixel((i,x),tuple([int(f) for f in color_gradient_list[i]]))
    
    return im

if __name__ == "__main__" :
    gradient_creator(Fcolor,Scolor).save("gradient.png")