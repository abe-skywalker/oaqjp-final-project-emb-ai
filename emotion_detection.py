### URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
### Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
### Input json: { "raw_document": { "text": text_to_analyse } }

import json
import requests

EP_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def max_score(scores_dict):
    return max(scores_dict, key=scores_dict.get)

def emotion_detector(text_to_analyse):
    res = requests.post(EP_URL,
    headers=HEADERS, 
    json={"raw_document": {"text": str(text_to_analyse)}})
    if res.status_code == 200:
        resp_json = json.loads(res.text)
        scores = resp_json["emotionPredictions"][0]["emotion"]
        scores["dominant_emotion"] = max_score(scores)
        return scores
    else:
        raise Exception(f"Something went wrong: ERROR {res.status_code} - {rex.text}")
