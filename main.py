import pyttsx3
engine = pyttsx3.init()
def text_to_voice(text):
    engine.say(text)
    engine.runAndWait()

# Call the text_to_voice function to convert text to speech
text_to_voice("Hello, how are you?")

if __name__ == "__main__":
    text_to_voice("Hello, how are you?")
