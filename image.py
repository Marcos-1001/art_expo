import PIL.Image as Image



if __name__ == "__main__":

    # improve image dpi
    image = Image.open("l_system_4.png")
    # Resize for 115x185 cm at 600 dpi
    image = image.resize((6880, 11100))    
    image.save("l_system_4_hi.png", dpi = (600, 600))

    

