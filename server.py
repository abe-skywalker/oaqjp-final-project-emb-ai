"""Module for flask app. Provides an endpoint to the emotion_detector function."""

from flask import Flask, request
from .emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    """Method to serve /emotionDetector endpoint"""

    text_to_analyze = request.args.get('textToAnalyze','')
    print(text_to_analyze)
    results = emotion_detector(text_to_analyze)

    if results['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    resp = f"""For the given statement, the system response is
     'anger': {results['anger']},
     'disgust': {results['disgust']},
     'fear': {results['fear']},
     'joy': {results['joy']} and
     'sadness': {results['sadness']}.
     The dominant emotion is {results['dominant_emotion']}."""

    return resp


if __name__ == '__main__':
    app.run(debug=True)
