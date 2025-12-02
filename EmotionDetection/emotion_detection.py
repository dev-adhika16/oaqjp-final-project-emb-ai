"""Emotion detection module using IBM Watson NLP service."""

import requests
import json


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the provided text using Watson NLP service.
    
    Args:
        text_to_analyze (str): The text to analyze for emotions.
    
    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Keys: anger, disgust, fear, joy, sadness, dominant_emotion
              On error, returns a dictionary with an 'error' key.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(input_data))

    if response.status_code == 200:
        emotion_predictions = response.json().get('emotionPredictions', [])
        if not emotion_predictions:
            return {"error": "No emotion predictions found in the response."}
          
        emotions = emotion_predictions[0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        anger = emotions.get('anger', 0)
        disgust = emotions.get('disgust', 0)
        fear = emotions.get('fear', 0)
        joy = emotions.get('joy', 0)
        sadness = emotions.get('sadness', 0)
        
        return {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        # Per requirement: for blank entries the upstream returns 400.
        # Return the same structure but with all values set to None so
        # callers can display a blank / placeholder response.
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        return {"error": f"Request failed with status code {response.status_code}"}
