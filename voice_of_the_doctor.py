from gtts import gTTS
from pydub import AudioSegment
import platform
import subprocess
import os

def convert_mp3_to_wav(mp3_path, wav_path):
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav")

def text_to_speech_with_gtts_wav(input_text, output_file_path):
    language = "en"

    # Step 1: Save MP3 using gTTS
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_file_path)

    # Step 2: Convert MP3 to WAV
    output_filepath_wav = output_file_path.replace(".mp3", ".wav")
    convert_mp3_to_wav(output_file_path, output_filepath_wav)

    # Step 3: Play WAV file depending on OS
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath_wav])
        elif os_name == "Windows":  # Windows
            subprocess.run([
                'powershell', '-c',
                f'(New-Object Media.SoundPlayer "{output_filepath_wav}").PlaySync();'
            ])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath_wav])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


#text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")