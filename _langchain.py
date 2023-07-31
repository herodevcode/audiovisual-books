import os
from dotenv import load_dotenv
import openai

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def paragraphs_from_text(txt):
    output = txt.splitlines()
    return output

# method to generate prompt for stable diffusion
def image_gen_prompt(paragraph, style):
    result = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "user", "content": f"""

            I have a short book that I want to convert into a picture book. To make the drawings, I'm using an AI model that converts a text prompt into an image. These prompts are short, simple and easy to understand without unnecessary adjectives. Here's what your prompts should look like: 
             
            'A raccoon eating an apple, photorealistic style'
             
            Can you take the following paragraph and artstyle, and generate a prompt for the aforementioned AI model?
             
            paragraph to be illustrated: 
            {paragraph}

            artstyle:
            {style}

            """}
        ]
    )
    message = result['choices'][0]['message']['content']
    return message

def get_all_prompts(paragraphs, style):
    prompts = []
    for paragraph in paragraphs:
        prompt = image_gen_prompt(paragraph, style)
        prompts.append(prompt)
    return prompts

