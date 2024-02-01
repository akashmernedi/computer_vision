from PIL import Image
from PIL import ImageDraw

# Canavas dimensions
canvas_width = 800
canvas_height = 400

# creating a canavas based on dimensions
canvas = Image.new("L", (canvas_width, canvas_height), "white")
draw = ImageDraw.Draw(canvas)

# Space between the dimensions
step = 9
bar_height = (10, 350) 
empty_space = (150, 250)

# Character mapping of the variables
alphabets = {' ':1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12,
                           'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22,
                           'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}  

def encode(text):
    # temp variable to track the steps
    x = 8
    for char in text:
        if char != ' ':
            bar_width = alphabets.get(char, 1)
            y1, y2 = bar_height
        else:
            bar_width = 1
            y1, y2 = empty_space

        draw.rectangle([x, y1, x + bar_width, y2], fill="black")
        x += bar_width + step

    canvas.save("output.png")
    # canvas.show()

# Reading the string input from the user
text = input("Enter text to generate barcode: ")
encode(text)
print('The barcode has been generated for the input data')
