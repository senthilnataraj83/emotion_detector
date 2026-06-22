import requests
import json

def emotion_detector(text_to_analyze):
    # Corrected Watson NLP API URL endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Corrected dictionary syntax with matching curly braces
    headers = {"grpc-metadata-mm-model-id": "emotion_sn_watson_nlp_expr"}
    
    # Input JSON payload containing the text to analyze
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Sending a POST request to the API
    response = requests.post(url, json = myobj, headers = headers)
    
    # Return the raw text of the response
    return response.text
