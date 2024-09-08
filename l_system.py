
import PIL.Image as Image
from PIL import ImageDraw
from random import randint
import numpy as np
import cv2
import re
def l_system(axiom : str, rules : dict, iterations : int) -> str:
    new_axiom = ""
    for _ in range(iterations):
        new_axiom = "".join([rules[c] if c in rules else c for c in axiom])
        axiom = new_axiom
    return axiom





def draw_l_system(image: Image, 
                  axiom : str, 
                  ) -> Image:
    x, y = 500, 1000
    stack = []
    draw = ImageDraw.Draw(image)
    init_angle = 270
    
    length = 10
    #print(axiom)
    for c in axiom:
        if c == "F" or c == "X":

            x1 = x + length * np.cos(np.radians(init_angle))
            y1 = y + length * np.sin(np.radians(init_angle))
            draw.line((x, y, x1, y1), fill="black")
            x, y = x1, y1


        elif c == "+":
            init_angle += 25.7
        elif c == "-":
            init_angle -= 25.7
        elif c == "[":
            stack.append((x, y, init_angle))
        elif c == "]":
            x, y, init_angle = stack.pop()





    
                                                     






            
            
       
# Parametric L-System


                
            
    



if __name__ == '__main__':
    
    iterations = 4
    angle = 25.7
    length = 20    
    image = Image.new("RGB", (1000, 1000), "white")
    axiom = "X"
    rules = {
        "F":"FF",
        "X":"F-[[X]+X]+F[+FX]-X",
    }
    rules_1 = {
        "F":"FF-[-F+F+F]+[+F-F-F]"
    }
    

    draw_l_system(image, l_system("F", rules_1, iterations))
    image.show()
    image.save("l_system.png")
