import os
import datetime
from dotenv import load_dotenv
from elevenlabs import generate, set_api_key, save

# load_dotenv()
# XI_API_KEY = os.getenv("XI_API_KEY")
# # Set API key for ElevenLabs
# set_api_key(XI_API_KEY)

# Define function for generating speech
def generate_speech(text_input, voice_actor, api_key):

    set_api_key(api_key)

    generated_speech = generate(
        text = text_input,
        voice = voice_actor,
        model = 'eleven_monolingual_v1')
    
    return generated_speech

def generate_and_save_all_speech(text_inputs, voice_actor, api_key):

    # Generate all audio files
    all_speeches = [(idx, generate_speech(text, voice_actor, api_key)) for idx, text in text_inputs]

    # Creating the directory path
    now = datetime.datetime.now()
    dir_path = f'data/audios/{now:%Y-%m-%d_%H-%M-%S}'

    # Creating the directory if it does not already exist
    os.makedirs(dir_path, exist_ok=True)

    audio_list = []
    audio_paths = []
    for idx, audio in all_speeches:
        filename = f"audio{idx}.mp3"
        file_path = os.path.join(dir_path, filename)
        save(audio, file_path)
        audio_list.append(audio)
        audio_paths.append(file_path)

    # return audio_paths
    return audio_list