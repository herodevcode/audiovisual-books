import os
import openai

# from dotenv import load_dotenv
# load_dotenv()
# openai.api_key  = os.getenv("OPENAI_API_KEY")

# method to generate prompt for stable diffusion
def image_gen_prompt(paragraph, style, api_key):
    openai.api_key = api_key
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

def get_all_prompts(texts, style, api_key):
    prompts = []
    for idx, paragraph in enumerate(texts):
        prompt = image_gen_prompt(paragraph, style, api_key)
        prompts.append((idx, prompt))
        if idx >= 2:  # stop after generating 3 prompts
            break
    return prompts