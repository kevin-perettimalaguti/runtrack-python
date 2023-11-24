def draw_rectangle(width, height):
    width -=2
    print("|" + "-" * width + "|")
    y = 0
    while y < height -2:            
        print("|" + " " * width + "|")
        y += 1
    print("|" + "-" * width + "|")    


draw_rectangle(10, 3)

    

    
