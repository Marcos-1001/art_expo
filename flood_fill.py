from  random import randint
import PIL.Image as Image
from tqdm import tqdm
import numpy as np

def get_random_color() -> tuple:
    return (randint(150, 255), randint(150, 255), randint(150, 255))

# Normal distribution
def get_random_coordinates( limits : int) -> list:
    return  (
        abs(int(np.random.normal(limits//2, limits//4,))),
        abs(int(np.random.normal(limits//2, limits//4,)))
    )


def get_random_seeds(size : int, limits : int) -> list:
    return  [ [
                get_random_coordinates(limits=limits) ,  get_random_color()
              ] 
                for _ in range(size)
            ]


def is_limit(x : int, y : int, limits : int) -> bool:
    return x < 0 or y < 0 or x >= limits or y >= limits

def mixing_colors(color1 : tuple, color2 : tuple) -> tuple:
    if color2 == (0, 0, 0):
        return color1

    return ((color1[0] + color2[0]) // 2, (color1[1] + color2[1]) // 2, (color1[2] + color2[2]) // 2)

def flood_fill(seeds : list, limits : int, image : Image):
    
    for [seed, color_seed] in tqdm(seeds):
        stack = [[seed, color_seed,0]]
        visited = [[0 for i in range(limits)] for j in range(limits)]            
        while stack:
            #print(len(stack))
            pixel_info = stack.pop()
            x, y = pixel_info[0]
            color = pixel_info[1]       
            step = pixel_info[2]     
            if is_limit(x, y, limits) or  visited[x][y] == 1 or step > 200:
                continue
            new_color  =  mixing_colors(color , image.getpixel((x,y)))
            
            image.putpixel((x, y), new_color)
            new_color = (int(new_color[0] ), int(new_color[1] ), int(new_color[2] ))
            
            visited[x][y] = 1


            # move randomly   
            #

            stack.append([[x+1, y], new_color, step+randint(1,3)])
            stack.append([[x-1, y], new_color, step+randint(1,3)])
            stack.append([[x, y+1], new_color, step+randint(1,3)])
            stack.append([[x, y-1], new_color, step+randint(1,3)])
            
            







limits = 500
size = 100

im = Image.new('RGB', (limits, limits), (0, 0, 0))

seeds = get_random_seeds(size, limits)
flood_fill(seeds, limits, im)




im.save('image.png')
