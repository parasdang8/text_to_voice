from flask import Flask, request, jsonify
import pyttsx3
import base64

app = Flask(_name_)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Text-to-Speech in Python</title>
        <style>
            button {
                background-color: blue; /* Set the background color of the button to blue */
                color: white; /* Set the text color to white for better contrast */
                padding: 10px 20px; /* Add padding to the button for better appearance */
                border: none; /* Remove the default button border */
                cursor: pointer; /* Change the cursor to a pointer on hover */
            }
        </style>
    </head>
    <body>
        <h1>Text-to-Speech in Python</h1>
        <textarea id="inputText" rows="4" cols="50" placeholder="Enter text to be converted to speech"></textarea><br>
        <button onclick="generateSpeech()">Generate Speech</button>

        <script>
            function generateSpeech() {
                var inputText = document.getElementById("inputText").value;

                // AJAX request to the server for speech generation
                var xhr = new XMLHttpRequest();
                xhr.open("POST", "/generate_speech", true);
                xhr.setRequestHeader("Content-Type", "application/json");

                xhr.onreadystatechange = function() {
                    if (xhr.readyState === 4 && xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        var audioElement = new Audio('data:audio/wav;base64,' + response.base64_audio);
                        audioElement.play();
                    }
                };

                xhr.send(JSON.stringify({ "text": inputText }));
            }
        </script>
    </body>
    </html>
    """

@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    data = request.json
    input_text = data.get('text')

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties for the female voice
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    print("Choose voice gender:")
    print("1. Male")
    print("2. Female")
    voice_choice = input("Enter 1 or 2: ")

    voices = engine.getProperty('voices')

    if voice_choice == "1":
        engine.setProperty('voice', voices[0].id) 
    else:
        engine.setProperty('voice', voices[1].id)

    # Convert text to speech
    engine.say(input_text)
    engine.save_to_file(input_text, 'output.mp3')
    engine.runAndWait()

    # Convert the speech to base64 for sending as a response
    with open("output.mp3", "rb") as audio_file:
        encoded_string = base64.b64encode(audio_file.read()).decode('utf-8')

    return jsonify({"base64_audio": encoded_string})

if _name_ == '_main_':
    app.run()