# method to generate images from text
# input: single paragraph
# output: image

import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


from dotenv import load_dotenv
load_dotenv()
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = os.getenv('DREAMSTUDIO_API_KEY')

stability_api = client.StabilityInference(
    key = os.environ['STABILITY_KEY'],
    verbose = True,
    engine = "stable-diffusion-v1"
)

def save_image(prompt, idx):
    answers = stability_api.generate(
        prompt = prompt
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(str(idx) + ".png")

def gen_all_images(prompts):
    for idx, prompt in prompts:
        save_image(prompt, idx)


