import replicate
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Fetch the API token from the environment variable
api_token = os.getenv("REPLICATE_API_TOKEN")
print("API Token:", api_token)

# Make sure the token is not None
if not api_token:
    print("API Token is missing. Please check the environment variable.")
else:
    print("API Token loaded successfully.")

# Initialize Replicate client with the token
client = replicate.Client(api_token)


# Define the model and the input
import replicate

input = {
    "prompt": "an astronaut riding a horse on mars, hd, dramatic lighting",
    "scheduler": "K_EULER"
}

output = replicate.run(
    "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
    input=input
)
for index, item in enumerate(output):
    with open(f"output_{index}.png", "wb") as file:
        file.write(item.read())
#=> output_0.png written to disk


print("Image(s) saved successfully.")
