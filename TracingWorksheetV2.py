from PIL import Image, ImageDraw, ImageFont
import random
from datetime import datetime


def draw_dotted_text(draw, position, text, font, dot_spacing=15):
    """
    Draws text as a dotted outline by placing small dots along the character paths.
    """
    x, y = position
    bbox = draw.textbbox((x, y), text, font=font)
    char_width = bbox[2] - bbox[0]
    char_height = bbox[3] - bbox[1]
    for i in range(0, char_width, dot_spacing):
        for j in range(0, char_height, dot_spacing):
            draw.text((x + i, y + j), '.', font=font, fill="black")


def generate_tracing_worksheet():
    """
    Generates a simple black-and-white worksheet with dotted outlines of five letters or numbers
    for a child to trace and saves it as a PNG file.
    """
    characters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 5)
    characters += [char.lower() for char in characters[:5]]  # Generate lowercase versions

    # Image dimensions
    img_width, img_height = 1000, 1200
    background_color = "white"

    # Create image
    img = Image.new("RGB", (img_width, img_height), background_color)
    draw = ImageDraw.Draw(img)

    # Load a basic font
    try:
        font = ImageFont.truetype("arial.ttf", 200)  # Adjust size as needed
    except IOError:
        font = ImageFont.load_default()

    # Define starting position
    x, y = 100, 100
    spacing = 250

    for char in characters:
        draw.text((x, y), char, font=font, fill="lightgray")  # Draw solid letter in faint gray
        draw_dotted_text(draw, (x, y), char, font)  # Overlay with dotted version
        y += spacing  # Move down for next character

    # Generate timestamped file name
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"tracing_worksheet_{timestamp}.png"

    # Save image to file
    img.save(filename)
    print(f"Worksheet saved as {filename}")

    return filename


if __name__ == "__main__":
    generate_tracing_worksheet()
    print("Done.")
