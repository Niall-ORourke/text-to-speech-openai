# Text-to-Speech Generator

This Python script leverages the OpenAI API to convert specified text into speech, creating audio files. It dynamically reads text and configuration details from a JSON file, allowing for flexible and easy adjustments to the text-to-speech generation process.

## Features

- **Dynamic Text-to-Speech Conversion**: Converts a variety of text inputs into speech.
- **Configurable Input**: Utilizes a JSON file for input text, making it easy to change the content without altering the script.
- **Automated File Management**: Automatically creates and stores audio files in a specified directory.

## Prerequisites

- Python 3.x
- OpenAI API Key
- Installation of the `openai` Python package

## Installation and Dependency Management

### 1. Clone the Repository:

Ensure you have Git installed on your system. Clone the repository to your local machine using:

```
git clone https://github.com/Niall-ORourke/text-to-speech.git
```

### 2. Install Python:

If you don't have Python installed, download and install Python 3.x from [python.org](https://www.python.org/downloads/).

### 3. Create a Virtual Environment (Optional but Recommended):

Navigate to your project directory and create a virtual environment. This keeps dependencies required by different projects separate by creating isolated Python environments for them.

```
python -m venv venv
```

Activate the virtual environment:

- On Windows: `venv\Scripts\activate`
- On macOS and Linux: `source venv/bin/activate`

### 4. Install Dependencies:

Install the required Python package (`openai`) using pip:

```
pip install openai
```

### 5. API Key Configuration:

Create a `config.json` file in the root directory of your project and insert your OpenAI API key as shown below:

```json
{
  "api_key": "<Your-OpenAI-API-Key>"
}
```

Replace `<Your-OpenAI-API-Key>` with your actual API key.

### 6. Setting Up the Audio Configuration File:

Adjust the `audio_config.json` file to include the text you want to convert into speech and other configurations.

### 7. Running the Script:

To run the script, execute:

```
python text_to_speech.py
```

The script will read configurations from `audio_config.json`, generate audio files based on these settings, and save them in the specified directory.

## Configuration File (`audio_config.json`) Format

The configuration file should be structured as follows:

```json
{
  "audio_folder": "<Your-Desired-Audio-Output-Folder>",
  "audio_parts": [
    {
      "text": "Your text here",
      "filename": "output_filename.mp3",
      "generate": true or false
    },
    // Additional entries can be added here
  ]
}
```

## Additional Resources

For more information about the OpenAI Text-to-Speech API and its capabilities, please refer to the official OpenAI documentation:

- [OpenAI Text-to-Speech API Documentation](https://platform.openai.com/docs/guides/text-to-speech)

This resource is invaluable for understanding the full range of features offered by the API, including various models, voices, and advanced configurations.

## Contributing

Feel free to fork this project and contribute. If you have suggestions or improvements, your input is welcome. Please open an issue first to discuss what you would like to change, or directly submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
