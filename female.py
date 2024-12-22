import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the female voice
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Input text to be converted to speech
text = "hello i am Paras ,this is my female voice"

# Set the female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Using the second female voice
engine.setProperty('language', 'hi')

# Convert text to speech
engine.say(text)
engine.runAndWait()