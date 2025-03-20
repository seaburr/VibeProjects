from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO
import os
import sys
from datetime import datetime

# Set up your OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    print("OpenAI API key not set in environment variables: expecting OPENAI_API_KEY")
    sys.exit(1)
else:
    client = OpenAI(api_key=api_key)

def generate_coloring_page(prompt, save_path):
    response = client.images.generate(prompt=f"{prompt}, black and white line art, simple, child-friendly, with an emphasis on cute for animal and people suitable for coloring",
    model="dall-e-3",
    n=1,
    size="1024x1024"
    )

    image_url = response.data[0].url
    print("Generated Image URL:", image_url)

    # Download and display the image
    image_response = requests.get(image_url)
    img = Image.open(BytesIO(image_response.content))

    #os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists
    img.save(save_path, format="PNG")
    print(f"Image saved as {save_path}")

    img.show()

prompt = input("Image prompt: ")
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
print("Generating image...")
generate_coloring_page(prompt, f"{timestamp}.png")
print("Done.")
sys.exit(0)