from PIL import Image

# reading the row from middle line(200)
scan_row = 200

# Space between the dimensions
step = 9

# Character mapping of the variables
alphabets = {' ':1, 'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, 'i': 10, 'j': 11, 'k': 12,
                               'l': 13, 'm': 14, 'n': 15, 'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22,
                               'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27}

def decode(image):
    
    # Dynamically read the image size
    canvas_width, canvas_height = image.size
    x = 0
    # variable to store the decoded msg
    str = ""

    # Reading the row of the canavs    
    while x < canvas_width:
        # calculating width of the bar
        current_width = 0
        while x + current_width < canvas_width and image.getpixel((x + current_width, scan_row)) == 0:
            current_width += 1

        # Checks space or a character
        if current_width == 1:
            str += " "
        else:
            for char, width in alphabets.items():
                if width == current_width:
                    str += char
                    break   
                
        x+= current_width if current_width > 0 else step

    return str

# Reading the image from the user
image = Image.open('807333.png')
# image = Image.open('output.png')
decoded_str = decode(image)  
print("The decoded text from the barcode is:", decoded_str)