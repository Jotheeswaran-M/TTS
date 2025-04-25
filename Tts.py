import easyocr
import pyttsx3  # Import the pyttsx3 module

def extract_text_with_easyocr(image_path):
    reader = easyocr.Reader(['en'])  # You can add more languages, e.g., ['en', 'fr']
    results = reader.readtext(image_path)

    extracted_text = ""
    for detection in results:
        text = detection[1]
        extracted_text += text + "\n"

    return extracted_text

def text_to_speech(text):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    image_path = r"C:\Users\Admin\OneDrive\Pictures\Screenshots\1.png"
    text = extract_text_with_easyocr(image_path)

    print("\nExtracted Text:\n")
    print(text)

    # Convert the extracted text to speech
    print("\nConverting text to speech...\n")
    text_to_speech(text)
