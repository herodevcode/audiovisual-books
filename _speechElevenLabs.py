import os
import wave
from dotenv import load_dotenv
from elevenlabs import generate, set_api_key, save

load_dotenv()
XI_API_KEY = os.getenv("XI_API_KEY")
#Set API key for ElevenLabs
set_api_key(XI_API_KEY)

#Define function for generating speech
def generate_speech(text_input, voice_actor):
    generated_speech = generate(
        text = text_input,
        voice = voice_actor,
        model = 'eleven_monolingual_v1')
    
    return generated_speech

def generate_all_speech(text_inputs, voice_actor):
    all_speeches = [generate_speech(text_input, voice_actor) for text_input in text_inputs]
    return all_speeches

def save_audios(audios):
    folderpath = os.getcwd() + "/audios"
    for idx, audio in enumerate(audios):
        filename = f"audio{idx}.mp3"
        file_path = os.path.join(folderpath, filename)
        save(audio, file_path)
