
import PIL.Image as Image
from PIL import ImageDraw
import numpy as np
import cv2

def l_system(axiom : str, rules : dict, iterations : int) -> str:
    for _ in range(iterations):
        axiom = "".join([rules.get(c, c) for c in axiom])
        
    return axiom

def draw_l_system(image: Image, 
                  axiom : str, 
                  angle : int, 
                  length : int) -> Image:
    x, y = 500, 900
    stack = []
    draw = ImageDraw.Draw(image)
    angle = 270
    for c in axiom:
        if c == "F":
            x1 = x + length * np.cos(np.radians(angle))
            y1 = y + length * np.sin(np.radians(angle))
            draw.line((x, y, x1, y1), fill="black")
            x, y = x1, y1
        elif c == "+":
            angle += 25
        elif c == "-":
            angle -= 25
        elif c == "[":
            stack.append((x, y, angle))
        elif c == "]":
            x, y, angle = stack.pop()
    

if __name__ == '__main__':
    axiom = "F"
    rules = {"F1": "F[+F]F[-F]F",
             "F2":"F[+F]F",
              "F3":"F[-F]F",}
    iterations = 5
    angle = 25.7
    length = 15    
    image = Image.new("RGB", (1000, 1000), "white")
    draw_l_system(image, l_system(axiom, rules, iterations), angle, length)
    image.show()
    image.save("l_system.png")
