# Import the necessary library
try:
    from gtts import gTTS
except ImportError:
    print("The 'gTTS' library is not installed.")
    print("Please install it using: pip install gTTS")
    exit()

import os

"""
    Converts the given text into an audio file (MP3).

    Args:
        text_to_convert (str): The text you want to convert to speech.
        output_filename (str): The name of the file to save the audio to.
                               Defaults to 'output.mp3'.
                               If it doesn't end with '.mp3', it will be added.
        language (str): The language of the text (e.g., 'en' for English,
                        'es' for Spanish, 'fr' for French). Defaults to 'en'.
"""
def text_to_mp3(text_to_convert, output_filename="output.mp3", language='en'):
    
    try:
        # Ensure the filename ends with .mp3
        if not output_filename.lower().endswith('.mp3'):
            output_filename += '.mp3'
            print(f"Info: Appending .mp3 extension. Filename is now: {output_filename}")

        print(f"Converting text to speech (language: {language})...")

        # Create gTTS object
        # slow=False means the speech will be at normal speed
        tts = gTTS(text=text_to_convert, lang=language, slow=False)

        # Save the converted audio file
        tts.save(output_filename)

        print("-" * 30)
        print(f"Successfully converted text to audio!")
        print(f"Audio saved as: {output_filename}")
        print(f"Full path: {os.path.abspath(output_filename)}")
        print("-" * 30)

    except Exception as e:
        print("\nAn error occurred:")
        print(e)
        print("\nPlease check:")
        print("  - Your internet connection (gTTS requires it).")
        print("  - If the language code is valid.")
        print("  - If you have write permissions in the current directory.")

# --- Main execution part ---
if __name__ == "__main__":
    print("--- Text - to - MP3 Converter ---")

    # Get text input from the user
    my_text = input("Enter the text to convert to audio:\n> ")

    if not my_text:
        print("Error: No text entered. Exiting.")
    else:
        # Get desired filename from the user
        filename = input("Enter the desired output filename (e.g., my_audio.mp3) [press Enter for 'output.mp3']:\n> ")

        # Use default if no filename is provided
        if not filename:
            filename = "output.mp3"

        # (Optional) Get language input
        # lang_code = input("Enter language code (e.g., 'en', 'es', 'fr') [press Enter for 'en']:\n> ")
        # if not lang_code:
        #     lang_code = 'en'

        # Call the function to perform the conversion
        # text_to_mp3(my_text, filename, lang_code) # If using language input
        text_to_mp3(my_text, filename) # Using default English language

