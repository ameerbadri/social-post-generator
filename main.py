import os
import re
import base64
from dotenv import load_dotenv
import writer as wf
import writer.ai
from openai import OpenAI

# Set the API keys
# Load environment variables from .env file
load_dotenv()
wf.api_key = os.getenv("WRITER_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Welcome to Writer Framework! 
# This template is a starting point for your AI apps.
# More documentation is available at https://dev.writer.com/framework

def generate_and_display_posts_and_tags(state):
    print(f"Here's what the user entered: {state['topic']}")

    # Display message
    state["message"] = "% Generating social media posts and tags for you..."

    # Generate and display social posts
    prompt = f"You are a social media expert. Generate 5 engaging social media posts about {state['topic']}. Include emojis, and put a blank line between each post."
    state["posts"] = writer.ai.complete(prompt)
    print(f"Posts: {state['posts']}")

    # Generate and display hashtags
    prompt = f"You are a social media expert. Generate around 5 hashtags about {state['topic']}, delimited by spaces. For example, #dogs #cats #ducks #elephants #badgers"
    pattern = r"#\w+"
    hashtags = re.findall(pattern, writer.ai.complete(prompt))
    state["tags"] = {item: item for item in hashtags}
    print(f"Tags: {state['tags']}")

    # Generate image using OpenAI
    image_prompt = f"You are a creative and whimsical artist. Create an image of: {state['topic']}"
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_prompt,
        size="1024x1024",
        response_format="b64_json",
        quality="standard",
        n=1,
    )
    # Get the image binary
    # Extract the base64-encoded image data
    image_data = response.data[0].b64_json
    # Decode the base64 image data
    image_bytes = base64.b64decode(image_data)
    state["image_binary"] =  wf.pack_bytes(image_bytes, "image/png")

    # Hide message
    state["message"] = ""


# Initialise the state
wf.init_state({
    "topic": "",
    "message": "",
    "tags": {},
    "posts": "",
    "image_binary": "",
    "my_app": {
        "title": "SOCIAL POST GENERATOR",
        "sub-title": "AI Social Media Post Generator using the Writer Framework"
    },
})