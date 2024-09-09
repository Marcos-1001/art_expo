from random import randint
import PIL.Image as Image
from tqdm import tqdm
import numpy as np

def extreme_random_point(image_size: int) -> tuple:
    extreme = randint(0, 3)
    if extreme == 0:
        return (randint(0, image_size-1), 0)
    if extreme == 1:
        return (randint(0, image_size-1), image_size-1)
    if extreme == 2:
        return (0, randint(0, image_size-1))
    if extreme == 3:
        return (image_size-1, randint(0, image_size-1))


def is_limit(x : int, y : int, limits : int) -> bool:
    return x < 0 or y < 0 or x >= limits or y >= limits

all_directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def walker(tree, seed, image_size ): 
    x, y = seed
    stuck = False
    move_size = 5
    
    while not stuck:        


        dx, dy = (randint(-move_size, move_size), randint(-move_size, move_size))            
        while is_limit(x+dx, y+dy, image_size):
            dx, dy = (randint(-move_size, move_size), randint(-move_size, move_size))
        x+=dx
        y+=dy

        for dx, dy in all_directions:
            dx*= move_size
            dy*= move_size 
            if not is_limit(x+ dx, y +dy, image_size)  and tree[x+dx][y+dy] == 1:
                stuck = True
                break
        
        
    tree[x][y] = 1
    tree[image_size-1 - x][y] = 1


def diffusion_limited_agg(image_size: int, seed : tuple ,image: Image): 
    
    tree =  [[0 for i in range(image_size)] for j in range(image_size)]
    tree[seed[0]][seed[1]] = 1
    
    for _ in tqdm(range(15000)):
        walker(tree, extreme_random_point(image_size=image_size), image_size)
    
    for i in range(image_size): 
        for j in range(image_size):
           
            if tree[i][j] == 1:
                for k in range(i-3, i+3):
                    for z in range(j-3, j+3):
                        if not is_limit(k, z, image_size) :
                            image.putpixel((k, z), (255, 255, 255))
    return tree
def map_image_to_tree(image: Image ) -> None:
    tree = [[0 for i in range(image.height)] for j in range(image.width)]
    for i in range(image.width):
        for j in range(image.height):
            if image.getpixel((i, j)) == (255, 255, 255):
                tree[i][j] = 1
    return tree


def gaussian_color() -> tuple:
    random = np.random.normal(128, 20, 3)
    return  (int(random[0]), int(random[1]), int(random[2]))

def mix_colors(color1 : tuple, color2 : tuple) -> tuple:
    final  = np.clip((np.array(color1)*np.array(color2)) , 0, 255).tolist()
    #print(final)
    return (int(final[0]), int(final[1]), int(final[2]))

def gradient_color(image,tree, seed, color) -> tuple:
    queue = [(seed, color, 0)]
    limits = len(tree)
    while queue:
        ( (x, y) , color, step) = queue.pop(0)
        for dx, dy in all_directions:
            if not is_limit(x+dx, y+dy, limits) and tree[x+dx][y+dy] == 1:

                tree[x+dx][y+dy] = 2
                if step % 45 == 0: 
                    queue.append(((x+dx, y+dy), mix_colors(color, (1.075, 1.0015, 1.0009)), step+1))
                    #print("here")
                else: 
                    queue.append(((x+dx, y+dy), color, step+1))
                image.putpixel((x+dx, y+dy), color)

    
    




if __name__ == "__main__":
    image_size = 1000 
    #image = Image.new("RGB", (image_size, image_size), (0, 0, 0))
    seed = (image_size//2, image_size//2)
    
    image = Image.open("dla_3.png")
    tree = map_image_to_tree(image=image)
    #tree = diffusion_limited_agg(image_size, seed, image)
    gradient_color(image, tree, seed, (100, 100, 100))
    image.save("dla_4.png")