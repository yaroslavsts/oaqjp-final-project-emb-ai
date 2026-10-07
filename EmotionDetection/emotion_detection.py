"""Analyze text using the embeddable Watson Emotion Predict service."""

import json
import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return emotion scores and the dominant emotion, or None for HTTP 400."""
    response = requests.post(
        URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        },
        timeout=30,
    )
    if response.status_code == 400:
        return dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    response.raise_for_status()
    response_dict = json.loads(response.text)
    scores = response_dict["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
