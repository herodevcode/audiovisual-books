# method to generate images from text
# input: single paragraph
# output: image

import os
import io
import warnings
import datetime

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# from dotenv import load_dotenv
# load_dotenv()
# os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
# os.environ['STABILITY_KEY'] = os.getenv('DREAMSTUDIO_API_KEY')

def save_image(idx, prompt, dir_path, api_key):

    stability_api = client.StabilityInference(
    key = api_key,
    verbose = True,
    engine = "stable-diffusion-v1"
    )   

    warnings_string = None
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always") 
        answers = stability_api.generate(prompt=prompt)
        # Check if any warnings were triggered
        for warning in w:
            if issubclass(warning.category, UserWarning):
                warnings_string = str(warning.message)

    answers = stability_api.generate(
        prompt = prompt,
        steps=5
    )
    images = []
    image_paths = []
    count = 0
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warning_message = (
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                    )
                warnings.warn(warning_message)
                return None, warning_message
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                
                # Saving the image in the specified directory
                image_path = f'{dir_path}/{str(idx)}.png'
                img.save(image_path)
                
                images.append(img)
                image_paths.append(image_path)
                count += 1
        if count >= 1:
            break
    # return image_paths, warnings_string
    return images, warnings_string

def gen_all_images(prompts, api_key):

    images = []
    warnings = []

    # Creating the directory path
    now = datetime.datetime.now()
    dir_path = f'data/images/{now:%Y-%m-%d_%H-%M-%S}'

    # Creating the directory if it does not already exist
    os.makedirs(dir_path, exist_ok=True)

    for idx, prompt in prompts:
        image_list, warning_message = save_image(idx, prompt, dir_path, api_key)
        if image_list is None:
            warnings.append(warning_message)
        else:
            images.extend(image_list)
    return images, warnings