import time
from PIL import Image

# Generate a random number
current_time: float = int(time.time())
generated_number: int = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
 
print(f"Generated number: {generated_number}")
 
with Image.open("Chapter1.png") as image:
    # Convert the image to RGB format
    image = image.convert("RGB")
    width: int = image.width
    height: int = image.height
 
    # Loop each pixel in the image
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the current pixel
            r, g, b = image.getpixel((x, y))
 
            # Add  generated number to the red (r) value
            r += generated_number
 
            # Set the RGB values of the current pixel to the new values
            image.putpixel((x, y), (r, g, b))
 
    # Save the modified image as 'chapterlout.png'
    image.save("chapterlout.png")
 
# Calculate the sum of all the red (r) pixel values in the modified image
red_sum: int = sum(image.getpixel((x, y))[0] for x in range(width) for y in range(height))
 
# Print the sum of all the red pixel values
print(f"Sum of red pixel values: {red_sum}")