from Flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(_name_)

@app.route("/emotionDetector")
def emot_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the detector function
    response = emotion_detector(text_to_analyze)
    
    # Format the response string dynamically
    output_str = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. The dominant emotion is *{response['dominant_emotion']}*."
    )
    return output_str

@app.route("/")
def render_index_page():
    return render_template('index.html')

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
