
import PIL.Image as Image
from PIL import ImageDraw
from random import randint
import numpy as np
import cv2
import re
def l_system(axiom : str, rules : dict, iterations : int) -> str:
    new_axiom = ""
    for _ in range(iterations):
        new_axiom = "".join([rules[c][randint(0, len(rules[c])-1)] if rules.get(c) else c for c in axiom])
        axiom = new_axiom
    return axiom





def draw_l_system(image: Image, 
                  axiom : str, 
                  seed : tuple = (500, 500),
                  length : int = 15,
                  angle : int = 25.7
                  ) -> Image:
    x, y = seed
    stack = []
    draw = ImageDraw.Draw(image)
    init_angle = 270
    
    #print(axiom)
    for c in axiom:
        if c == "F" or c == "X":

            x1 = x + length * np.cos(np.radians(init_angle))
            y1 = y + length * np.sin(np.radians(init_angle))
            draw.line((x, y, x1, y1), fill="black")
            x, y = x1, y1


        elif c == "+":
            init_angle += angle
        elif c == "-":
            init_angle -= angle
        elif c == "[":
            stack.append((x, y, init_angle))
        elif c == "]":
            x, y, init_angle = stack.pop()





    
                                                     






            
            
       
# Parametric L-System


                
            
    



if __name__ == '__main__':
    
    iterations = 5
    angle = 22.5
    length = 35    
    image = Image.new("RGB", (1000, 1000), "white")
    axiom = "X"
    rules = {
        "F":["FF"],
        "X":["F-[[X]+X]+F[+FX]-X","F+[[X]-X]-F[-FX]+X"],
    }
    rules_1 = {
        "F":["FF-[-F+F+F]+[+F-F-F]"]
    }
    
    
    rules_2 = {
        "F": ["FF"],
        "X":["[F[-X]F[-X]+X]"]
    }
    rules_3 = {
        "F" : ["FF","F[+F]F[-F]F",
               "F[+F]F",
               "F[-F]F",],
    }

    draw_l_system(image, l_system("X", rules_2, iterations), seed=(300, 1000), length=5, angle=22.5)
    draw_l_system(image, l_system("X", rules, 4), seed=(750, 1000), length=10, angle=25)
    draw_l_system(image, l_system("F", rules_3, 5), seed=(500, 1000), length=3, angle=18)
    #draw_l_system(image, l_system("F", rules_3, 5), seed=(560, 1000),       =3, angle=18)
    draw_l_system(image, l_system("F", rules_3, 5), seed=(440, 1000), length=3, angle=18)
    draw_l_system(image, l_system("F", rules_1, 4), seed=(620, 1000), length=10, angle=18)
    image.show()
    # Erase the background 
    image.save("l_system.png")
    
    
    
