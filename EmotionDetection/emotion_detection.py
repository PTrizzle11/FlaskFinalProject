"""
Python file for running the emotion_detector method
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Method for employing Watson Emotion detection
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = obj, headers = header, timeout = 10)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = {
        "anger": formatted_response["emotionPredictions"][0]["emotion"]["anger"],
        "disgust": formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
        "fear": formatted_response["emotionPredictions"][0]["emotion"]["fear"],
        "joy": formatted_response["emotionPredictions"][0]["emotion"]["joy"],
        "sadness": formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
        }
        dominant_emotion = max(emotions, key = emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
    elif response.status_code == 400:
        emotions = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
        }

    return emotions