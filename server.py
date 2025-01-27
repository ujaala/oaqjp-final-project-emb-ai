"""
This is the starting file of the server.
It serves API requests with appropriate responses.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    It takes input text from user and sends it to the emotion detection function, 
    then returns a response based on the detected emotions. 
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Validate input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please provide non-empty input text."

    # Get response from the emotion detection function
    response = emotion_detector(text_to_analyze)

    # Check for errors in the response
    if 'error' in response:
        return response['error']

    # Extract emotion scores
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Unable to determine the dominant emotion."

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    It starts the server and serves the index.html page on the root endpoint. 
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
