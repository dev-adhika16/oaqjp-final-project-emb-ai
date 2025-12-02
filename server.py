"""Flask server for Emotion Detection web app."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    """Render the home page with the emotion detection UI."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """API endpoint for emotion detection. Returns formatted result or error message."""
    # treat missing param as an error, but allow empty string so the
    # upstream service can respond and we can return a 200-friendly message
    text_to_analyze = request.args.get('textToAnalyze', None)

    if text_to_analyze is None:
        return "Please provide text to analyze.", 400

    result = emotion_detector(text_to_analyze)

    if 'error' in result:
        return f"Error: {result['error']}", 500

    # If the detector returns None for dominant_emotion (e.g. blank/invalid input),
    # show a friendly message to the user as requested.
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_message

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
