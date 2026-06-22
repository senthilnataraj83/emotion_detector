"""
Server module for the AI-Based Emotion Detection application.
Uses Flask to serve a web interface that connects to the Watson NLP
backend for text emotion analysis.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(_name_)

@app.route("/emotionDetector")
def emot_detector():
    """
    Function to handle the request from the web interface, send text to the
    Backend, and return the formatted emotion analysis response.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the backend analysis service
    response = emotion_detector(text_to_analyze)

    # Check for the blank input error case handled in the function
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format and return the successful result string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is *{response['dominant_emotion']}*."
    )

@app.route("/")
def render_index_page():
    """
    Route function to render the main HTML application interface.
    """
    return render_template('index.html')

if _name_ == "_main_":
    # Start the server on host 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
