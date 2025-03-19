from openai import OpenAI
import os
import sys

# Set up your OpenAI API key
api_key = os.environ.get("OPENAI_API_KEY")
if api_key is None:
    print("OpenAI API key not set in environment variables: expecting OPENAI_API_KEY")
    sys.exit(1)
else:
    client = OpenAI(api_key=api_key)

# Code goes here.

print("Done.")
sys.exit(0)