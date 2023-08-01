from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import numpy as np
import datetime
import os
import tempfile

video_width = 1280
video_height = 720
fps = 30

def create_slide(illustration, audio_path):
    # Convert the PIL.Image object to a numpy array
    illustration_np = np.array(illustration)

    # Load the audio
    audio = AudioFileClip(audio_path)

    # Match the illustration's duration with the audio's duration
    illustration = ImageClip(illustration_np).set_duration(audio.duration)

    # Combine the illustration and audio
    slide = illustration.set_audio(audio)

    return slide

def generate_video(illustrations, audios):
    # Create a list to hold all the slides
    slides = []

    for illustration, audio in zip(illustrations, audios):
        # Save the audio data to a temporary file
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as audio_file:
            audio_file.write(audio)
            audio_path = audio_file.name
        
        slide = create_slide(illustration, audio_path)
        slides.append(slide)
        os.unlink(audio_path)  # Delete the temporary audio file

    # Create the directory path
    now = datetime.datetime.now()
    dir_path = f'data/storybook/{now:%Y-%m-%d_%H-%M-%S}'
    os.makedirs(dir_path, exist_ok=True)

    # Save the final video to the created directory
    video_path = f"{dir_path}/filename.mp4"
    final_video = concatenate_videoclips(slides).set_duration(sum(s.duration for s in slides)).set_fps(fps)
    final_video.write_videofile(video_path, codec='libx264')
    
    return video_path  # Return the path of the saved video