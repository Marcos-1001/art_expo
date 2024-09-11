from  random import randint
import PIL.Image as Image
from tqdm import tqdm
import numpy as np
import cv2


def get_random_color() -> tuple:
    return (int(np.random.uniform(100, 200)), int(np.random.uniform(100, 200)), int(np.random.uniform(100, 200)))


def gaussian_color(distr = (1,1,1)) -> tuple:
    random = np.random.normal(128, 80, 3)
    
    return  (int(random[0]*distr[0]), int(random[1]*distr[1]), int(random[2]*distr[2]))


# Normal distribution
def get_random_coordinates( limits : int) -> list:
    return  (
        abs(int(np.random.uniform(0, limits-1))), abs(int(np.random.uniform(0, limits-1))) 
    )


def  mix_colors(color1 : tuple, color2 : tuple) -> tuple:
    final  = np.clip((np.array(color1) + np.array(color2)*0.24)//2 * 1.75, 0, 255).tolist()
    return (int(final[0]), int(final[1]), int(final[2]))




def is_limit(x : int, y : int, limits : int) -> bool:
    return x < 0 or y < 0 or x >= limits or y >= limits


move_map = [(0, 1),  (1, 0),  (1, 1), 
            (0, -1), (-1, 0), (-1, -1), 
            (1, -1), (-1, 1) ]
    
    

def flood_fill(seeds : list, limits : int, im : Image) -> None:
    tree =  [[0 for i in range(limits)] for j in range(limits)]
            
    queue = [(x, y,0, color) for (x,y), color in seeds]
    while queue:

        x, y, step, color = queue.pop(0)
        tree[x][y] = 1
        im.putpixel((x, y), color)
            
        # Random walk - choose 4 random directions
        moves = [move_map[randint(0,39)% 8] for i in range(4)]

        for dx, dy in moves:
            if not is_limit(x+ dx, y +dy, limits)  and tree[x+dx][y+dy] == 0:
                
                tree[x+dx][y+dy] = 1

                if step >= 100 and step % 20 == 0: 
                    
                    ncolor = gaussian_color((.1, .75, .05))
                    queue.append((x+dx, y+dy,step+1, mix_colors(color, ncolor )))
                elif step < 100 and step % 10 == 0: 
                    ncolor = gaussian_color((.9, .9, .05))
                    queue.append((x+dx, y+dy,step+1, mix_colors(color, ncolor )))
                else: 
                    queue.append((x+dx, y+dy,step+1, color))
            


            


# This functions fills the pixel holes where the random walk did not reach
def fill_holes(image: Image , limits : int) -> Image:
    for i in range(limits):
        for j in range(limits):
            if image.getpixel((i, j)) == (0, 0, 0):
                fill_color = (150, 10, 30)
                
                
                for k in range(i-4, i+4):
                    for z in range(j-4, j+4):
                        if not is_limit(k, z, limits)  and k != i and z != j:
                            pixel_color = image.getpixel((k, z))
                            fill_color = (fill_color[0] + pixel_color[0], fill_color[1] + pixel_color[1], fill_color[2] + pixel_color[2])


                fill_color = (fill_color[0]// 49, fill_color[1]// 49, fill_color[2]// 49)

                image.putpixel((i, j), fill_color)


if __name__ == "__main__":
    limits = 1000
    size = 2
    np.random.seed()
    im = Image.new('RGB', (limits, limits), (0, 0, 0))

    #seeds = [(get_random_coordinates(limits=limits), gaussian_color()) for _ in range(size)]   
    seeds = [((200, 800), (255,255,0))]

    flood_fill(seeds, limits, im)
    #im.show()

    fill_holes(im, limits=limits)

    #im.show()

    im.save('image.png')


#print(get_random_coordinates(500))

