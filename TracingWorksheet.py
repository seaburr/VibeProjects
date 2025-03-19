from openai import OpenAI
import os
import sys
import requests
import random
from datetime import datetime


def generate_tracing_worksheet(characters: list):
    """
    Generates a simple black-and-white worksheet with dashed outlines of five letters or numbers
    for a child to trace and saves it as a PNG file.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        print("OpenAI API key not set in environment variables: expecting OPENAI_API_KEY")
        sys.exit(1)

    client = OpenAI(api_key=api_key)

    prompt = (f"A black-and-white tracing worksheet displaying only these characters: {' '.join(characters)}. "
              "Each character should be in a large, dashed outline for tracing. "
              "No additional images, symbols, glyphs, decorations, or background—only the specified characters "
              "in a simple, clean, and clear dotted-line font for tracing.")

    response = client.images.generate(
        #model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1
    )

    image_url = response.data[0].url
    print(f"Worksheet generated: {image_url}")

    # Download the image
    image_data = requests.get(image_url).content

    # Generate timestamped file name
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    filename = f"tracing_worksheet_{timestamp}.png"

    # Save image to file
    with open(filename, "wb") as file:
        file.write(image_data)

    print(f"Worksheet saved as {filename}")
    return filename


if __name__ == "__main__":
    characters = random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", 5)
    characters += [char.lower() for char in characters[:5]]  # Generate lowercase versions

    generate_tracing_worksheet(characters)

    print("Done.")
    sys.exit(0)