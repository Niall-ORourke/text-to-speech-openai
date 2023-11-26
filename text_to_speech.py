from pathlib import Path
import openai
import json

# Load API key from the configuration file
with open('config.json', 'r') as file:
    config = json.load(file)
    api_key = config['api_key']

# Initialize the OpenAI client with the API key
client = openai.OpenAI(api_key=api_key)

# Path to the JSON configuration file
config_path = Path(__file__).parent / "audio_config.json"

# Load the audio configuration from the JSON file
with open(config_path, 'r') as file:
    audio_config = json.load(file)

# Extract the directory for storing the audio files from the config
audio_folder = Path(__file__).parent / audio_config["audio_folder"]
audio_folder.mkdir(exist_ok=True)  # Create the folder if it doesn't exist

# Loop through each entry in the configuration and generate audio files accordingly
for part in audio_config["audio_parts"]:
    speech_file_path = audio_folder / part["filename"]

    if part["generate"]:
        # Create the speech
        response = client.audio.speech.create(
            model="tts-1",
            voice="echo",
            input=part["text"]
        )

        # Stream the response to a file
        response.stream_to_file(speech_file_path)
    else:
        print(f"Skipping generation of {part['filename']} as per the provided flag.")
















