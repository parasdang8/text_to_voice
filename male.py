import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for the male voice
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Input text to be converted to speech
text = " i am a student of thapar institute  "

# Set the male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Using the first male voice

# Convert text to speech
engine.say(text)
engine.runAndWait()