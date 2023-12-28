"""
Executing this file will run the emotion detector
app on port 5000
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Method for deploying the emotion detector file
    on the server
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response["dominant_emotion"]
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return ("For the given statement, the system response is" +
    f"'anger': {anger_score}, 'disgust': {disgust_score}, 'fear':" +
    f"{fear_score}, 'joy': {joy_score}, and 'sadness': {sadness_score}." + 
    f"The dominant emotion is {dominant_emotion}.")

@app.route("/")
def render_index_page():
    """
    Method meant to render the index.html page with new data
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
